---
title: 'Template #22361: GitHub PR Mermaid Architecture Diagrams'
description: 'n8n template #22361: extract Mermaid architecture diagrams and schemas from GitHub PRs, encode SVG previews, compute SHA-256 drift hashes, and sync to Slack and Notion.'
---

# 🏗️ Template #22361: Sync GitHub PR Architecture Diagrams with DevDeskApp, Slack and Notion

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-indigo">Template ID: 22361</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/22361](https://n8n.io/workflows/22361-sync-github-pr-architecture-diagrams-with-devdeskapp-slack-and-notion/)

<div class="doc-image">
  <img src="/images/fig-canvas-22361.png" alt="Template 22361 GitHub PR Mermaid architecture diagram sync workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

Code reviewers frequently struggle to visualize database migrations, system workflows, and service interactions from raw git code diffs. Furthermore, software teams often forget to update architectural documentation in Notion wikis when merging pull requests.

This template automates continuous architecture reviews on every Pull Request:

1. **Intakes GitHub PR Events**: Triggers on pull request submissions or schema file changes (`schema.prisma`, `migrations.sql`, or `.mermaid` definitions).
2. **In-Memory Base64 & Slug Encoding**: Encodes raw Mermaid diagram definitions into URL-safe strings for real-time SVG rendering with DevDeskApp **Base64 Converter** and **Slugify String**.
3. **Cryptographic Schema Fingerprinting**: Computes a **SHA-256 hash** of the schema to detect architectural drift and generates a **UUID v4** execution audit token.
4. **Multi-Channel Architecture Sync**: Posts visual diagram previews directly into engineering **Slack** channels and updates the **Notion** architecture documentation wiki.

::: tip Deterministic In-Memory Processing
All Base64 encoding, SHA-256 schema hashing, and slugification execute 100% in-memory within `n8n-nodes-devdeskapp`. Your proprietary codebase schemas and PR diffs never touch external third-party API converters.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-22361.png" alt="Template 22361 pipeline: GitHub PR trigger, DevDeskApp converter and crypto nodes, validation gate, Slack and Notion branches" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| GitHub PR Trigger / Manual Test | `trigger` · `manualTrigger` / `github` | Ingests new PR event containing schema or system diffs |
| DevDeskApp: Base64 Encoder | `converters` · `base64` | Encodes raw Mermaid definitions into safe data strings for SVG preview |
| DevDeskApp: SHA-256 Hasher | `crypto` · `hash` (`sha256`) | Checksum of the schema to detect drift between branches |
| DevDeskApp: Trace UUID Generator | `crypto` · `uuid` | RFC 4122 v4 unique audit identifier for CI/CD tracking |
| DevDeskApp: PR Slugifier | `text` · `slugify` | Builds a clean URL slug from PR title and branch name |
| If: Valid Architecture PR | `if` | Verifies non-empty schema and validates diagram syntax |
| Slack: Architecture Alert | Slack node | Sends rich Slack blocks with rendered diagram link to engineers |
| Notion: Architecture Hub | Notion node | Appends visual architecture diagrams to team engineering documentation |

---

## ⚡ Execution sample

```json
{
  "status": "ARCHITECTURE_SYNCED",
  "auditToken": "9b1deb4d-3b7d-4bad-9bdd-2b0d7b3dcb6d",
  "prNumber": 142,
  "repository": "DevdeskApp/enterprise-core",
  "prSlug": "pr-142-feat-distributed-order-state-machine",
  "schemaFingerprint": {
    "algorithm": "sha256",
    "hash": "7a3b8c9d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2b3c4d5e6f7a8b"
  },
  "mermaid": {
    "type": "stateDiagram-v2",
    "base64Encoded": "c3RhdGVEaWFncmFtLXYyCiAgICBbKl0gLS0+IFBlbmRpbmcKICAgIFBlbmRpbmcgLS0+IFByb2Nlc3NpbmcKICAgIFByb2Nlc3NpbmcgLS0+IENvbXBsZXRlZAo=",
    "previewUrl": "https://mermaid.ink/svg/c3RhdGVEaWFncmFtLXYyCiAgICBbKl0gLS0+IFBlbmRpbmcKICAgIFBlbmRpbmcgLS0+IFByb2Nlc3NpbmcKICAgIFByb2Nlc3NpbmcgLS0+IENvbXBsZXRlZAo="
  },
  "channelsUpdated": [
    "#engineering-architecture",
    "Notion: System Architecture Wiki"
  ]
}
```

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/22361-sync-github-pr-architecture-diagrams-with-devdeskapp-slack-and-notion/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Configure your **GitHub App / Personal Access Token** in the GitHub Trigger node.
5. Connect **Slack** and **Notion** credentials, then click **Test workflow**.
