# Auth.md

**DevDeskApp Documentation (docs.devdeskapp.com)** provides public documentation for DevDeskApp developer utilities and the `n8n-nodes-devdeskapp` community node.

## Agent Registration
Autonomous AI agents can register and access all developer resources and documentation using standard discovery protocols:

- **Registration Endpoint**: `https://docs.devdeskapp.com/.well-known/oauth-authorization-server`
- **Supported Identity Types**: `anonymous`, `agent`
- **Supported Credential Types**: `none`
- **Register URI**: `https://docs.devdeskapp.com/auth.md`
- **Scopes Supported**: `public`, `read`
- **Grant Types**: `implicit`, `anonymous`

### Access Control & Privacy
- **Zero Authentication Required**: All documentation, architecture articles, and workflow blueprints are 100% free and open access. No API keys, accounts, or bearer tokens are required.
- **Privacy First**: Payloads and data processed via DevDeskApp execute purely in-memory on the local host with zero external transmission.
- **Politeness Policy**: 100ms interval between batch requests.

## Discovery Resources
- ARD AI Catalog: `https://docs.devdeskapp.com/.well-known/ai-catalog.json`
- MCP Server Card: `https://docs.devdeskapp.com/.well-known/mcp/server-card.json`
- Agent Skills Discovery: `https://docs.devdeskapp.com/.well-known/agent-skills/index.json`
- Protected Resource Metadata: `https://docs.devdeskapp.com/.well-known/oauth-protected-resource`
