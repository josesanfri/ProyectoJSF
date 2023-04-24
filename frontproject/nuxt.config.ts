// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            // Main title of web
            title: 'La Esquina Gourmet:',
      
            // Inject meta tags
            meta: [
                { charset: 'utf-8' },
                { name: 'viewport', content: 'width=device-width, initial-scale=1' },
                {
                    hid: 'description',
                    name: 'description',
                    content: 'my website description'
                }  
            ],

            htmlAttrs: {
                lang: 'es'
            },

            link: [{ rel: 'icon', type: 'image/x-icon', href: "~/fav.svg" }]
        },
        pageTransition: { name: 'page', mode: 'out-in' }
    },
    
    // Static config
    static: {
        prefix: false
    },

    typescript: {
        strict: false
    },

    // Global CSS: https://go.nuxtjs.dev/config-css
    css: [
        '~/assets/main.sass',
    ],

    // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
    plugins: [
    ],

    // Auto import components by folder: https://go.nuxtjs.dev/config-components
    components: true,

    server: {
        host: 'localhost',
        port: 80,
    },
})
