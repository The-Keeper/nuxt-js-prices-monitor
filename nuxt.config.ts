import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  hooks: {
    'ready': () => {
    
    }
  },
  modules: [
    // Simple usage
    'nuxt-highcharts',
  ],
  postcss: {
    plugins: {
      'postcss-import': {},
      'tailwindcss/nesting': {},
      tailwindcss: {},
      autoprefixer: {},
    },
  },
})