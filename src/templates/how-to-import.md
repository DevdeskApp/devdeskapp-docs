---
title: 'How to Import n8n Templates'
description: 'Import official DevDeskApp templates into n8n Cloud, self-hosted n8n or Docker by pasting the workflow JSON onto the canvas, step by step.'
---

# ⚡ How to Import Templates into n8n

Every workflow template built with **`n8n-nodes-devdeskapp`** can be imported directly into any n8n environment in seconds.

---

## Prerequisites

Before importing, ensure your n8n workspace has **`n8n-nodes-devdeskapp`** installed:

1. In your n8n web app, open **Settings → Community Nodes**.
2. Click **Install**.
3. Enter `n8n-nodes-devdeskapp` and confirm.
4. If running via Docker, make sure `N8N_COMMUNITY_PACKAGES_ENABLED=true` is set.  
   *(See the complete [Installation Guide](/n8n/installation) for details)*.

---

## 3-Step Import Method (Clipboard Copy / Paste)

This is the fastest method and works on all n8n instances (Self-Hosted, Cloud, Desktop, and Docker):

### Step 1: Open Template on n8n Creator Portal
Navigate to either of our official templates:
- **[Template #21017: Developer Suite & Security Engine](https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities)**
- **[Template #21130: CTC to In-Hand Salary Engine](https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp)**

Click the **"Copy workflow to clipboard"** or **"Use workflow"** button.

### Step 2: Open Your n8n Canvas
In your n8n workspace:
1. Click **+ New Workflow** in the sidebar.
2. Click once on the canvas grid background to focus the window.

### Step 3: Paste (`Ctrl + V`)
Press **`Ctrl + V`** (Windows / Linux) or **`Cmd + V`** (macOS).

The complete workflow with all pre-configured nodes, sticky notes, and wiring will immediately appear on your screen!

---

## Troubleshooting Common Issues

### "Unknown Node: devdeskapp"
- **Cause:** The `n8n-nodes-devdeskapp` package is not installed or the n8n container needs a quick restart.
- **Fix:** Install `n8n-nodes-devdeskapp` via **Settings → Community Nodes** and reload the page.

### Canvas did not register paste
- **Cause:** Canvas window was not focused before pressing `Ctrl+V`.
- **Fix:** Click anywhere on the dotted grid background and press `Ctrl+V` again.
