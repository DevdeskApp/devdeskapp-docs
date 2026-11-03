---
title: 'Template #21593: AI LLM JSON Ingestion'
description: 'n8n template #21593: sanitize raw AI LLM responses, strip markdown backticks, compute SHA-256 audit digests, and ingest into PostgreSQL with Slack notifications.'
---

# 🤖 Template #21593: Sanitize & Ingest AI LLM JSON into Postgres with DevDeskApp and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io Creator Portal</span>
  <span class="badge-live" style="background: rgba(99, 102, 241, 0.12); color: #6366f1; border-color: rgba(99, 102, 241, 0.3);">Template ID: 21593</span>
</div>

🔗 **Direct n8n Template Link:**  
[https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/)

<div class="doc-image">
  <img src="/images/screen_ai_llm_canvas.png" alt="AI LLM Ingestion Canvas" />
</div>
<div class="doc-caption">Figure 1: Full AI LLM JSON ingestion and sanitation pipeline in n8n.</div>

---

## 🎯 Overview & Use Cases

Large Language Models (OpenAI GPT-4, Anthropic Claude, Google Gemini, Ollama, DeepSeek) are increasingly used to generate structured JSON payloads. However, in production pipelines, LLMs introduce several critical failure modes:

1. **Markdown Code Fence Pollution:** LLMs frequently wrap JSON output in markdown backticks (e.g., ```` ```json ... ``` ````) or include conversational preambles/postambles that break downstream native JSON parsers and SQL statements.
2. **Missing Distributed Correlation:** Without an RFC 4122 UUID injected at ingestion, tracking multi-agent or asynchronous AI calls across PostgreSQL and Slack is impossible.
3. **Data Integrity & Non-Repudiation:** Generative AI responses must be cryptographically hashed (SHA-256) to ensure tamper-proof audit trails for compliance and billing validation.
4. **Unformatted Slugs:** AI categories, topics, or customer usernames need URL-safe normalization before database indexing.

**Template #21593** acts as an enterprise-grade ingestion gateway. It intercepts raw AI completions, strips markdown fences, validates and prettifies JSON, calculates cryptographic SHA-256 digests and UUID v4 trace tokens, normalizes taxonomy slugs, and inserts clean structured records directly into PostgreSQL with automated Slack alerts.

---

## 📸 Workflow Architecture

### Pipeline Sequence

```mermaid
flowchart TD
    subgraph TriggerStage ["📥 Stage 1: Trigger & LLM Completion"]
        T1["⚡ Webhook / Manual Event"]
        AI["🤖 LLM Model Output (Raw Text with Markdown ```json fences)"]
        T1 --> AI
    end

    subgraph DevDeskStage ["🛡️ Stage 2: DevDeskApp In-Memory Processing (<0.2ms)"]
        direction TB
        N1["1️⃣ JSON Prettifier & Schema Validator
Cleans markdown fences, unescapes characters & formats JSON"]
        N2["2️⃣ SHA-256 Cryptographic Hasher
Generates audit digest of raw AI prompt & completion"]
        N3["3️⃣ RFC UUID v4 Generator
Injects distributed trace & incident correlation ID"]
        N4["4️⃣ Slugifier
Creates URL-safe category & document index slug"]
        N1 --> N2 --> N3 --> N4
    end

    subgraph ValidationStage ["⚖️ Stage 3: Integrity Validation"]
        Gate{"Payload Valid & Schema Conforms?"}
    end

    subgraph IngestStage ["🗄️ Stage 4: Database Storage & Team Alerts"]
        PG["🐘 PostgreSQL Ingest
INSERT INTO ai_generations (...)"]
        Slack["💬 Slack Channel Dispatch
#ai-operations (Clean Status Notification)"]
        PG --> Slack
    end

    TriggerStage --> DevDeskStage
    DevDeskStage --> ValidationStage
    ValidationStage -->|Valid| IngestStage
    ValidationStage -->|Invalid| SlackErr["🚨 Slack Alert: Malformed AI Payload"]
```

---

## ⚙️ Key Operations Used

| Operation | DevDeskApp Function | Purpose |
| :--- | :--- | :--- |
| **JSON Prettifier** | `formatJson` | Strips outer markdown wrappers (` ```json `), validates syntax, and produces normalized JSON. |
| **SHA-256 Digest** | `generateHash` | Timing-safe cryptographic SHA-256 hash guaranteeing payload integrity and non-repudiation. |
| **UUID v4 Trace** | `generateUuid` | Injects an RFC 4122 v4 unique ID to link database rows with audit logs and Slack alerts. |
| **Slugifier** | `slugify` | Transforms model topics and category names into normalized lowercase URL-friendly strings. |

---

## ⚡ Real-Time Execution Result

### Sample Input (Raw LLM Output)

```text
Here is your generated analysis:
```json
{
  "topic": "Automated Cloud FinOps 2026",
  "confidenceScore": 0.984,
  "recommendations": [
    "Scale idle compute nodes during off-peak hours",
    "Consolidate external API gateways to local memory tools"
  ],
  "author": "Autonomous Agent Alpha"
}
```
Please let me know if you need any adjustments!
```

### Clean Normalized Output Sample

```json
{
  "traceId": "c479e390-d8fa-4e78-9844-46b0a1a09d31",
  "payloadHash": "7f83b1657ff1fc53b92dc18148a1d65dfc2d4b1fa3d677284addd200126d9069",
  "topicSlug": "automated-cloud-finops-2026",
  "parsedData": {
    "topic": "Automated Cloud FinOps 2026",
    "confidenceScore": 0.984,
    "recommendations": [
      "Scale idle compute nodes during off-peak hours",
      "Consolidate external API gateways to local memory tools"
    ],
    "author": "Autonomous Agent Alpha"
  },
  "ingestedAt": "2026-11-04T00:30:00.000Z",
  "dbStatus": "SUCCESS"
}
```

---

## 📥 How to Import into Your n8n Instance

1. Open the [n8n Creator Portal page](https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/) and copy the template JSON or click **"Use workflow"**.
2. In your n8n workspace, navigate to **Workflows → New Workflow**.
3. Press **`Ctrl + V`** (or **`Cmd + V`** on macOS) inside the workflow canvas.
4. Configure your **PostgreSQL** credentials and **Slack** webhook URL.
5. Save and trigger the workflow!
