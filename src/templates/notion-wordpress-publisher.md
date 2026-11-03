---
title: 'Template #21596: Notion to WordPress SEO Publisher'
description: 'n8n template #21596: build clean SEO slugs with DevDeskApp, fingerprint article content with SHA-256, add a UUID trace ID and publish approved Notion posts to WordPress with Slack alerts.'
---

# 📝 Template #21596: Publish SEO-Safe Notion Blog Posts to WordPress with DevDeskApp and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-pink">Template ID: 21596</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/21596](https://n8n.io/workflows/21596-publish-seo-safe-notion-blog-posts-to-wordpress-with-devdeskapp-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-21596.png" alt="Template 21596 Notion to WordPress workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

Content teams write in Notion and publish on WordPress. Copying by hand produces messy permalinks and no record of which version went live. This template:

1. Turns the article title into a **clean SEO slug** with DevDeskApp **Slugify String**. For example, *"Top 10 High-Throughput Microservice Architecture Patterns in 2027"* becomes `top-10-high-throughput-microservice-architecture-patterns-in-2027`.
2. Computes a **SHA-256 fingerprint** of the article HTML, so you can tell whether the content changed between versions.
3. Adds a **UUID v4 publication ID** to the JSON-LD and audit data.
4. Checks the editorial status with an **If** node, then creates or updates the post through the **WordPress** node and announces it on **Slack**. Drafts trigger an editorial warning instead.

::: danger Known issue in the published version (checked 4 Nov 2026)
Running the published template end to end shows two problems:
1. **The content hash covers an empty string.** `Content Fingerprint Hasher` reads `{{ $json.rawHtmlContent }}`, but its input is the slug node's output. Use `{{ $('Sample Notion Article Draft').item.json.rawHtmlContent }}`, or your Notion trigger node's name.
2. **The post title is empty.** `Meta Title Casing Formatter` uses Target Case `title`, which the node does not support (it returns an empty `result`), and the WordPress code reads `titleData.convertedText`, which does not exist. Either delete that node and use `article.articleTitle` in `Format WordPress Post Payload`, or pick a supported case and read `titleData.result`.
:::

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-21596.png" alt="Template 21596 pipeline: ingest, four DevDeskApp nodes, approval gate, WordPress and Slack" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| DevDeskApp: URL Slug Normalizer | `text` · `slugify` | WordPress `slug` |
| DevDeskApp: Content Fingerprint Hasher | `crypto` · `hash` (`sha256`) | Version digest of the article HTML |
| DevDeskApp: Publication Trace UUID | `crypto` · `uuid` | Publication ID in JSON-LD and audit data |
| DevDeskApp: Meta Title Casing Formatter | `text` · `caseConverter` | See the known issue. There is no Title Case option. |
| If: Article Approved & Ready for Publication | `if` | Publishes approved posts only |
| WordPress: Create / Update Blog Post | WordPress node | Creates the post with title, slug, content and categories |

---

## ⚡ WordPress payload (with the fixes above)

```json
{
  "title": "Top 10 High-Throughput Microservice Architecture Patterns in 2027",
  "slug": "top-10-high-throughput-microservice-architecture-patterns-in-2027",
  "status": "publish",
  "categories": ["Software Engineering"],
  "audit": {
    "publicationId": "a7c1f0f2-1b0e-4a55-9b52-5c0c1d6f8e21",
    "contentSha256": "f27253646187f9d5f7aa44e397fee49df53d0001946d6b729b476911e0a03f0a",
    "permalink": "https://myblog.com/posts/top-10-high-throughput-microservice-architecture-patterns-in-2027"
  }
}
```

`contentSha256` is the SHA-256 of the sample article's HTML. `publicationId` changes on every run.

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/21596-publish-seo-safe-notion-blog-posts-to-wordpress-with-devdeskapp-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Apply the fixes from the known-issue box.
5. Connect **Notion**, **WordPress** (application password) and **Slack** credentials, then click **Test workflow**.
