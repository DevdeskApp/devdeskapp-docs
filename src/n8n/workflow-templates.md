---
title: Official Workflow Templates | DevDeskApp
description: Production-ready, verified n8n workflow blueprints powered by n8n-nodes-devdeskapp. Copy, paste, and automate developer utilities, security hashing, and payroll calculations.
---

# Official Workflow Templates

Discover and copy production-ready n8n workflows built with `n8n-nodes-devdeskapp`. You can copy the workflow JSON snippets below and paste them directly into your n8n canvas using `Ctrl+V` (or `Cmd+V`).

<div class="official-template-card">
  <div class="template-card-left">
    <div class="template-card-header">
      <span class="template-badge">New Hub</span>
      <span class="badge-live">Dedicated Templates Portal</span>
    </div>
    <h3 class="template-card-title">Explore the Dedicated Templates Hub</h3>
    <p class="template-card-desc">
      We have launched a dedicated <strong>Templates Catalog</strong> featuring individual blueprints, architectural diagrams, parameter guides, and 1-click import instructions.
    </p>
  </div>
  <a href="/templates/" class="template-card-cta">
    <span>Browse All Templates</span>
    <span>→</span>
  </a>
</div>

---

## Template 1: Flagship Developer Suite & Security Engine (Template #21017)

<div style="margin: 1rem 0;">
  <span class="badge-live">Published on n8n.io Creator Portal</span>
  <span class="badge-live" style="margin-left: 8px;">Template ID: 21017</span>
</div>

🔗 **Direct n8n Template Link:**  
[n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities)

📖 **Detailed Documentation & Blueprint:**  
[Read the Full Blueprint Guide →](/templates/developer-suite)

### Workflow Architecture
This workflow runs on a manual trigger or incoming webhook and performs 5 essential developer operations sequentially:
1. **Sample Developer & HR Payload:** Mock payload with minified JSON and candidate profile.
2. **DevDeskApp Prettifier:** Re-formats raw JSON into an indented, human-readable structure.
3. **DevDeskApp SHA-256 Digest:** Generates cryptographic tamper-proof digest.
4. **DevDeskApp UUID Generator:** Stamps every request with an RFC 4122 v4 trace ID.
5. **DevDeskApp Slugifier:** Cleans full names and titles into URL-safe slug identifiers.
6. **DevDeskApp CTC Calculator:** Computes monthly take-home, employee/employer PF, PT, and tax breakdown.
7. **Consolidated Output:** Assembles clean, validated JSON output ready for databases or downstream microservices.

<div class="doc-image">
  <img src="/images/screen_2_workflow_canvas.png" alt="Developer Suite Canvas" />
</div>
<div class="doc-caption">Figure 1: Complete automation pipeline with sticky notes and configured node parameters.</div>

### 1-Click Execution Result
When executed, every step finishes in sub-millisecond CPU time:

<div class="doc-image">
  <img src="/images/template_test_result.png" alt="Template Test Result Execution" />
</div>
<div class="doc-caption">Figure 2: Execution trace showing instantaneous transformation across all 5 DevDeskApp operations.</div>

---

## Template 2: Employee CTC to In-Hand Salary Engine (Template #21130)

<div style="margin: 1rem 0;">
  <span class="badge-live">Published on n8n.io Creator Portal</span>
  <span class="badge-live" style="margin-left: 8px; background: rgba(16, 185, 129, 0.12); color: #10b981; border-color: rgba(16, 185, 129, 0.3);">Template ID: 21130</span>
</div>

🔗 **Direct n8n Template Link:**  
[n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp](https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp)

📖 **Detailed Documentation & Blueprint:**  
[Read the Full Blueprint Guide →](/templates/ctc-salary-engine)

Designed for HR, Payroll, and Recruiting operations to automate salary computation from raw offer letter inputs:

<div class="doc-image">
  <img src="/images/screen_ctc_canvas.png" alt="CTC Calculator Canvas" />
</div>
<div class="doc-caption">Figure 3: Automated CTC evaluation flow in n8n.</div>

### Parameter Drawer & Indian Payroll Rules
- Input annual CTC (e.g. ₹2,400,000).
- Configurable basic salary percentage (default: 50%).
- Automatic statutory calculation for Employee PF, Employer PF, Professional Tax (PT), and estimated monthly in-hand take-home salary.

<div class="doc-image">
  <img src="/images/screen_ctc_drawer.png" alt="CTC Parameter Drawer" />
</div>
<div class="doc-caption">Figure 4: Inputting annual compensation parameters in DevDeskApp node drawer.</div>

### Real-Time Breakdown Output

<div class="doc-image">
  <img src="/images/screen_ctc_executed.png" alt="CTC Execution Output" />
</div>
<div class="doc-caption">Figure 5: Complete salary breakdown returned in structured JSON format.</div>

```json
{
  "annualCtc": 2400000,
  "monthlyGross": 200000,
  "monthlyInHand": 145000,
  "breakdown": {
    "basic": 100000,
    "hra": 50000,
    "specialAllowance": 34600,
    "employeePf": 12000,
    "employerPf": 12000,
    "professionalTax": 200,
    "estimatedTaxMonthly": 40200
  }
}
```

---

## How to Import Templates into Your n8n

1. Copy the JSON structure of any template or click the direct n8n.io link.
2. In your n8n editor window, click anywhere on the canvas grid.
3. Press `Ctrl + V` (or `Cmd + V` on macOS).
4. The workflow will appear instantly with all connections and pre-set parameters!  
   *(See the complete [Import Guide](/templates/how-to-import) for details)*.
