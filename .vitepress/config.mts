import { defineConfig } from 'vitepress'

export default defineConfig({
  title: 'DevDeskApp Docs',
  description: 'Official Documentation for DevDeskApp suite, developer utilities, and n8n-nodes-devdeskapp community node.',
  cleanUrls: true,
  head: [
    ['link', { rel: 'icon', href: '/logo.svg' }],
    ['meta', { name: 'theme-color', content: '#8b5cf6' }],
    ['meta', { name: 'og:site_name', content: 'DevDeskApp Docs' }],
    ['meta', { name: 'og:type', content: 'website' }],
    ['meta', { name: 'og:title', content: 'DevDeskApp Documentation & Automation Suite' }],
    ['meta', { name: 'og:description', content: 'Zero-API privacy developer tools and high-performance n8n automation node for developers, HR, and DevOps.' }]
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
      { text: 'Operations Reference', link: '/n8n/operations' },
      { text: 'Workflow Templates', link: '/n8n/workflow-templates' },
      { text: 'Architecture', link: '/solutions/' },
      {
        text: 'v0.1.4 (Latest)',
        items: [
          { text: 'NPM Package', link: 'https://www.npmjs.com/package/n8n-nodes-devdeskapp' },
          { text: 'n8n Template #21017', link: 'https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities' },
          { text: 'Node GitHub Repo', link: 'https://github.com/DevdeskApp/n8n-nodes-devdeskapp' },
          { text: 'DevDeskApp Web App', link: 'https://www.devdeskapp.com' }
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
          text: 'Solutions & Production',
          items: [
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
