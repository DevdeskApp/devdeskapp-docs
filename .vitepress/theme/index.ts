import DefaultTheme from 'vitepress/theme'
import './custom.css'
import HeroShowcase from './components/HeroShowcase.vue'
import QuickNavGrid from './components/QuickNavGrid.vue'
import { onMounted, watch, nextTick } from 'vue'
import { useRoute } from 'vitepress'
import mediumZoom from 'medium-zoom'

export default {
  extends: DefaultTheme,
  setup() {
    const route = useRoute()

    const initZoom = () => {
      // Attach smooth zoom to all documentation images except navbar/icons
      mediumZoom('.vp-doc img, .doc-image img', {
        background: 'rgba(15, 23, 42, 0.92)',
        margin: 24,
        scrollOffset: 40
      })
    }

    const syncNpmVersion = async () => {
      try {
        const res = await fetch('https://registry.npmjs.org/n8n-nodes-devdeskapp/latest')
        if (res.ok) {
          const data = await res.json()
          if (data && data.version) {
            const ver = `v${data.version}`
            document.querySelectorAll('.VPNavBarMenuLink, .VPFlyout button, .VPMenuLink, .badge-live').forEach(el => {
              if (el.textContent && el.textContent.includes('(Latest)')) {
                el.textContent = `${ver} (Latest)`
              }
            })
          }
        }
      } catch {
        // Fallback silently
      }
    }

    onMounted(() => {
      initZoom()
      syncNpmVersion()
    })

    watch(
      () => route.path,
      () => nextTick(() => {
        initZoom()
        syncNpmVersion()
      })
    )
  },
  enhanceApp({ app }) {
    app.component('HeroShowcase', HeroShowcase)
    app.component('QuickNavGrid', QuickNavGrid)
  }
}
