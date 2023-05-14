<template>
    <footer class="footer">
        <section class="footer-section">
            <basic-image
                :image="{
                    src: '/img/logo/logo.webp',
                    alt: 'gray logo',
                    width: 160,
                    height: 120,
                    attrs: {
                        needContrast: true
                    }
                }"
                :sources="[{
                    srcset: '/img/logo/logo.webp',
                    media:'(min-width: 320px)',
                }]"
            />
            <basic-list-link 
                class="footer-about"
                :title="footerText.about.title"
                :items="footerText.about.items"
            />
            <basic-list-link 
                class="footer-terms"
                :title="footerText.terms.title"
                :items="footerText.terms.items"
            />
            <custom-list-contact
                class="footer-support"
                :title="footerText.support.title"
                :items="footerText.support.items"
            />
            <basic-small 
                class="footer-copyright"
                :text="footerText.copyright.text"     
                :attrs="footerText.copyright.attrs"     
                :icon="footerText.copyright.icon"
            />
        </section>
    </footer>
</template>

<script>
import footerText from '~/content/components/footer/web.json'

export default {
    data() {
        return {
            footerText: footerText
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.footer
    @include bg-gray-dark
    @apply p-10 grid gap-4
    z-index: 2

    &-section
        @apply flex flex-col items-center text-center gap-4

        @media ( min-width: $tablet-max)
            @apply grid grid-cols-4 items-start text-left

    &-support
        @apply items-center

        @media ( min-width: $large-screen)
            @apply items-start
</style>