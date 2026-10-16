# About DevDeskApp

DevDeskApp is an all-in-one developer productivity platform and open-source automation utility suite. It provides modern engineering and operations teams with over 330+ developer utilities, calculators, encoders, and workflow tools designed to run with maximum speed and absolute privacy.

## Mission and Vision

Every day, software engineers, DevOps professionals, and automation builders copy and paste sensitive data into ad-hoc online tools:
- Database connection strings and API payloads into online JSON formatters.
- Plaintext passwords and secret tokens into third-party hash generators.
- Employee payroll and compensation numbers into random calculator websites.

DevDeskApp eliminates this security vulnerability by delivering a comprehensive suite of utilities that execute locally in your environment:
1. **DevDeskApp Web**: Runs 100% inside your browser using client-side JavaScript and WebAssembly. No telemetry, no server logs, and no remote data storage.
2. **n8n Community Node (`n8n-nodes-devdeskapp`)**: Runs natively inside your n8n workflow engine as local Node.js functions. No HTTP API calls, no third-party downtime, and zero cloud exfiltration.

---

## The DevDeskApp Ecosystem

The platform spans two core components:

### 1. DevDeskApp Web Platform
The flagship web portal houses more than 330 tools categorized for daily developer workflows:
- **Formatters & Beautifiers**: JSON, XML, HTML, CSS, SQL, GraphQL, YAML.
- **Crypto & Security**: MD5, SHA-1, SHA-256, SHA-512, HMAC, AES, RSA key generators, JWT decoders.
- **Encoders & Decoders**: Base64, URL, HTML entities, Hex, Unicode, Punycode.
- **Generators**: UUID v4, NanoID, Lorem Ipsum, QR codes, Strong passwords, Dummy data.
- **Calculators & Converters**: CTC salary breakdown, in-hand tax estimation, unit converters, timestamp/epoch converters.

### 2. n8n Community Node
An official n8n community package (`n8n-nodes-devdeskapp`) that brings core DevDeskApp processing capabilities directly into workflow automation pipelines. With seamless n8n UI integration, users can sanitize payloads, calculate salaries, hash sensitive fields, and format strings without writing custom JavaScript code.

---

## Core Principles

- **Zero-Trust Privacy**: Your data belongs to you. No inputs or outputs are ever transmitted to external endpoints.
- **Speed & Efficiency**: Instant execution without network latency.
- **Standards Compliance**: Tested against strict formatting and calculation standards (including official Indian payroll PF, ESI, PT, and Tax regulations).
- **Open Architecture**: Open-source, extensible, and fully transparent.
