import DefaultTheme from 'vitepress/theme'
import './custom.css'
import HeroShowcase from './components/HeroShowcase.vue'
import QuickNavGrid from './components/QuickNavGrid.vue'
import NodeVersion from './components/NodeVersion.vue'
import { onMounted, watch, nextTick } from 'vue'
import { useRoute, useData } from 'vitepress'
import mediumZoom from 'medium-zoom'

function updateFavicon(dark: boolean) {
  if (typeof document === 'undefined') return
  const iconLinks = document.querySelectorAll<HTMLLinkElement>("link[rel~='icon'], link[rel='shortcut icon']")
  const newHref = dark ? '/logo-dark.jpg' : '/logo-light.jpg'
  if (iconLinks.length > 0) {
    iconLinks.forEach(link => {
      link.type = 'image/jpeg'
      link.href = newHref
    })
  } else {
    const link = document.createElement('link')
    link.rel = 'icon'
    link.type = 'image/jpeg'
    link.href = newHref
    document.head.appendChild(link)
  }
}

export default {
  extends: DefaultTheme,
  setup() {
    const route = useRoute()
    const { isDark } = useData()

    const initZoom = () => {
      // Attach smooth zoom to all documentation images except navbar/icons
      mediumZoom('.vp-doc img, .doc-image img', {
        background: 'rgba(15, 23, 42, 0.92)',
        margin: 24,
        scrollOffset: 40
      })
    }

    onMounted(() => {
      initZoom()
      updateFavicon(isDark.value || document.documentElement.classList.contains('dark'))
      const observer = new MutationObserver(() => {
        updateFavicon(document.documentElement.classList.contains('dark'))
      })
      observer.observe(document.documentElement, { attributes: true, attributeFilter: ['class'] })
    })

    watch(
      () => isDark.value,
      (val) => {
        updateFavicon(val)
      }
    )

    watch(
      () => route.path,
      () => nextTick(() => {
        initZoom()
      })
    )
  },
  enhanceApp({ app }) {
    app.component('HeroShowcase', HeroShowcase)
    app.component('QuickNavGrid', QuickNavGrid)
    // <NodeVersion /> in Markdown: latest n8n-nodes-devdeskapp version (build-time + live refresh).
    app.component('NodeVersion', NodeVersion)
  }
}
