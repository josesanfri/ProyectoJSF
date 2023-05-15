<template>
    <p
        class="basic"
        :class="{
                'color-white': attrs.isWhite, 
                'color-gray-dark': attrs.isGrayDark,
                'color-gray-light': attrs.isGrayLight,
                'color-primary': attrs.isBlue,
                'center': attrs.isCenter,
                'bold': attrs.isBold
            }" 
        >
        <basic-image
            style="margin-right: 5px;"
            v-if="icon" 
            :image="icon.image"
            :sources="icon.sources"
        /> {{text}}
    </p>
</template>

<script>
export default {
    props: {
        icon: {
            type: Object,
            required: false
        },
        text: {
            type: String,
            required: true
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                isWhite: false,
                isGrayDark: false,
                isGrayLight: false,
                isBlue: false,
                isCenter: false,
                isBold: false
            })
        }
    }
}
</script>


<style lang="sass" scoped>
@import ~/assets/sass/components/basics/text/paragraph/paragraph
@import ~/assets/sass/theme/light/color

.basic
    @include p-basic

.color-white
    @include color-white

.color-gray-dark
    @include color-gray-dark

.color-gray-light
    @include color-gray-light

.color-primary
    @include color-primary

.center
    display: flex

.bold
    font-weight: bolder
</style>