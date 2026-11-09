# Architecture Reference

## Table of Contents
- [System Layers](#system-layers)
- [Key File Locations](#key-file-locations)

---

## System Layers

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                              USER REQUEST                                    │
│              (query, report_type, report_source, tone, mcp_configs)         │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                         BACKEND API LAYER                                    │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐          │
│  │  FastAPI Server  │  │ WebSocket Manager│  │  Report Store    │          │
│  │  backend/server/ │  │ Real-time events │  │  JSON persistence│          │
│  │  app.py          │  │ websocket_mgr.py │  │  report_store.py │          │
│  └──────────────────┘  └──────────────────┘  └──────────────────┘          │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                    ResearchAgent (research_agent/agent.py)                   │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                         SKILLS LAYER                                   │  │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │  │
│  │  │ ResearchConductor│ │ ReportGenerator │ │ ContextManager  │         │  │
│  │  │ Plan & gather   │ │ Write reports   │ │ Similarity search│         │  │
│  │  │ researcher.py   │ │ writer.py       │ │ context_manager │         │  │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │  │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │  │
│  │  │ BrowserManager  │ │ SourceCurator   │ │ ImageGenerator  │         │  │
│  │  │ Web scraping    │ │ Rank sources    │ │ Gemini images   │         │  │
│  │  │ browser.py      │ │ curator.py      │ │ image_generator │         │  │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │  │
│  │  ┌─────────────────┐                                                  │  │
│  │  │ DeepResearchSkill│                                                 │  │
│  │  │ Recursive depth │                                                  │  │
│  │  │ deep_research.py│                                                  │  │
│  │  └─────────────────┘                                                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                        ACTIONS LAYER                                   │  │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │  │
│  │  │ report_generation│ │ query_processing│ │ web_scraping    │         │  │
│  │  │ LLM report write│ │ Sub-query plan  │ │ URL scraping    │         │  │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │  │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │  │
│  │  │ retriever.py    │ │ agent_creator   │ │ markdown_process│         │  │
│  │  │ Get retrievers  │ │ Choose agent    │ │ Parse markdown  │         │  │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                                                              │
│  ┌───────────────────────────────────────────────────────────────────────┐  │
│  │                       PROVIDERS LAYER                                  │  │
│  │  ┌─────────────────┐ ┌─────────────────┐ ┌─────────────────┐         │  │
│  │  │ LLM Provider    │ │ Retrievers      │ │ Scrapers        │         │  │
│  │  │ OpenAI,Anthropic│ │ Tavily,Google   │ │ BS4,Playwright  │         │  │
│  │  │ Google,Groq...  │ │ Bing,MCP...     │ │ PDF,DOCX...     │         │  │
│  │  │ llm_provider/   │ │ retrievers/     │ │ scraper/        │         │  │
│  │  └─────────────────┘ └─────────────────┘ └─────────────────┘         │  │
│  │  ┌─────────────────┐                                                  │  │
│  │  │ ImageGenerator  │                                                  │  │
│  │  │ Gemini/Imagen   │                                                  │  │
│  │  │ llm_provider/   │                                                  │  │
│  │  │ image/          │                                                  │  │
│  │  └─────────────────┘                                                  │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CONFIGURATION LAYER                                   │
│                     research_agent/config/                                   │
│                                                                              │
│     Environment Variables  →  JSON Config File  →  Default Values            │
│           (highest)              (medium)            (lowest)                │
│                                                                              │
│     config.py loads and merges all sources                                   │
│     variables/default.py contains all defaults                               │
│     variables/base.py defines TypedDict for type safety                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Key File Locations

| Need | Primary File | Key Classes/Functions |
|------|--------------|----------------------|
| Main orchestrator | `research_agent/agent.py` | `ResearchAgent` |
| Research logic | `research_agent/skills/researcher.py` | `ResearchConductor` |
| Report writing | `research_agent/skills/writer.py` | `ReportGenerator` |
| Context/embeddings | `research_agent/skills/context_manager.py` | `ContextManager` |
| Source ranking | `research_agent/skills/curator.py` | `SourceCurator` |
| Deep research | `research_agent/skills/deep_research.py` | `DeepResearchSkill` |
| Image generation | `research_agent/skills/image_generator.py` | `ImageGenerator` |
| All prompts | `research_agent/prompts.py` | `PromptFamily` |
| Configuration | `research_agent/config/config.py` | `Config` |
| Config defaults | `research_agent/config/variables/default.py` | `DEFAULT_CONFIG` |
| Config types | `research_agent/config/variables/base.py` | `BaseConfig` |
| API server | `backend/server/app.py` | FastAPI `app` |
| WebSocket mgmt | `backend/server/websocket_manager.py` | `WebSocketManager`, `run_agent` |
| Report types | `backend/report_type/` | `BasicReport`, `DetailedReport` |
| Search engines | `research_agent/retrievers/` | `TavilySearch`, `GoogleSearch`, etc. |
| Web scraping | `research_agent/scraper/` | Various scrapers |
| Enums | `research_agent/utils/enum.py` | `ReportType`, `ReportSource`, `Tone` |
