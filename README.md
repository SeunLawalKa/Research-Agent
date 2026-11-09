<div align="center" id="top">

<img src="https://github.com/SeunLawalKa/research-agent/assets/13554167/20af8286-b386-44a5-9a83-3be1365139c3" alt="Logo" width="80">


</div>

# 🔎 Research Agent

**Research Agent the first open deep research agent designed for both web and local research on any given task.** 

The agent produces detailed, factual, and unbiased research reports with citations. Research Agent provides a full suite of customization options to create tailor made and domain specific research agents. Research Agent goes well beyond RAG: planner and execution agents break each task into research questions, [decision models](#-smart-context-filtering-with-jev) keep only the context that is actually useful for answering them, [multi-agent](#-multi-agent-assistant) workflows coordinate specialized agents from planning to publication, and [recursive deep research](#-deep-research) explores a topic in both breadth and depth. Research runs in parallel, which keeps it fast, stable and reliable, and reduces misinformation.

**Our mission is to empower individuals and organizations with accurate, unbiased, and factual information through AI.**

## Why Research Agent?

- Objective conclusions for manual research can take weeks, requiring vast resources and time.
- LLMs trained on outdated information can hallucinate, becoming irrelevant for current research tasks.
- Current LLMs have token limitations, insufficient for generating long research reports.
- Limited web sources in existing services lead to misinformation and shallow results.
- Selective web sources can introduce bias into research tasks.

## Demo
<a href="https://www.youtube.com/watch?v=f60rlc_QCxE" target="_blank" rel="noopener">
  <img src="https://github.com/user-attachments/assets/ac2ec55f-b487-4b3f-ae6f-b8743ad296e4" alt="Demo video" width="800" target="_blank" />
</a>

## Install as Claude Skill

Extend Claude's deep research capabilities by installing Research Agent as a [Claude Skill](https://skills.sh/SeunLawalKa/research-agent/research-agent):

```bash
npx skills add SeunLawalKa/research-agent
```

Once installed, Claude can leverage Research Agent's deep research capabilities directly within your conversations.

## Architecture

The core idea is to utilize 'planner' and 'execution' agents. The planner generates research questions, while the execution agents gather relevant information. The publisher then aggregates all findings into a comprehensive report.

<div align="center">
<img align="center" height="600" src="https://github.com/SeunLawalKa/research-agent/assets/13554167/4ac896fd-63ab-4b77-9688-ff62aafcc527">
</div>

Steps:
* Create a task-specific agent based on a research query.
* Generate questions that collectively form an objective opinion on the task.
* Use a crawler agent for gathering information for each question.
* Summarize and source-track each resource.
* Filter and aggregate summaries into a final research report.

## Tutorials
 - [How it Works](https://docs.gptr.dev/blog/building-research-agent)
 - [How to Install](https://www.loom.com/share/04ebffb6ed2a4520a27c3e3addcdde20?sid=da1848e8-b1f1-42d1-93c3-5b0b9c3b24ea)
 - [Live Demo](https://www.loom.com/share/6a3385db4e8747a1913dd85a7834846f?sid=a740fd5b-2aa3-457e-8fb7-86976f59f9b8)

## Features

- 📝 Generate detailed research reports using web and local documents.
- 🖼️ Smart image scraping and filtering for reports.
- 🍌 **AI-generated inline images** using Google Gemini (Nano Banana) for visual illustrations.
- 📜 Generate detailed reports exceeding 2,000 words.
- 🌐 Aggregate over 20 sources for objective conclusions.
- 🎯 Smart context filtering with [Jev](#-smart-context-filtering-with-jev), with no API key or embeddings required by default.
- 🖥️ Frontend available in lightweight (HTML/CSS/JS) and production-ready (NextJS + Tailwind) versions.
- 🔍 JavaScript-enabled web scraping.
- 📂 Maintains memory and context throughout research.
- 📄 Export reports to PDF, Word, and other formats.

## 📖 Documentation

See the [Documentation](https://docs.gptr.dev/docs/research-agent/getting-started) for:
- Installation and setup guides
- Configuration and customization options
- How-To examples
- Full API references

## ⚙️ Getting Started

### Installation

1. Install Python 3.12 or later. [Guide](https://www.tutorialsteacher.com/python/install-python).
2. Clone the project and navigate to the directory:

    ```bash
    git clone https://github.com/SeunLawalKa/research-agent.git
    cd research-agent
    ```

3. Set up API keys by exporting them or storing them in a `.env` file.

    ```bash
    export OPENAI_API_KEY={Your OpenAI API Key here}
    export TAVILY_API_KEY={Your Tavily API Key here}
    ```

    (Optional) For enhanced tracing and observability, you can also set:
    
    ```bash
    # export LANGCHAIN_TRACING_V2=true
    # export LANGCHAIN_API_KEY={Your LangChain API Key here}
    ```

    For custom OpenAI-compatible APIs (e.g., local models, other providers), you can also set:
    
    ```bash
    export OPENAI_BASE_URL={Your custom API base URL here}
    ```

4. Install dependencies and start the server:

    ```bash
    pip install -r requirements.txt
    python -m uvicorn main:app --reload
    ```

Visit [http://localhost:8000](http://localhost:8000) to start.


## Run as PIP package
```bash
pip install research-agent

```
### Example Usage:
```python
...
from research_agent import ResearchAgent

query = "why is Nvidia stock going up?"
researcher = ResearchAgent(query=query)
# Conduct research on the given query
research_result = await researcher.conduct_research()
# Write the report
report = await researcher.write_report()
...
```

### 🔧 MCP Client
Research Agent supports MCP integration to connect with specialized data sources like GitHub repositories, databases, and custom APIs. This enables research from data sources alongside web search.

```bash
export RETRIEVER=tavily,mcp  # Enable hybrid web + MCP research
```

```python
from research_agent import ResearchAgent
import asyncio
import os

async def mcp_research_example():
    # Enable MCP with web search
    os.environ["RETRIEVER"] = "tavily,mcp"
    
    researcher = ResearchAgent(
        query="What are the top open source web research agents?",
        mcp_configs=[
            {
                "name": "github",
                "command": "npx",
                "args": ["-y", "@modelcontextprotocol/server-github"],
                "env": {"GITHUB_TOKEN": os.getenv("GITHUB_TOKEN")}
            }
        ]
    )
    
    research_result = await researcher.conduct_research()
    report = await researcher.write_report()
    return report
```

> For comprehensive MCP documentation and advanced examples, visit the [MCP Integration Guide](https://docs.gptr.dev/docs/research-agent/retrievers/mcp-configs).

## 🍌 Inline Image Generation

Research Agent can automatically generate and embed AI-created illustrations in your research reports using Google's Gemini models (Nano Banana).

```bash
# Enable in your .env file
IMAGE_GENERATION_ENABLED=true
GOOGLE_API_KEY=your_google_api_key
IMAGE_GENERATION_MODEL=models/gemini-2.5-flash-image
```

When enabled, the system will:
1. Analyze your research context to identify visualization opportunities
2. Pre-generate 2-3 relevant images during the research phase
3. Embed them inline as the report is written

Images are generated with dark-mode styling that matches the Research Agent UI, featuring professional infographic aesthetics with teal accents.

[Learn more about Image Generation](https://docs.gptr.dev/docs/research-agent/gptr/image_generation) in our documentation.

## ✨ Deep Research

Research Agent now includes Deep Research - an advanced recursive research workflow that explores topics with agentic depth and breadth. This feature employs a tree-like exploration pattern, diving deeper into subtopics while maintaining a comprehensive view of the research subject.

- 🌳 Tree-like exploration with configurable depth and breadth
- ⚡️ Concurrent processing for faster results
- 🤝 Smart context management across research branches
- ⏱️ Takes ~5 minutes per deep research
- 💰 Costs ~$0.4 per research (using `o3-mini` on "high" reasoning effort)

[Learn more about Deep Research](https://docs.gptr.dev/docs/research-agent/gptr/deep_research) in our documentation.

## 🎯 Smart Context Filtering with Jev

Every research run scrapes dozens of pages, and only some of each page helps answer the question. Before anything reaches the LLM, Research Agent decides which passages to keep. By default it uses **[Jev](https://typesafe.ai/blog/introducing-system-one-models-and-jev)** by TypeSafe, a model that scores how useful each passage is for the question, rather than how similar its words or embedding are.

**Jev's context is 59% more relevant than embeddings, at the same cost** (73% of kept passages relevant vs 46%). We benchmarked every option on 28 research tasks, replaying the same scraped sources so that only the filter changed:

| Context filter | Relevant passages kept | Head-to-head vs embeddings | Filter time | Cost per report | Needs |
|---|---|---|---|---|---|
| **Jev** (default) | **73%** | **15 wins · 10 ties · 3 losses** | 1.7s | $0.115 | `TYPESAFE_API_KEY` |
| Keyword (fallback) | 51% | 14 wins · 8 ties · 6 losses | 0.02s | $0.116 | nothing |
| Embeddings | 46% | — | 1.0s | $0.117 | an embedding provider |
| No filter | — | 13 wins · 11 ties · 4 losses | — | $0.192 | nothing |

Writing the report takes ~45s whichever filter you use, so a run's total time moves only by the filter step. Passing every page unfiltered writes the broadest reports on open-ended questions, but costs 65% more.

**Nothing is required.** With a `TYPESAFE_API_KEY`, Jev is used. Without one, or if a Jev call fails, Research Agent falls back to keyword (BM25) ranking, which runs locally with no API key, model or embeddings. Embeddings remain available as an option.

```bash
export TYPESAFE_API_KEY=...   # use Jev (the default when a key is set)
export CONTEXT_FILTER=auto    # auto | jev | keyword | embeddings | none
```

See the [Context Filter docs](https://docs.gptr.dev/docs/research-agent/gptr/context-filter) and the [full benchmark](evals/context_filter) for method, caveats and how to reproduce it.

## Run with Docker

> **Step 1** - [Install Docker](https://docs.gptr.dev/docs/research-agent/getting-started/getting-started-with-docker)

> **Step 2** - Clone the '.env.example' file, add your API Keys to the cloned file and save the file as '.env'

> **Step 3** - Within the docker-compose file comment out services that you don't want to run with Docker.

```bash
docker-compose up --build
```

If that doesn't work, try running it without the dash:
```bash
docker compose up --build
```

> **Step 4** - By default, if you haven't uncommented anything in your docker-compose file, this flow will start 2 processes:
 - the Python server running on localhost:8000<br>
 - the React app running on localhost:3000<br>

Visit localhost:3000 on any browser and enjoy researching!


## 📄 Research on Local Documents

You can instruct the Research Agent to run research tasks based on your local documents. Currently supported file formats are: PDF, plain text, CSV, Excel, Markdown, PowerPoint, and Word documents.

Step 1: Add the env variable `DOC_PATH` pointing to the folder where your documents are located.

```bash
export DOC_PATH="./my-docs"
```

Step 2: 
 - If you're running the frontend app on localhost:8000, simply select "My Documents" from the "Report Source" Dropdown Options.
 - If you're running Research Agent with the [PIP package](https://docs.tavily.com/guides/research-agent/research-agent#pip-package), pass the `report_source` argument as "local" when you instantiate the `ResearchAgent` class [code sample here](https://docs.gptr.dev/docs/research-agent/context/tailored-research).


## 🤖 MCP Server

We've moved our MCP server to a dedicated repository: [gptr-mcp](https://github.com/SeunLawalKa/gptr-mcp).

The Research Agent MCP Server enables AI applications like Claude to conduct deep research. While LLM apps can access web search tools with MCP, Research Agent MCP delivers deeper, more reliable research results.

Features:
- Deep research capabilities for AI assistants
- Higher quality information with optimized context usage
- Comprehensive results with better reasoning for LLMs
- Claude Desktop integration

For detailed installation and usage instructions, please visit the [official repository](https://github.com/SeunLawalKa/gptr-mcp).


## 👪 Multi-Agent Assistant
As AI evolves from prompt engineering and RAG to multi-agent systems, we're excited to introduce multi-agent assistants built with [LangGraph](https://python.langchain.com/v0.1/docs/langgraph/) and [AG2](https://github.com/ag2ai/ag2).

By using multi-agent frameworks, the research process can be significantly improved in depth and quality by leveraging multiple agents with specialized skills. This project showcases how a team of AI agents can work together to conduct research on a given topic, from planning to publication.

An average run generates a 5-6 page research report in multiple formats such as PDF, Docx and Markdown.

Check it out [here](https://github.com/SeunLawalKa/research-agent/tree/master/multi_agents) or head over to our documentation for [LangGraph](https://docs.gptr.dev/docs/research-agent/multi_agents/langgraph) and [AG2](https://docs.gptr.dev/docs/research-agent/multi_agents/ag2) for more information.

## 🔍 Observability

Research Agent supports **LangSmith** for enhanced tracing and observability, making it easier to debug and optimize complex multi-agent workflows.

To enable tracing:
1. Set the following environment variables:
   ```bash
   export LANGCHAIN_TRACING_V2=true
   export LANGCHAIN_API_KEY=your_api_key
   export LANGCHAIN_PROJECT="research-agent"
   ```
2. Run your research tasks as usual. All LangGraph-based agent interactions will be automatically traced and visualized in your LangSmith dashboard.

## 🖥️ Frontend Applications

research-agent now features an enhanced frontend to improve the user experience and streamline the research process. The frontend offers:

- An intuitive interface for inputting research queries
- Real-time progress tracking of research tasks
- Interactive display of research findings
- Customizable settings for tailored research experiences

Two deployment options are available:
1. A lightweight static frontend served by FastAPI
2. A feature-rich NextJS application for advanced functionality

For detailed setup instructions and more information about the frontend features, please visit our [documentation page](https://docs.gptr.dev/docs/research-agent/frontend/introduction).

## 🚀 Contributing
We highly welcome contributions! Please check out [contributing](https://github.com/SeunLawalKa/research-agent/blob/master/CONTRIBUTING.md) if you're interested.

Please check out our [roadmap](https://trello.com/b/3O7KBePw/research-agent-roadmap) page and reach out to us via our [Discord community](https://discord.gg/QgZXvJAccX) if you're interested in joining our mission.
<a href="https://github.com/SeunLawalKa/research-agent/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=SeunLawalKa/research-agent&max=1000" />
</a>
## ✉️ Support / Contact us
- [Community Discord](https://discord.gg/spBgZmm3Xe)
- Author Email: seunlawalka@gmail.com

## 🛡 Disclaimer

This project, Research Agent, is an experimental application and is provided "as-is" without any warranty, express or implied. We are sharing codes for academic purposes under the Apache 2 license. Nothing herein is academic advice, and NOT a recommendation to use in academic or research papers.

Our view on unbiased research claims:
1. The main goal of Research Agent is to reduce incorrect and biased facts. How? We assume that the more sites we scrape the less chances of incorrect data. By scraping multiple sites per research, and choosing the most frequent information, the chances that they are all wrong is extremely low.
2. We do not aim to eliminate biases; we aim to reduce it as much as possible. **We are here as a community to figure out the most effective human/llm interactions.**
3. In research, people also tend towards biases as most have already opinions on the topics they research about. This tool scrapes many opinions and will evenly explain diverse views that a biased person would never have read.

---

<p align="center">
<a href="https://star-history.com/#SeunLawalKa/research-agent">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=SeunLawalKa/research-agent&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=SeunLawalKa/research-agent&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=SeunLawalKa/research-agent&type=Date" />
  </picture>
</a>
</p>


<p align="right">
  <a href="#top">⬆️ Back to Top</a>
</p>
