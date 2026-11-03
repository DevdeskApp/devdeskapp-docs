---
title: 'Template #21017: Developer Suite'
description: 'n8n template #21017: format JSON, compute a SHA-256 digest, add a UUID v4 trace ID, build a slug and estimate CTC take-home with n8n-nodes-devdeskapp.'
---

# 🌟 Template #21017: Developer Suite & Security Engine

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-indigo">Template ID: 21017</span>
  <span class="badge-live badge-blue">No credentials needed</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21017](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/)

<div class="doc-image">
  <img src="/images/fig-canvas-21017.png" alt="Template 21017 Developer Suite workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas, with its sticky notes.</div>

---

## 🎯 Overview

This workflow shows five DevDeskApp operations chained on one sample payload, with no Code-node logic for the transformations and no external APIs:

1. **JSON Prettifier** formats the minified `rawMinifiedApiData` string.
2. **SHA-256 Digest** hashes the formatted JSON.
3. **UUID Generator** adds an RFC 4122 v4 trace ID.
4. **Slugifier** turns the candidate name into a URL-safe slug.
5. **CTC Calculator** estimates monthly take-home pay from the annual CTC.

A final Code node merges the five results into one item. It needs no credentials, so you can run it right after import.

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21017.png" alt="Template 21017 pipeline: manual trigger, sample payload, five DevDeskApp operations, consolidated output" />
</div>
<div class="doc-caption">Figure 2: Node order in the published template.</div>

| Node | Resource · Operation | Key parameter |
| :--- | :--- | :--- |
| DevDeskApp: JSON Prettifier | `json` · `prettify` | `jsonInput = {{ $json.rawMinifiedApiData }}`, 2 spaces |
| DevDeskApp: SHA-256 Digest | `crypto` · `hash` | `textPayload = {{ $json.formatted }}`, `sha256` |
| DevDeskApp: UUID Generator | `crypto` · `uuid` | none |
| DevDeskApp: Slugifier | `text` · `slugify` | `textInput = candidateFullName` from the sample node |
| DevDeskApp: CTC Calculator | `calculator` · `ctcToInHand` | `annualCtc` and `basicPercentage` from the sample node |

---

## ⚡ Execution result

One test run executes all eight nodes with one item each:

<div class="doc-image">
  <img src="/images/fig-suite-executed.png" alt="Template 21017 after a test run: all eight nodes succeeded with their key outputs" />
</div>
<div class="doc-caption">Figure 3: Every node after a test run, with the value each DevDeskApp node returned.</div>

<div class="doc-image">
  <img src="/images/fig-suite-output.png" alt="Consolidated Final Output item of template 21017" />
</div>
<div class="doc-caption">Figure 4: The item produced by <strong>Consolidated Final Output</strong>.</div>

### Consolidated output (from a real run)

The sample payload uses `annualCtc: 2400000` and `basicPercentage: 50`. The `traceId` changes on every run.

```json
{
  "meta": {
    "traceId": "5ad52af6-8b62-48a0-b934-7a82c4ab3eb1",
    "sha256PayloadHash": "f7e61312d64a6fefb8ff2dcc4ccc957e7204a229c04647fffba674aed41620df",
    "candidateFileSlug": "rahul-verma-principal-cloud-architect",
    "status": "VERIFIED_AND_PROCESSED"
  },
  "compensationBreakdown": {
    "annualCtcFormatted": "₹24,00,000",
    "monthlyGross": "₹1,98,200",
    "netMonthlyTakeHome": "₹1,63,075",
    "taxDeductions": {
      "monthlyBasic": "₹1,00,000",
      "employeePf": "₹1,800",
      "estimatedMonthlyTax": "₹33,125",
      "professionalTax": "₹200"
    }
  }
}
```

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities/) and click **Use for free**, or copy the workflow JSON.
3. In n8n, create a new workflow, click the canvas and press **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Click **Test workflow**.
