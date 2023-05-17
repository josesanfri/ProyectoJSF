<template>
    <details class="details-basic">
        <summary class="summary-basic">
            <basic-text-title 
                v-if="title" 
                :title="title"
                :attrs="title.attrs"
            />
        </summary>
        <basic-text-paragraph
            class="p-basic"
            v-if="paragraph"
            :text="paragraph.text" 
            :attrs="paragraph.attrs"
        />
    </details>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: false
        },
        paragraph: {
            type: Object,
            required: false
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({})
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/basics/dropdown/dropdown
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/components/basics/text/paragraph/paragraph

.details-basic
    @include details-basic

.summary-basic
    @include summary-basic
    @apply items-center
    display: block

    @media ( min-width: $large-screen)
        white-space: nowrap


.p-basic
    @include p-basic
    @apply p-4 block

@keyframes sweep
    0%
        opacity: 1
        transform: translateX(-10px)
    100%
        opacity: 1
        transform: translateX(0)

details[open] summary ~ * 
    animation: sweep .5s ease-in-out
    display: none
    content: "+"
    font-size: 1rem
    padding-left: 1rem 

summary::-webkit-details-marker
    display: none

summary:after
    display: none
    content: "-"
    font-size: 1rem
    padding-left: 1rem 
</style>