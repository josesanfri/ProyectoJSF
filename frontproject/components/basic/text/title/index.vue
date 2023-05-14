<template>
    <hgroup>
        <h1 
            v-if="title.text"
            class="title"
            :class="{
                'color-white': title.attrs.isWhite,
                'bold': title.attrs.isBold,
                'font-xl': title.attrs.textXl,
                'title-xxl': title.attrs.titleXxl
            }"
        >
            {{title.text}}
        </h1>

        <h2 
            v-if="title.subtitle" 
            class=""
            :class="{
                'color-white': title.subtitle.attrs.isWhite,
                'bold': title.subtitle.attrs.isBold
            }"
        >
            {{title.subtitle.text}}
        </h2>

        <basic-text-paragraph
            v-if="title.paragraph"
            :text="title.paragraph.text"
            :attrs="title.paragraph.attrs" 
        />
    </hgroup>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: true
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                isWhite: false,
                isBold: false,
                textXl: false,
                titleXxl: false
            })
        }
    }
}
</script>

<style lang="sass" scoped>
    @import ~/assets/sass/components/basics/text/paragraph/paragraph
    @import ~/assets/sass/theme/light/color

    .title
        @apply py-2
        height: fit-content

    .basic
        @include p-basic

    .bold
        @include font-bold

    .color-white
        @include color-white

    .font-xl
        @apply text-xl

    .title-xxl
        @include font-bold
        font-size: 7rem
        line-height: 3.75rem
        -webkit-text-stroke: 6px black
</style>