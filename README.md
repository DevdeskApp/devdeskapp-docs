# 📖 DevDeskApp Documentation Portal

> Official documentation for the **DevDeskApp** platform, 350+ developer utilities, and the **`n8n-nodes-devdeskapp`** community node.

<div align="center">

[![Live Documentation](https://img.shields.io/badge/docs-docs.devdeskapp.com-6366f1?style=for-the-badge&logo=googlechrome&logoColor=white)](https://docs.devdeskapp.com)
[![NPM Package](https://img.shields.io/npm/v/n8n-nodes-devdeskapp?color=ea4b71&style=for-the-badge&logo=npm)](https://www.npmjs.com/package/n8n-nodes-devdeskapp)
[![n8n Template #21017](https://img.shields.io/badge/n8n.io-Template_%2321017-10b981?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities)
[![n8n Template #21130](https://img.shields.io/badge/n8n.io-Template_%2321130-3b82f6?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

</div>

---

## 🌟 What is DevDeskApp?

DevDeskApp is a modern, privacy-first developer ecosystem designed to eliminate sensitive data leaks:

1. **[DevDeskApp Web](https://www.devdeskapp.com/)**: Over 350+ browser-based utilities (JSON formatters, regex testers, cryptography tools, and CTC calculators) operating 100% client-side with zero external server tracking.
2. **[`n8n-nodes-devdeskapp`](https://www.npmjs.com/package/n8n-nodes-devdeskapp)**: Official n8n community node providing deterministic, in-memory execution in **< 0.2ms** with **zero cloud API exfiltration**.
3. **AI Agent Tool Calling**: Deterministic local function calling tools for LangChain, OpenAI, Google Gemini, Anthropic Claude, and Ollama agents inside n8n workflows.

---

## 📑 Documentation Structure

The documentation portal is built with **VitePress 1.6+** and structured into 5 core pillars:

| Section | Route | Description |
| :--- | :--- | :--- |
| **DevDeskApp Suite** | [`/about/`](https://docs.devdeskapp.com/about/) | Platform mission, zero-leak architecture, and privacy model. |
| **n8n Node Guide** | [`/n8n/`](https://docs.devdeskapp.com/n8n/) | UI installation, Docker deployment, and operational concepts. |
| **Templates Hub** | [`/templates/`](https://docs.devdeskapp.com/templates/) | Central catalog of official blueprints, parameter schemas, and 1-click import guides. |
| **AI Agents & LLMs** | [`/solutions/ai-agents`](https://docs.devdeskapp.com/solutions/ai-agents) | Connecting in-memory tools to AI Agents for hallucination-free payroll math and hashing. |
| **Enterprise Solutions** | [`/solutions/`](https://docs.devdeskapp.com/solutions/) | Benchmarks, concurrency limits, and native Node vs REST API latency comparisons. |

---

## 📋 Official n8n Workflow Templates

We provide verified, production-ready n8n blueprints published directly on the **n8n.io Creator Portal**:

- **🌟 [Template #21017: Developer Suite & Security Engine](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities)**
  - Sequential pipeline: JSON prettification, SHA-256 cryptographic hashing, RFC 4122 v4 UUID tracing, SEO slug generation, and CTC salary breakdown.
  - [Read Detailed Blueprint Guide →](https://docs.devdeskapp.com/templates/developer-suite)

- **💰 [Template #21130: CTC to In-Hand Salary Engine](https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp)**
  - Automated compensation modeling: Indian statutory PF calculation (12%), Professional Tax (PT), HRA allowance, and take-home salary projections.
  - [Read Detailed Blueprint Guide →](https://docs.devdeskapp.com/templates/ctc-salary-engine)

---

## ⚙️ 10 Native Operations Reference

`n8n-nodes-devdeskapp` provides 10 high-speed operations out of the box:

1. **`jsonPrettifier`**: Minify or format JSON with customizable indentation.
2. **`hashGenerator`**: Compute SHA-256, SHA-512, MD5, and SHA-1 cryptographic digests.
3. **`ctcCalculator`**: Indian statutory payroll engine (basic, HRA, PF, PT, and net monthly in-hand).
4. **`slugGenerator`**: SEO-friendly URL slug generation with multi-language transliteration.
5. **`base64Converter`**: Fast UTF-8 string encoding and decoding.
6. **`urlEncoder`**: Safe percent-encoding / decoding of query parameters.
7. **`uuidGenerator`**: Cryptographically secure RFC 4122 Version 4 UUIDs.
8. **`caseConverter`**: CamelCase, snake_case, kebab-case, and PascalCase transformations.
9. **`markdownToHtml`**: Sanitized Markdown rendering to HTML.
10. **`jwtDecoder`**: Header and payload claim inspection without signature verification.

---

## ⚡ Quick Node Installation

### In n8n Community Nodes UI:
1. In your n8n workspace: **Settings** → **Community Nodes** → **Install**.
2. Enter package name:
   ```text
   n8n-nodes-devdeskapp
   ```
3. Agree to the risks and click **Install**.

### Via Docker / CLI:
```bash
npm install n8n-nodes-devdeskapp
```

---

## 🤖 Machine-Readable AI Endpoints

For AI crawlers, LLMs, and autonomous agents, this documentation exposes clean markdown and context endpoints:

- **LLMs Index**: [`https://docs.devdeskapp.com/llms.txt`](https://docs.devdeskapp.com/llms.txt)
- **Comprehensive Full Context**: [`https://docs.devdeskapp.com/llms-full.txt`](https://docs.devdeskapp.com/llms-full.txt)

---

## 🔗 Official Ecosystem Links

- **Documentation Portal**: [https://docs.devdeskapp.com](https://docs.devdeskapp.com)
- **Web Platform**: [https://www.devdeskapp.com](https://www.devdeskapp.com)
- **Node NPM Package**: [https://www.npmjs.com/package/n8n-nodes-devdeskapp](https://www.npmjs.com/package/n8n-nodes-devdeskapp)
- **Node Source Code**: [https://github.com/DevdeskApp/n8n-nodes-devdeskapp](https://github.com/DevdeskApp/n8n-nodes-devdeskapp)
- **Template #21017**: [n8n.io/workflows/21017](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities)
- **Template #21130**: [n8n.io/workflows/21130](https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp)

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE) for more information.

Copyright © 2026 [DevDeskApp Community](https://github.com/DevdeskApp). All rights reserved.
