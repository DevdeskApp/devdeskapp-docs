import { type DefaultTheme, defineConfigWithTheme } from 'vitepress'
import { resolveN8nNodeVersion } from './n8n-node-version'
import { N8N_NODE_VERSIONS_URL } from './theme/n8n-node'

// Latest n8n-nodes-devdeskapp release, baked into every page at build time (the
// <NodeVersion /> component also refreshes it in the browser). The deploy workflow
// rebuilds daily, so the nav label follows new npm releases without a docs commit.
const n8nNode = await resolveN8nNodeVersion()
console.log(`n8n-nodes-devdeskapp version: ${n8nNode.version} (${n8nNode.source})`)

const OG_IMAGE = 'https://docs.devdeskapp.com/og-docs.jpg'

export default defineConfigWithTheme<DefaultTheme.Config & { n8nNodeVersion: string }>({
  srcDir: 'src',
  // Files in src/public are static assets (auth.md, llms.txt...). Without this,
  // VitePress also renders public/auth.md as an indexable /public/auth page.
  srcExclude: ['public/**'],
  title: 'DevDeskApp Docs',
  description: 'Official Documentation for DevDeskApp suite, developer utilities, and n8n-nodes-devdeskapp community node.',
  cleanUrls: true,
  // Git commit time of each page: shown as "Last updated" and emitted as <lastmod> in sitemap.xml.
  lastUpdated: true,
  sitemap: {
    hostname: 'https://docs.devdeskapp.com'
  },
  transformHead({ pageData, title, description }) {
    // The 404 page must not claim a canonical URL and must stay out of the index.
    if (pageData.isNotFound || pageData.relativePath === '404.md') {
      return [['meta', { name: 'robots', content: 'noindex, follow' }]]
    }
    const cleanPath = pageData.relativePath
      .replace(/index\.md$/, '')
      .replace(/\.md$/, '')
    const canonical = cleanPath ? `https://docs.devdeskapp.com/${cleanPath}` : 'https://docs.devdeskapp.com/'
    return [
      ['link', { rel: 'canonical', href: canonical }],
      ['meta', { property: 'og:url', content: canonical }],
      ['meta', { property: 'og:title', content: title }],
      ['meta', { property: 'og:description', content: description }],
      ['meta', { name: 'twitter:title', content: title }],
      ['meta', { name: 'twitter:description', content: description }]
    ]
  },
  head: [
    ['link', { rel: 'icon', href: '/logo.svg' }],
    ['link', { rel: 'ai-catalog', href: 'https://docs.devdeskapp.com/.well-known/ai-catalog.json', type: 'application/json' }],
    ['link', { rel: 'api-catalog', href: 'https://docs.devdeskapp.com/.well-known/api-catalog', type: 'application/linkset+json' }],
    ['link', { rel: 'service-doc', href: 'https://docs.devdeskapp.com/llms.txt', type: 'text/markdown' }],
    ['link', { rel: 'mcp-server', href: 'https://docs.devdeskapp.com/.well-known/mcp/server-card.json', type: 'application/json' }],
    ['link', { rel: 'agent-skills', href: 'https://docs.devdeskapp.com/.well-known/agent-skills/index.json', type: 'application/json' }],
    ['script', {}, `(function(){try{const mc=(typeof document!=='undefined'&&document.modelContext)||(typeof navigator!=='undefined'&&navigator.modelContext);if(mc&&typeof mc.registerTool==='function'){mc.registerTool({name:'search_documentation',description:'Search DevDeskApp documentation',inputSchema:{type:'object',properties:{query:{type:'string'}},required:['query']},execute:async(p)=>({result:'Results for '+p.query})});}}catch(e){}})();`],
    ['meta', { name: 'theme-color', content: '#6366f1' }],
    ['meta', { name: 'robots', content: 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1' }],
    ['meta', { property: 'og:site_name', content: 'DevDeskApp Docs' }],
    ['meta', { property: 'og:type', content: 'website' }],
    ['meta', { property: 'og:locale', content: 'en_US' }],
    // 1200x630 social card (the old logo-dark.jpg was 120x120 but declared 1200x630).
    ['meta', { property: 'og:image', content: OG_IMAGE }],
    ['meta', { property: 'og:image:width', content: '1200' }],
    ['meta', { property: 'og:image:height', content: '630' }],
    ['meta', { property: 'og:image:type', content: 'image/jpeg' }],
    ['meta', { property: 'og:image:alt', content: 'DevDeskApp Docs: n8n community node and developer utilities' }],
    ['meta', { name: 'twitter:card', content: 'summary_large_image' }],
    ['meta', { name: 'twitter:site', content: '@devdeskapp' }],
    ['meta', { name: 'twitter:image', content: OG_IMAGE }],
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
    n8nNodeVersion: n8nNode.version,
    logo: {
      light: '/logo-light.jpg',
      dark: '/logo-dark.jpg'
    },
    siteTitle: 'DevDeskApp',
    nav: [
      { text: 'DevDeskApp Suite', link: '/about/' },
      { text: 'n8n Node Guide', link: '/n8n/' },
      { text: '📋 Templates', link: '/templates/' },
      { text: '🤖 AI Agents & LLMs', link: '/solutions/ai-agents' },
      {
        text: 'More',
        items: [
          { text: '⚙️ Operations Reference', link: '/n8n/operations' },
          { text: '📋 Templates Catalog', link: '/templates/' },
          { text: '🏛️ Architecture & Solutions', link: '/solutions/' },
          { text: `📦 NPM Package (v${n8nNode.version})`, link: N8N_NODE_VERSIONS_URL },
          { text: '🌟 n8n Template #21017', link: 'https://n8n.io/workflows/21017-format-json-and-secure-hr-payloads-with-devdeskapp-utilities' },
          { text: '💰 n8n Template #21130', link: 'https://n8n.io/workflows/21130-automate-salary-and-in-hand-ctc-calculations-with-devdeskapp' },
          { text: '🛡️ n8n Template #21376', link: 'https://n8n.io/workflows/21376' },
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
            { text: 'Workflow Templates Hub', link: '/templates/' }
          ]
        }
      ],
      '/templates/': [
        {
          text: 'Workflow Templates Hub',
          items: [
            { text: '📋 All Templates Catalog', link: '/templates/' },
            { text: '⚡ Quick Import Guide', link: '/templates/how-to-import' }
          ]
        },
        {
          text: 'Official Blueprints',
          items: [
            { text: '🌟 Developer Suite (#21017)', link: '/templates/developer-suite' },
            { text: '💰 CTC Salary Engine (#21130)', link: '/templates/ctc-salary-engine' },
            { text: '🛡️ Payment Webhook Sanitizer (#21376)', link: '/templates/payment-webhook-sanitizer' }
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
