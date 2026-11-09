# Research Agent UI

A React component library for integrating the Research Agent interface into your React applications. Take it for a test ride with the [GPTR React Starter Template](https://github.com/elishakay/research-agent-react), or simply:

<div align="center" id="top">

<img src="https://github.com/SeunLawalKa/research-agent/assets/13554167/20af8286-b386-44a5-9a83-3be1365139c3" alt="Logo" width="80">

####

[![Website](https://img.shields.io/badge/Official%20Website-gptr.dev-teal?style=for-the-badge&logo=world&logoColor=white&color=0891b2)](https://gptr.dev)
[![Documentation](https://img.shields.io/badge/Documentation-DOCS-f472b6?logo=googledocs&logoColor=white&style=for-the-badge)](https://docs.gptr.dev)
[![Discord Follow](https://dcbadge.vercel.app/api/server/QgZXvJAccX?style=for-the-badge&theme=clean-inverted&?compact=true)](https://discord.gg/QgZXvJAccX)

[![PyPI version](https://img.shields.io/pypi/v/research-agent?logo=pypi&logoColor=white&style=flat)](https://badge.fury.io/py/research-agent)
![GitHub Release](https://img.shields.io/github/v/release/SeunLawalKa/research-agent?style=flat&logo=github)
[![Open In Colab](https://img.shields.io/static/v1?message=Open%20in%20Colab&logo=googlecolab&labelColor=grey&color=yellow&label=%20&style=flat&logoSize=40)](https://colab.research.google.com/github/SeunLawalKa/research-agent/blob/master/docs/docs/examples/pip-run.ipynb)
[![Docker Image Version](https://img.shields.io/docker/v/elestio/research-agent/latest?arch=amd64&style=flat&logo=docker&logoColor=white&color=1D63ED)](https://hub.docker.com/r/ResearchAgent/research-agent)

[English](README.md) | [中文](README-zh_CN.md) | [日本語](README-ja_JP.md) | [한국어](README-ko_KR.md)

</div>

# 🔎 Research Agent

**Research Agent is an open deep research agent designed for both web and local research on any given task.** 

The agent produces detailed, factual, and unbiased research reports with citations. Research Agent provides a full suite of customization options to create tailor made and domain specific research agents. Research Agent goes well beyond RAG: planner and execution agents break each task into research questions, [decision models](https://docs.gptr.dev/docs/research-agent/gptr/context-filter) keep only the context that is actually useful for answering them, [multi-agent](https://docs.gptr.dev/docs/research-agent/multi_agents/langgraph) workflows coordinate specialized agents from planning to publication, and [recursive deep research](https://docs.gptr.dev/docs/research-agent/gptr/deep_research) explores a topic in both breadth and depth. Research runs in parallel, which keeps it fast, stable and reliable, and reduces misinformation.

**Our mission is to empower individuals and organizations with accurate, unbiased, and factual information through AI.**


## Installation

```bash
npm install research-agent-ui
```

## Usage

```javascript
import React from 'react';
import { ResearchAgent } from 'research-agent-ui';

function App() {
  return (
    <div className="App">
      <ResearchAgent 
        apiUrl="http://localhost:8000"
        defaultPrompt="What is quantum computing?"
        onResultsChange={(results) => console.log('Research results:', results)}
      />
    </div>
  );
}

export default App;
```

## Advanced Usage

```javascript
import React, { useState } from 'react';
import { ResearchAgent } from 'research-agent-ui';

function App() {
  const [results, setResults] = useState([]);

  const handleResultsChange = (newResults) => {
    setResults(newResults);
    console.log('Research progress:', newResults);
  };

  return (
    <div className="App">
      <h1>My Research Application</h1>
      
      <ResearchAgent 
        apiUrl="http://localhost:8000"
        apiKey="your-api-key-if-needed"
        defaultPrompt="Explain the impact of quantum computing on cryptography"
        onResultsChange={handleResultsChange}
      />
      
      {/* You can use the results state elsewhere in your app */}
      <div className="results-summary">
        {results.length > 0 && (
          <p>Research in progress: {results.length} items processed</p>
        )}
      </div>
    </div>
  );
}

export default App;
```