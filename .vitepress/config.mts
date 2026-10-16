import { defineConfig } from 'vitepress'

export default defineConfig({
  srcDir: 'src',
  title: 'DevDeskApp Docs',
  description: 'Official Documentation for DevDeskApp suite, developer utilities, and n8n-nodes-devdeskapp community node.',
  cleanUrls: true,
  sitemap: {
    hostname: 'https://docs.devdeskapp.com'
  },
  transformHead({ pageData }) {
    const cleanPath = pageData.relativePath
      .replace(/index\.md$/, '')
      .replace(/\.md$/, '')
    const canonical = cleanPath ? `https://docs.devdeskapp.com/${cleanPath}` : 'https://docs.devdeskapp.com/'
    return [
      ['link', { rel: 'canonical', href: canonical }]
    ]
  },
  head: [
    ['link', { rel: 'icon', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#6366f1' }],
    ['meta', { name: 'robots', content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' }],
    ['meta', { property: 'og:site_name', content: 'DevDeskApp Docs' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: 'en_US' }],
    ['meta', { property: 'og:image', content: 'https://docs.devdeskapp.com/logo-dark.jpg' }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:site', content: '@devdeskapp' }],
    ['meta', { name: 'twitter:image', content: 'https://docs.devdeskapp.com/logo-dark.jpg' }],
    [
      'script',
      { type: 'application/ld+json' },
      JSON.stringify({
        '@context': 'https://schema.org',
        '@graph': [
          {
            '@type': 'WebSite',
            name: 'DevDeskApp Documentation',
            url: 'https://docs.devdeskapp.com',
            description: 'Official documentation for DevDeskApp developer utilities, tools, and n8n-nodes-devdeskapp community node.'
          },
          {
            '@type': 'SoftwareApplication',
            name: 'DevDeskApp n8n Community Node',
            applicationCategory: 'DeveloperApplication, AutomationTool, AIAgentTool',
            operatingSystem: 'Cross-platform, Node.js, Docker, Linux, macOS, Windows',
            description: 'In-memory deterministic utility suite and AI Agent function calling tool for n8n workflows.',
            url: 'https://docs.devdeskapp.com',
            offers: {
              '@type': 'Offer',
              price: '0',
              priceCurrency: 'USD'
            }
          }
        ]
      })
    ]
  ],
  themeConfig: {
    logo: {
      light: '/logo-light.jpg',
      dark: '/logo-dark.jpg'
    },
    siteTitle: 'DevDeskApp',
    nav: [
      { text: 'DevDeskApp Suite', link: '/about/' },
      { text: 'n8n Node Guide', link: '/n8n/' },
      { text: '🤖 AI Agents & LLMs', link: '/solutions/ai-agents' },
      {
        text: 'More',
        items: [
          { text: '⚙️ Operations Reference', link: '/n8n/operations' },
          { text: '📋 Workflow Templates', link: '/n8n/workflow-templates' },
          { text: '🏛️ Architecture & Solutions', link: '/solutions/' },
          { text: '📦 NPM Package (v0.1.4)', link: 'https://www.npmjs.com/package/n8n-nodes-devdeskapp' },
          { text: '🌟 n8n Template #21017', link: 'https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities' },
          { text: '🐙 Node GitHub Repo', link: 'https://github.com/DevdeskApp/n8n-nodes-devdeskapp' },
          { text: '🌐 DevDeskApp Web App', link: 'https://www.devdeskapp.com' }
        ]
      }
    ],
    sidebar: {
      '/about/': [
        {
          text: 'DevDeskApp Platform',
          items: [
            { text: 'Platform Overview', link: '/about/' },
            { text: 'Zero-Leak Architecture', link: '/about/architecture' }
          ]
        }
      ],
      '/n8n/': [
        {
          text: 'n8n Community Node',
          items: [
            { text: 'Getting Started', link: '/n8n/' },
            { text: 'Step-by-Step Installation', link: '/n8n/installation' },
            { text: 'Operations Reference', link: '/n8n/operations' },
            { text: 'Workflow Templates', link: '/n8n/workflow-templates' }
          ]
        }
      ],
      '/solutions/': [
        {
          text: 'Solutions & AI',
          items: [
            { text: '🤖 AI Agents & LLM Calling', link: '/solutions/ai-agents' },
            { text: 'Local Node vs Cloud APIs', link: '/solutions/' },
            { text: 'Production Best Practices', link: '/solutions/best-practices' }
          ]
        }
      ]
    },
    socialLinks: [
      { icon: 'github', link: 'https://github.com/DevdeskApp' }
    ],
    search: {
      provider: 'local'
    },
    footer: {
      message: 'Released under the MIT License.',
      copyright: 'Copyright © 2026 DevDeskApp Community. All rights reserved.'
    }
  }
})
