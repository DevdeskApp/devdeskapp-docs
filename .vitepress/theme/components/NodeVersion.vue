<script setup lang="ts">
import { onMounted } from 'vue'
import { useData } from 'vitepress'
import { scheduleN8nNodeVersionRefresh, useN8nNodeVersion } from '../n8n-node'

// Latest n8n-nodes-devdeskapp version: baked in at build time, refreshed from npm in the browser.
const { theme } = useData()
const version = useN8nNodeVersion(theme.value.n8nNodeVersion)
onMounted(scheduleN8nNodeVersionRefresh)
</script>

<template>
  <span class="n8n-node-version">v{{ version }}</span>
</template>
