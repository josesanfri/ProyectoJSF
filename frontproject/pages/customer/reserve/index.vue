<template>
    <section class="min-height">
        <basic-text-title
            class="cover-title"
            :title="reserveText.cover.title" 
        />
        
        <section class="cust-reserve-section">
            <card-reserve
            />
        </section>
        
    </section>
</template>

<script>
import reserveText from '~/content/components/card/reserve.json'

export default {
    async asyncData(ctx) {
        return{
            reserveText: reserveText
        }
    },
    head() {
        return {
            titleTemplate: '%s Mis reservas',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'My reserves'
                }
            ]
        }
    },
    props: {
        myreserves: {
            type: Object,
            required: false
        }
    },
}
</script>

<style lang="sass">
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.min-height
    min-height: 65vh

.cover-title
    @include bg-gray-soft 
    @apply border-b-2 border-gray-400 text-center pt-20

    @media ( min-width: $large-screen)
        @apply text-left pl-12

.cust-reserve
    &-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20
</style>