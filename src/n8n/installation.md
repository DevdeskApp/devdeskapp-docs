---
title: 'Install the DevDeskApp n8n Node'
description: 'Install n8n-nodes-devdeskapp step by step from the n8n Community nodes panel, or manually with npm on self-hosted and Docker n8n instances.'
---
# Step-by-Step Installation Guide

You can install `n8n-nodes-devdeskapp` from n8n's **Community nodes** settings page or manually with npm.

**Latest release:** <NodeVersion /> ([all versions on npm](https://www.npmjs.com/package/n8n-nodes-devdeskapp?activeTab=versions)). Installing without a version number always gets the latest one.

::: tip Who can install
Installing from the UI needs an instance owner or admin account, and community nodes must be enabled on the instance. They are enabled by default on self-hosted n8n.
:::

---

## Option 1: Install from the n8n UI (recommended)

### Step 1: Open Community nodes
1. Open your n8n editor.
2. Go to **Settings**.
3. Select **Community nodes** in the settings menu.

<div class="doc-image">
  <img src="/images/fig-n8n-community-nodes.png" alt="Community nodes page in n8n settings" />
</div>
<div class="doc-caption">Figure 1: Settings &gt; Community nodes, with the <strong>Install a community node</strong> button.</div>

### Step 2: Enter the package name
1. Click **Install a community node**.
2. In **npm Package Name**, enter:
   ```text
   n8n-nodes-devdeskapp
   ```
3. Tick the confirmation *"I understand the risks of installing unverified code from a public source."*
4. Click **Install**.

<div class="doc-image">
  <img src="/images/fig-n8n-install-modal.png" alt="Install community nodes dialog with n8n-nodes-devdeskapp entered" />
</div>
<div class="doc-caption">Figure 2: The install dialog with the package name and the risk confirmation.</div>

### Step 3: Check that it is installed
1. Open any workflow and press `Tab` (or click **+**) to open the nodes panel.
2. Search for `DevDeskApp`.
3. Add the node and pick a **Resource** and an **Operation**.

---

## Option 2: Docker and Docker Compose

Community packages are enabled by default. If your instance disables them, set `N8N_COMMUNITY_PACKAGES_ENABLED=true`. Keep `/home/node/.n8n` on a volume so installed packages survive container restarts:

```yaml
services:
  n8n:
    image: docker.n8n.io/n8nio/n8n:latest
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_COMMUNITY_PACKAGES_ENABLED=true
    volumes:
      - n8n_data:/home/node/.n8n

volumes:
  n8n_data:
```

Then install from the UI (Option 1), or manually inside the container:

```bash
docker exec -it <n8n-container> sh
mkdir -p ~/.n8n/nodes && cd ~/.n8n/nodes
npm install n8n-nodes-devdeskapp
exit
docker restart <n8n-container>
```

::: warning Queue mode
In queue mode every worker executes nodes, so every worker needs the package. Install it on the shared `.n8n` volume or on each worker, then restart them.
:::

::: tip Using the node as an AI Agent tool
On self-hosted n8n, community nodes appear on an AI Agent's **Tool** port only if you set `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true`, for example under `environment:` in the compose file above. See [AI Agents & LLMs](/solutions/ai-agents).
:::

---

## Option 3: Self-hosted n8n with npm

If you run n8n directly with Node.js, install the package into n8n's `nodes` folder (the default is `~/.n8n/nodes`), then restart n8n:

```bash
mkdir -p ~/.n8n/nodes
cd ~/.n8n/nodes
npm install n8n-nodes-devdeskapp

# restart n8n so it loads the new node
n8n start
```

To update later, run `npm update n8n-nodes-devdeskapp` in the same folder and restart, or use **Settings → Community nodes → Update**.

---

## 🔍 First test

1. Add a **DevDeskApp** node after a **Manual Trigger**.
2. Set **Resource** to **JSON Utility** and **Operation** to **Prettify / Format**.
3. Set **JSON Input** to `{"status":"ok","code":200}`.
4. Click **Execute step**. The output item contains a `formatted` string and `"success": true`.

<div class="doc-image">
  <img src="/images/fig-node-prettify.png" alt="DevDeskApp first test step: JSON Utility Prettify input, parameters and output" />
</div>
<div class="doc-caption">Figure 3: The first test step and its real output.</div>
