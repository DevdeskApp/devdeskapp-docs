# 📖 DevDeskApp Documentation Portal

> Official documentation for the **DevDeskApp** platform (340+ browser-based developer tools) and the **`n8n-nodes-devdeskapp`** community node.

<div align="center">

[![Live Documentation](https://img.shields.io/badge/docs-docs.devdeskapp.com-6366f1?style=for-the-badge&logo=googlechrome&logoColor=white)](https://docs.devdeskapp.com)
[![NPM Package](https://img.shields.io/npm/v/n8n-nodes-devdeskapp?color=ea4b71&style=for-the-badge&logo=npm)](https://www.npmjs.com/package/n8n-nodes-devdeskapp)
[![n8n Template #21017](https://img.shields.io/badge/n8n.io-Template_%2321017-10b981?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/)
[![n8n Template #21130](https://img.shields.io/badge/n8n.io-Template_%2321130-3b82f6?style=for-the-badge&logo=n8n&logoColor=white)](https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)](LICENSE)

</div>

---

## 🌟 What is DevDeskApp?

1. **[DevDeskApp Web](https://www.devdeskapp.com/)**: 340+ browser-based tools (JSON formatters, hash generators, encoders, CTC and HR calculators) that process your input in the browser.
2. **[`n8n-nodes-devdeskapp`](https://www.npmjs.com/package/n8n-nodes-devdeskapp)**: an n8n community node with 19 operations that run inside your n8n process with no external API calls.
3. **AI Agent tools**: the node declares `usableAsTool: true`, so n8n AI Agents can call it for exact salary maths, hashes and JSON formatting.

---

## 📑 Documentation structure

Built with **VitePress 1.6**:

| Section | Route | Description |
| :--- | :--- | :--- |
| **DevDeskApp Suite** | [`/about/`](https://docs.devdeskapp.com/about/) | Platform, architecture and privacy model |
| **n8n Node Guide** | [`/n8n/`](https://docs.devdeskapp.com/n8n/) | Installation, Docker and the operations reference |
| **Templates Hub** | [`/templates/`](https://docs.devdeskapp.com/templates/) | The 7 published n8n templates and the import guide |
| **AI Agents & LLMs** | [`/solutions/ai-agents`](https://docs.devdeskapp.com/solutions/ai-agents) | Using the node as an AI Agent tool |
| **Enterprise Solutions** | [`/solutions/`](https://docs.devdeskapp.com/solutions/) | Local node vs cloud API, with measured timings |

---

## 📋 Published n8n templates

| ID | Template | Docs |
| :--- | :--- | :--- |
| #21017 | [Developer Suite & Security Engine](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/) | [Guide](https://docs.devdeskapp.com/templates/developer-suite) |
| #21130 | [CTC to In-Hand Salary Engine](https://n8n.io/workflows/21130-generate-indian-ctc-offers-and-payroll-breakdowns-with-devdeskapp/) | [Guide](https://docs.devdeskapp.com/templates/ctc-salary-engine) |
| #21376 | [Payment Webhook Sanitizer](https://n8n.io/workflows/21376-sanitize-and-audit-payment-webhooks-with-devdeskapp-json-and-crypto-tools/) | [Guide](https://docs.devdeskapp.com/templates/payment-webhook-sanitizer) |
| #21593 | [AI LLM JSON into Postgres](https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/) | [Guide](https://docs.devdeskapp.com/templates/ai-llm-postgres-ingest) |
| #21594 | [CTC Offer Letter Generator](https://n8n.io/workflows/21594-generate-indian-ctc-offer-letters-with-devdeskapp-google-docs-gmail-and-slack/) | [Guide](https://docs.devdeskapp.com/templates/offer-letter-generator) |
| #21595 | [Meta CAPI Lead Sync](https://n8n.io/workflows/21595-hash-and-sync-leads-to-meta-capi-with-devdeskapp-google-sheets-and-slack/) | [Guide](https://docs.devdeskapp.com/templates/meta-capi-lead-sync) |
| #21596 | [Notion to WordPress Publisher](https://n8n.io/workflows/21596-publish-seo-safe-notion-blog-posts-to-wordpress-with-devdeskapp-and-slack/) | [Guide](https://docs.devdeskapp.com/templates/notion-wordpress-publisher) |

---

## ⚙️ 19 operations in 5 resources

| Resource | Operations |
| :--- | :--- |
| **JSON** (`json`) | `prettify`, `minify`, `validate` |
| **Crypto** (`crypto`) | `hash` (md5, sha1, sha256, sha512), `base64Encode`, `base64Decode`, `uuid` |
| **Text** (`text`) | `slugify`, `caseConverter` (camelCase, kebabCase, lowerCase, pascalCase, snakeCase, upperCase), `urlEncode`, `urlDecode` |
| **Calculator** (`calculator`) | `ctcToInHand` |
| **E-commerce** (`ecommerce`) | `catalogMapper`, `upiQr`, `gstJsonToTable`, `profitCalculator`, `shippingLabelCrop`, `webhookVerifier`, `whatsappPayload` |

Full parameters and real outputs: [Operations Reference](https://docs.devdeskapp.com/n8n/operations).

---

## ⚡ Quick node installation

### In the n8n UI
1. **Settings** → **Community Nodes** → **Install**.
2. Enter `n8n-nodes-devdeskapp`.
3. Tick the risk acknowledgement and click **Install**.

### Manually (self-hosted)
```bash
mkdir -p ~/.n8n/nodes && cd ~/.n8n/nodes
npm install n8n-nodes-devdeskapp
# then restart n8n
```

---

## 🛠️ Working on these docs

```bash
npm install
npm run docs:dev      # local preview at http://localhost:5173
npm run docs:build    # production build into .vitepress/dist
```

Figures in `src/public/images/fig-*.png` are generated with the DevDeskApp light palette:

```bash
python -I scripts/doc-images/generate.py            # all figures
python -I scripts/doc-images/generate.py node-prettify ctc-output   # selected figures
```

The generator needs Python, Playwright and a local Chrome install. Source screenshots for the framed figures are in `scripts/doc-images/raw/`.

---

## 🤖 Machine-readable endpoints

- **LLMs index**: [`https://docs.devdeskapp.com/llms.txt`](https://docs.devdeskapp.com/llms.txt)
- **Full context**: [`https://docs.devdeskapp.com/llms-full.txt`](https://docs.devdeskapp.com/llms-full.txt)

---

## 🔗 Links

- **Documentation**: [https://docs.devdeskapp.com](https://docs.devdeskapp.com)
- **Web platform**: [https://www.devdeskapp.com](https://www.devdeskapp.com)
- **npm package**: [https://www.npmjs.com/package/n8n-nodes-devdeskapp](https://www.npmjs.com/package/n8n-nodes-devdeskapp)
- **Node source code**: [https://github.com/DevdeskApp/n8n-nodes-devdeskapp](https://github.com/DevdeskApp/n8n-nodes-devdeskapp)

---

## 📄 License

Distributed under the **MIT License**. See [LICENSE](LICENSE).
