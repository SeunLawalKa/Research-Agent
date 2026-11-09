# npm package

The [research-agent npm package](https://www.npmjs.com/package/research-agent) is a WebSocket client for interacting with Research Agent.

## Installation

```bash
npm install research-agent
```

## Usage

```javascript
const ResearchAgent = require('research-agent');

const researcher = new ResearchAgent({
  host: 'localhost:8000',
  logListener: (data) => console.log('logListener logging data: ',data)
});

researcher.sendMessage({
  query: 'Does providing better context reduce LLM hallucinations?',
  moreContext: 'Provide a detailed answer'
});
```
