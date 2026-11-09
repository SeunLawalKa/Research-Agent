"""available_images must not KeyError when entries lack url."""
import asyncio
import importlib.util
import pathlib
import sys
import types
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch

_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "research_agent"
    / "actions"
    / "report_generation.py"
)


def _load_module():
    pkg = types.ModuleType("research_agent")
    pkg.__path__ = [str(_PATH.parent.parent)]
    sys.modules.setdefault("research_agent", pkg)
    actions = types.ModuleType("research_agent.actions")
    actions.__path__ = [str(_PATH.parent)]
    sys.modules.setdefault("research_agent.actions", actions)

    for name in [
        "research_agent.config",
        "research_agent.config.config",
        "research_agent.utils",
        "research_agent.utils.llm",
        "research_agent.utils.logger",
        "research_agent.prompts",
        "research_agent.utils.enum",
    ]:
        if name not in sys.modules:
            sys.modules[name] = types.ModuleType(name)

    sys.modules["research_agent.utils.logger"].get_formatted_logger = lambda: __import__(
        "logging"
    ).getLogger("t")
    sys.modules["research_agent.prompts"].PromptFamily = object
    sys.modules["research_agent.prompts"].get_prompt_by_report_type = lambda *a, **k: (
        lambda *args, **kwargs: "PROMPT"
    )
    sys.modules["research_agent.utils.enum"].Tone = SimpleNamespace
    sys.modules["research_agent.config.config"].Config = object
    sys.modules["research_agent.utils.llm"].create_chat_completion = AsyncMock(
        return_value="REPORT"
    )

    # Avoid double-load running olderbodies
    mod_name = "research_agent.actions.report_generation_under_test2"
    spec = importlib.util.spec_from_file_location(mod_name, _PATH)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[mod_name] = mod
    spec.loader.exec_module(mod)
    return mod


def _cfg():
    return SimpleNamespace(
        smart_llm_model="m",
        smart_llm_provider="p",
        llm_kwargs={},
        report_format="markdown",
        total_words=100,
        language="en",
        stream_output=False,
        smart_token_limit=4000,
    )


def test_generate_report_skips_images_without_url():
    mod = _load_module()

    async def _run():
        with patch.object(mod, "create_chat_completion", new_callable=AsyncMock) as mock_cc:
            mock_cc.return_value = "REPORT OK"
            out = await mod.generate_report(
                query="q",
                context="ctx",
                agent_role_prompt="role",
                report_type="research_report",
                tone="objective",
                report_source="web",
                websocket=None,
                cfg=_cfg(),
                available_images=[
                    None,
                    "not-a-dict",
                    {"title": "no url"},
                    {"url": "", "title": "empty"},
                    {
                        "url": "https://img.example/a.png",
                        "title": "Good",
                        "section_hint": "Intro",
                    },
                ],
            )
            assert out == "REPORT OK"
            content = mock_cc.await_args.kwargs["messages"][1]["content"]
            assert "AVAILABLE IMAGES" in content
            assert "https://img.example/a.png" in content
            assert "Good" in content

    asyncio.run(_run())


def test_generate_report_all_invalid_images_omits_block():
    mod = _load_module()

    async def _run():
        with patch.object(mod, "create_chat_completion", new_callable=AsyncMock) as mock_cc:
            mock_cc.return_value = "R"
            await mod.generate_report(
                query="q",
                context="ctx",
                agent_role_prompt="role",
                report_type="research_report",
                tone="objective",
                report_source="web",
                websocket=None,
                cfg=_cfg(),
                available_images=[{"title": "x"}, None],
            )
            content = mock_cc.await_args.kwargs["messages"][1]["content"]
            assert "AVAILABLE IMAGES" not in content

    asyncio.run(_run())
