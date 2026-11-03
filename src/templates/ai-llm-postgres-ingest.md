---
title: 'Template #21593: AI LLM JSON Ingestion'
description: 'n8n template #21593: strip markdown fences from LLM output, format and fingerprint the JSON with DevDeskApp, add a UUID trace ID, and insert clean records into PostgreSQL with Slack alerts.'
---

# 🤖 Template #21593: Sanitize & Ingest AI LLM JSON into Postgres with DevDeskApp and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-indigo">Template ID: 21593</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21593](https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-21593.png" alt="Template 21593 AI LLM JSON ingestion workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

LLMs often wrap JSON in markdown fences (`` ```json … ``` ``), which breaks `JSON.parse` and SQL inserts. This template is an ingestion gateway for model output:

1. A **Code node** strips the markdown fences from `rawResponse`.
2. The **DevDeskApp JSON Prettifier** parses and formats the cleaned string. Invalid JSON stops here with a clear error.
3. **DevDeskApp UUID** adds a trace ID that links the database row, logs and Slack.
4. **DevDeskApp SHA-256** fingerprints the formatted JSON for deduplication and audit.
5. An **If** node sends valid records to **PostgreSQL** plus a Slack log, and malformed ones to a Slack alert.

::: danger Known issue in the published version (checked 4 Nov 2026)
Running the published template end to end shows three problems. Fix them after import:
1. **Sample node fails to run.** `Sample Raw LLM Output (With Markdown)` writes the response with four backticks (` ```` `), which is a JavaScript syntax error. Change it to a normal string, for example `rawResponse: "```json\n{ ... }\n```"`.
2. **The hash covers an empty string.** `SHA-256 Integrity Hasher` reads `{{ $json.prettified }}`, but the prettifier outputs `formatted`, and the previous node is the UUID generator. Use `{{ $('DevDeskApp: JSON Prettifier & Schema Validator').item.json.formatted }}`.
3. **The Postgres branch crashes.** `Format Clean Database Record` calls `JSON.parse(prettified.prettified)`. Change both `prettified.prettified` to `prettified.formatted`.

With these three changes the workflow runs through to the Postgres insert and Slack log.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21593.png" alt="Template 21593 pipeline: ingest, strip fences, three DevDeskApp nodes, If gate, Postgres and Slack branches" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| Strip Markdown Code Fences | Code node | Removes leading `` ```json `` and trailing `` ``` `` |
| DevDeskApp: JSON Prettifier & Schema Validator | `json` · `prettify` | Parses and formats `cleanedJsonString`. Throws on invalid JSON. |
| DevDeskApp: Trace UUID Generator | `crypto` · `uuid` | Trace ID |
| DevDeskApp: SHA-256 Integrity Hasher | `crypto` · `hash` (`sha256`) | Fingerprint of the formatted JSON |
| If: Valid JSON & Clean Schema | `if` | Routes to Postgres or to the error alert |

The DevDeskApp node does not remove markdown fences itself. That is the Code node's job, and the node then parses and formats the result.

---

## ⚡ Execution sample (with the fixes above)

**Input** (`rawResponse` from the sample node):

````text
```json
{
  "customer_id": "cust_88291",
  "sentiment": "positive",
  "confidence_score": 0.94,
  "intent": "upsell_enterprise",
  "extracted_topics": ["security_compliance", "sso", "audit_logs"],
  "action_required": true
}
```
````

**Output** of `Format Clean Database Record`:

```json
{
  "traceId": "110ae286-1a41-46ec-9142-ec2a2b8f22c5",
  "sha256Checksum": "07df809dca91e8094d9a16a331dd03b97e1aea4ce54b8166bd1a15fa446d9d59",
  "model": "gpt-4o",
  "parsedData": {
    "customer_id": "cust_88291",
    "sentiment": "positive",
    "confidence_score": 0.94,
    "intent": "upsell_enterprise",
    "extracted_topics": ["security_compliance", "sso", "audit_logs"],
    "action_required": true
  },
  "sqlInsertQuery": "INSERT INTO ai_agent_records (trace_id, model, payload, checksum) VALUES (...)"
}
```

::: warning Use query parameters in production
The sample builds `sqlInsertQuery` by string concatenation. For real data, use the Postgres node's **Insert** operation or query parameters instead of running that string.
:::

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21593-sanitize-and-ingest-ai-llm-json-into-postgres-with-devdeskapp-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Apply the three fixes from the known-issue box above.
5. Add your **PostgreSQL** and **Slack** credentials, create the `ai_agent_records` table, and click **Test workflow**.
