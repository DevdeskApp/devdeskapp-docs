# auth.md

**DevDeskApp Documentation (docs.devdeskapp.com)** provides public documentation for DevDeskApp developer utilities and the `n8n-nodes-devdeskapp` community node.

## Agent Registration

Autonomous AI agents, automated indexers, and LLM clients can register and access all developer resources and documentation using standard discovery protocols:

- **Audience**: AI Agents, LLM crawlers, autonomous agents
- **Registration Endpoint**: https://docs.devdeskapp.com/auth.md
- **Provisioning Endpoint**: https://docs.devdeskapp.com/auth.md
- **Register URI**: https://docs.devdeskapp.com/auth.md
- **Claim URI**: https://docs.devdeskapp.com/auth.md
- **Supported Identity Types**: anonymous, identity_assertion
- **Supported Methods**: anonymous, identity_assertion
- **Supported Credential Types**: none, bearer
- **Scopes Supported**: public, read
- **Grant Types**: implicit, anonymous

### Access Control & Privacy
- **Zero Authentication Required**: All documentation, architecture articles, and workflow blueprints are 100% free and open access. No API keys, accounts, or bearer tokens are required.
- **Privacy First**: Payloads and data processed via DevDeskApp execute purely in-memory on the local host with zero external transmission.
- **Credentials Use**: Public documentation endpoints require no credentials. Scoped agent operations accept RFC 6750 Bearer headers or anonymous tokens.
- **Politeness Policy**: 100ms interval between batch requests.

## Discovery Resources
- ARD AI Catalog: https://docs.devdeskapp.com/.well-known/ai-catalog.json
- MCP Server Card: https://docs.devdeskapp.com/.well-known/mcp/server-card.json
- Agent Skills Discovery: https://docs.devdeskapp.com/.well-known/agent-skills/index.json
- Protected Resource Metadata: https://docs.devdeskapp.com/.well-known/oauth-protected-resource
- OAuth Authorization Server: https://docs.devdeskapp.com/.well-known/oauth-authorization-server
