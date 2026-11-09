"""BeautifulSoupScraper must not AttributeError when session is None."""

import importlib.util
import sys
import types
from pathlib import Path
from unittest.mock import MagicMock

ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "research_agent" / "scraper" / "beautiful_soup" / "beautiful_soup.py"


def _load():
    # package stubs for relative imports
    pkg = types.ModuleType("research_agent")
    pkg.__path__ = [str(ROOT / "research_agent")]
    sys.modules.setdefault("research_agent", pkg)
    sc = types.ModuleType("research_agent.scraper")
    sc.__path__ = [str(ROOT / "research_agent" / "scraper")]
    sys.modules["research_agent.scraper"] = sc
    bs_pkg = types.ModuleType("research_agent.scraper.beautiful_soup")
    bs_pkg.__path__ = [str(ROOT / "research_agent" / "scraper" / "beautiful_soup")]
    sys.modules["research_agent.scraper.beautiful_soup"] = bs_pkg

    utils = types.ModuleType("research_agent.scraper.utils")
    utils.get_relevant_images = lambda *a, **k: []
    utils.extract_title = lambda soup: ""
    utils.get_text_from_soup = lambda soup: "text"
    utils.clean_soup = lambda soup: soup
    sys.modules["research_agent.scraper.utils"] = utils

    bs4 = types.ModuleType("bs4")
    bs4.BeautifulSoup = MagicMock
    sys.modules["bs4"] = bs4

    for key in list(sys.modules):
        if key.endswith("bs_none_testmod"):
            sys.modules.pop(key)

    spe = importlib.util.spec_from_file_location(
        "research_agent.scraper.beautiful_soup.bs_none_testmod", MODULE_PATH
    )
    mod = importlib.util.module_from_spec(spe)
    sys.modules[spe.name] = mod
    spe.loader.exec_module(mod)
    return mod


def test_scrape_with_none_session_returns_empty():
    mod = _load()
    content, images, title = mod.BeautifulSoupScraper(
        "https://example.com", session=None
    ).scrape()
    assert (content, images, title) == ("", [], "")
