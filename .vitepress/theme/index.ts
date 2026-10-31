import DefaultTheme from 'vitepress/theme'
import './custom.css'
import HeroShowcase from './components/HeroShowcase.vue'
import QuickNavGrid from './components/QuickNavGrid.vue'
import NodeVersion from './components/NodeVersion.vue'
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

    onMounted(() => {
      initZoom()
    })

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
