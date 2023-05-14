<template>
    <section>
        <section class="cookies-section">            
            <article>
                <basic-list 
                    :title="textCookies.politics.title"
                    :items="textCookies.politics.items"
                />
                <br>
                <basic-list 
                    :title="textCookies.cookiesesp.title"
                    :items="textCookies.cookiesesp.items"
                />
                <br>
                <basic-list 
                    :items="textCookies.user.items"
                />
                <br>
                <p>afdafa</p>
            </article>
        </section>
    </section>
</template>

<script>
import textCookies from '~/content/pages/about/cookies/text.json'

export default {
    async asyncData() {
        return{
            textCookies: textCookies
        }
    },
    head() {
        return {
            titleTemplate: '%s Política de cookies',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'Información sobre la política de cookies'
                }
            ]
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

table, th, td
    @include border-dark
    @apply border-collapse text-center p-2

.cookies
    &-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20
</style>