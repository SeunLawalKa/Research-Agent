# Claude Skill

Research Agent is available as a [Claude Skill](https://skills.sh/SeunLawalKa/research-agent/research-agent), allowing you to extend Claude's research capabilities directly within Claude Code and other Claude-powered applications.

## What are Claude Skills?

Skills are modular packages that extend Claude's capabilities by providing specialized knowledge, workflows, and tools. When you install Research Agent as a skill, Claude gains access to deep research procedures, helping it conduct comprehensive research with citations.

## Installation

Install Research Agent as a Claude Skill using the skills CLI:

```bash
npx skills add SeunLawalKa/research-agent
```

This installs the skill from the [Research Agent GitHub repository](https://github.com/SeunLawalKa/research-agent).

## What's Included

The Research Agent skill provides Claude with:

- **Architecture Knowledge** - Understanding of the planner-executor-publisher pattern
- **Component Signatures** - Method signatures for `ResearchAgent`, `ResearchConductor`, `ReportGenerator`
- **Integration Patterns** - How to add features, retrievers, and customize workflows
- **Configuration Reference** - All environment variables and config options
- **API Reference** - REST and WebSocket API documentation

## Usage

Once installed, Claude can help you with:

- Understanding Research Agent's architecture
- Adding new features following the 8-step pattern
- Debugging research pipelines
- Integrating MCP data sources
- Customizing report generation
- Adding new retrievers

## Skill Structure

The skill is located in the `.claude/` directory of the repository:

```
.claude/
├── SKILL.md              # Main skill file (lean, <500 lines)
└── references/           # Detailed documentation
    ├── architecture.md
    ├── components.md
    ├── flows.md
    ├── prompts.md
    ├── retrievers.md
    ├── mcp.md
    ├── deep-research.md
    ├── multi-agents.md
    ├── adding-features.md
    ├── advanced-patterns.md
    ├── api-reference.md
    └── config-reference.md
```

## Learn More

- [Skills.sh - Research Agent](https://skills.sh/SeunLawalKa/research-agent/research-agent) - View on skills.sh registry
- [Claude Code Documentation](https://docs.claude.com/en/docs/claude-code/skills) - Official skills documentation
- [Research Agent Documentation](https://docs.gptr.dev) - Full project documentation
