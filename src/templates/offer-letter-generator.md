---
title: 'Template #21594: Indian CTC Offer Letter Generator'
description: 'n8n template #21594: estimate in-hand salary, PF and PT from annual CTC with DevDeskApp, create a Google Docs offer letter, email it with Gmail and alert HR on Slack.'
---

# 📄 Template #21594: Generate Indian CTC Offer Letters with DevDeskApp, Google Docs, Gmail and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-green">Template ID: 21594</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21594](https://n8n.io/workflows/21594-generate-indian-ctc-offer-letters-with-devdeskapp-google-docs-gmail-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-21594.png" alt="Template 21594 CTC offer letter workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

Drafting offer letters by hand is slow, and compensation figures copied from spreadsheets drift. This template takes a candidate row (from the sample node or a **Google Sheets trigger**) and:

1. **Estimates pay** with DevDeskApp **CTC to In-Hand Salary**: monthly gross, basic, employee and employer PF, PT, TDS and in-hand.
2. **Creates an offer token** (UUID v4) and a **candidate slug** such as `ananya-roy-principal-devops-engineer`.
3. **Fingerprints the compensation** with SHA-256, so the figures in the letter can be checked later.
4. Checks the offer with an **If** node, then fills a **Google Docs** template, emails it with **Gmail** and posts to HR **Slack**. Invalid offers go to a compliance alert instead.

::: danger Known issue in the published version (checked 4 Nov 2026)
In `Format Offer Letter Document Payload`, three fields read top-level keys that the DevDeskApp node does not return, so the letter shows **₹0** for basic salary, PF and professional tax. Change:
- `salary.basicSalary` → `salary.breakdown.monthlyBasic`
- `salary.employeePf` → `salary.breakdown.employeePf`
- `salary.professionalTax` → `salary.breakdown.professionalTax`

Monthly gross, in-hand and CTC are already correct.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21594.png" alt="Template 21594 pipeline: ingest, four DevDeskApp nodes, If gate, Google Docs, Gmail and Slack branch" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| DevDeskApp: Indian CTC-to-In-Hand Engine | `calculator` · `ctcToInHand` | `annualCtc`, `basicPercentage` (default 50) |
| DevDeskApp: Offer Tracking UUID | `crypto` · `uuid` | Offer token |
| DevDeskApp: Candidate Slug Generator | `text` · `slugify` | `name-role` slug for file names |
| DevDeskApp: Compensation Checksum Hasher | `crypto` · `hash` (`sha256`) | Hash of the full salary output |
| If: Compensation Valid & Above Minimum Threshold | `if` | Valid offers go to Docs, Gmail and Slack, the rest to an HR alert |

---

## ⚡ Execution sample (with the fix above)

**Input** (sample candidate):

```json
{
  "candidateName": "Ananya Roy",
  "roleTitle": "Principal DevOps Engineer",
  "annualCtc": 2100000,
  "basicPercentage": 50,
  "joiningDate": "2026-12-01"
}
```

**DevDeskApp CTC output:** `monthlyGross: 173200`, `monthlyInHand: 145575`, `breakdown.monthlyBasic: 87500`, `employeePf: 1800`, `professionalTax: 200`, `estimatedMonthlyTds: 25625`.

**`Format Offer Letter Document Payload` output:**

```json
{
  "offerId": "83aaa78d-e801-4c0a-ab00-2621a1422747",
  "trackingSlug": "ananya-roy-principal-devops-engineer",
  "integrityChecksum": "575b5e91708c83e62caf29cc5e6a7fee1cfd0d5354faa7befc06dbcbb9a41293",
  "compensationBreakdown": {
    "annualCtcFormatted": "₹21,00,000",
    "monthlyGrossFormatted": "₹1,73,200",
    "basicSalaryFormatted": "₹87,500",
    "employeePfFormatted": "₹1,800",
    "professionalTaxFormatted": "₹200",
    "monthlyInHandFormatted": "₹1,45,575"
  }
}
```

PF follows the node's rule (12% of basic, capped at ₹1,800), so a ₹21L CTC shows ₹1,800, not 12% of the full basic.

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21594-generate-indian-ctc-offer-letters-with-devdeskapp-google-docs-gmail-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Apply the fix from the known-issue box, then connect **Google Docs**, **Gmail**, **Google Sheets** and **Slack** credentials.
5. Point the Google Docs node at your offer-letter template and click **Test workflow**.
