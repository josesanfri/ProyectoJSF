<template>
	<article>
        <custom-cover-search
            :title="textIndex.search.title"
            :select="textIndex.search.select"
            :button="textIndex.search.button"
            :bottom="textIndex.search.bottom"
        />
        <custom-list-cities
            :title="textIndex.cities.title"
            :items="textIndex.cities.items"
            :attrs="textIndex.cities.attrs"
        />
    </article>
</template>

<script>
import textIndex from '~/content/pages/index/text.json'

export default {
    layout: 'web/index',
    scrollToTop: true,
    asyncData() {
        return {
            textIndex: textIndex
        }
    },
    head() {
        return {
            titleTemplate: '%s Inicio',
            meta: [
                { name: 'robots', content: 'index,follow' },
            ]
        }
    },
    data() {
        if(!this.$store.state.devices.bot) {
            return {
                loadImage: true
            }
        }
        return {
            loadImage: false
        }
    },
    async mounted() {
        try {
            console.log(this.$store.state.auth.user.token)
        } catch (error) {
            console.log(error);
        }
    },
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/basics/image/url
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.list-horizontal
    display: grid !important
    grid-template-columns: repeat(2, 1fr) !important
    grid-template-rows: repeat(2, 1fr) !important

    & > li
        text-align: center

    @media ( min-width: $tablet-max)
        grid-template-columns: repeat(4, 1fr) !important
        grid-template-rows: 1fr !important

        & > li
            text-align: left

.home
    &-section
        @include bg-gray-soft
        @apply grid items-center m-auto
        grid-template-columns: 1fr
        gap: 1rem

        @media ( min-width: $large-screen)
            grid-template-columns: repeat(4, 1fr)
</style>