# auth.md - Agent Access & Registration Policy

**DevDeskApp Documentation (docs.devdeskapp.com)** provides public documentation for DevDeskApp developer utilities and the `n8n-nodes-devdeskapp` community node.

## No Authentication Required
- **Zero Auth**: All documentation pages, architecture guides, code examples, and template blueprints are 100% free and open access. No API keys, accounts, or bearer tokens are required.
- **Privacy First**: Payloads and data processed via DevDeskApp execute purely in-memory on the local host with zero external transmission.
- **Agent Friendly**: Autonomous AI agents, web crawlers, and LLM-assisted tools are explicitly permitted to read, parse, and cite all documentation pages under standard fair-use guidelines.

## Agent Registration
- Autonomous AI agents do not need to register credentials or negotiate tokens.
- For discovery endpoints, agents can query `/.well-known/ai-catalog.json`, `/.well-known/mcp/server-card.json`, and `/.well-known/agent-skills/index.json`.
- Rate Limit Policy: Politeness interval of 100ms between batch requests.
