---
title: 'Template #22360: Viral RSS Social Media Banner Publisher'
description: 'n8n template #22360: turn RSS blog feeds into dynamic OpenGraph social media banners, generate URL slugs, compute anti-duplicate SHA-256 hashes, and broadcast to LinkedIn, X, and Slack.'
---

# 🚀 Template #22360: Publish RSS-Based Social Banner Posts with DevDeskApp, LinkedIn, X, and Slack

<div style="margin: 1rem 0; display: flex; gap: 8px; flex-wrap: wrap; align-items: center;">
  <span class="badge-live">Published on n8n.io</span>
  <span class="badge-live badge-purple">Template ID: 22360</span>
</div>

🔗 **Template on n8n.io:** [n8n.io/workflows/22360](https://n8n.io/workflows/22360-publish-rss-based-social-banner-posts-with-devdeskapp-linkedin-x-and-slack/)

<div class="doc-image">
  <img src="/images/fig-canvas-22360.png" alt="Template 22360 RSS social banner publisher workflow on the n8n canvas" />
</div>
<div class="doc-caption">Figure 1: The template on the n8n canvas.</div>

---

## 🎯 Overview

Content marketers and developer advocates waste countless hours manually resizing blog banners, copy-pasting article summaries into social platforms, and managing campaign UTM tracking parameters. Inconsistent branding and delays in social posting directly reduce organic reach.

This template completely automates the blog-to-social distribution pipeline:

1. **Monitors RSS Blog Feeds**: Triggers automatically on new blog posts, WordPress articles, or Substack newsletter editions.
2. **Zero-API URL Encoding & Slugification**: Normalizes article titles into SEO-clean permalinks and formats dynamic query parameters with DevDeskApp **Slugify String**.
3. **Dynamic OpenGraph Banner Generation**: Constructs high-converting branded image URLs featuring the article title, author avatar, and reading time.
4. **Cryptographic Deduplication**: Generates an RFC **UUID v4** campaign tracking token and **SHA-256 fingerprint** to prevent accidental duplicate posts.
5. **Multi-Channel Broadcasting**: Concurrently publishes rich media cards to **LinkedIn**, **X (Twitter)**, and posts an announcement to your internal marketing **Slack** channel.

---

## 📸 Pipeline

<div class="doc-image">
  <img src="/images/fig-flow-22360.png" alt="Template 22360 pipeline: RSS trigger, DevDeskApp slugifier and crypto nodes, banner builder, LinkedIn, X, and Slack broadcast" />
</div>
<div class="doc-caption">Figure 2: Node order and branches in the published template.</div>

| Node | Resource · Operation | Purpose |
| :--- | :--- | :--- |
| RSS Feed Trigger / Manual Test | `trigger` · `rssFeedRead` / `manualTrigger` | Ingests new blog posts and article metadata |
| DevDeskApp: Article Slugifier | `text` · `slugify` | Normalizes headline into URL-safe campaign slugs |
| DevDeskApp: SHA-256 Fingerprint | `crypto` · `hash` (`sha256`) | Checksum of article URL + title to prevent duplicate postings |
| DevDeskApp: Campaign UUID | `crypto` · `uuid` | Tracking token for UTM analytics and multi-touch attribution |
| Build Dynamic Banner URL | `code` | Formats dynamic query parameters for on-the-fly branded image generation |
| LinkedIn: Share Update | LinkedIn node | Publishes formatted article card to company page or personal profile |
| X (Twitter): Post Tweet | Twitter node | Publishes tweet with preview banner and author attribution |
| Slack: Marketing Notification | Slack node | Alerts team with direct links to live social posts |

---

## ⚡ Execution sample

```json
{
  "status": "SOCIAL_PUBLISHED",
  "campaignId": "f47ac10b-58cc-4372-a567-0e02b2c3d479",
  "articleTitle": "How We Scaled In-Memory Webhooks to 10M Events with n8n",
  "articleSlug": "how-we-scaled-in-memory-webhooks-to-10m-events-with-n8n",
  "canonicalUrl": "https://www.devdeskapp.com/guides/scale-n8n-webhooks",
  "fingerprint": {
    "algorithm": "sha256",
    "hash": "4a5e6b7c8d9e0f1a2b3c4d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a"
  },
  "openGraphBannerUrl": "https://og.devdeskapp.com/api/banner?title=How+We+Scaled+In-Memory+Webhooks&author=DevDeskApp",
  "broadcast": {
    "linkedInPostId": "urn:li:share:7129841029481029",
    "tweetId": "182948102938102938",
    "slackChannel": "#announcements-marketing"
  }
}
```

---

## 📥 Import it

1. Make sure `n8n-nodes-devdeskapp` is installed ([installation guide](/n8n/installation)).
2. Open the [template on n8n.io](https://n8n.io/workflows/22360-publish-rss-based-social-banner-posts-with-devdeskapp-linkedin-x-and-slack/) and click **Use for free**, or copy the workflow JSON.
3. Paste it onto a new workflow canvas with **`Ctrl + V`** (**`Cmd + V`** on macOS).
4. Connect your **RSS Feed URL**, **LinkedIn OAuth2**, **X (Twitter) OAuth2**, and **Slack webhook**.
5. Click **Test workflow** to verify dynamic banner generation and instant multi-platform broadcasting.
