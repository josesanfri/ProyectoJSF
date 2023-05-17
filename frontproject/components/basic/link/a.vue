<template>
    <a
        class="basic"
        :class="{
            'color-white': attrs.isWhite, 
            'color-gray-dark': attrs.isGrayDark,
            'color-gray-light': attrs.isGrayLight,
            'color-primary': attrs.isBlue,
            'hover-primary': attrs.isHover,
            'center': attrs.isCenter,
            'gap-picture': icon && hasGap
        }" 
        :href="href"
        rel="noopener noreferrer" 
        :aria-label="label"
        :target="[newTab ? '_blanck' : '_top']"
        >
        <basic-image
            :class="{
                'mx-1': attrs.iconIsMarginAuto
            }"
            v-if="icon" 
            :image="icon.image" 
            :sources="icon.sources"
        /> {{text}}
    </a>
</template>

<script>
export default {
    props: {
        icon: {
            type: Object,
            required: false
        },
        hasGap: {
            type: Boolean,
            required: false,
            default: true    
        },
        href: {
            type: String,
            required: false,
            default: '#'
        },
        label: {
            type: String,
            required: true
        },
        text: {
            type: String,
            required: false,
            default: ''
        },
        open: {
            type: Boolean,
            required: false,
            default: false
        },
        refer: {
            type: Boolean,
            required: false,
            default: false
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
                isHover: false,
                iconIsMarginAuto: true
            })
        },
        newTab: {
            type: Boolean,
            required: false,
            default: false
        }
    }
}
</script>


<style lang="sass" scoped>
@import ~/assets/sass/components/basics/link/link
@import ~/assets/sass/theme/light/color

.basic
    @include link-basic

.color-white
    @include color-white

.color-gray-dark
    @include color-gray-dark

.color-gray-light
    @include color-gray-light

.color-primary
    @include color-primary

.center
    @apply flex justify-start items-center

.gap-picture
    @apply gap-2

.hover-primary
    &:hover
        @include color-primary-variant
        transition: all 0.3s ease-in-out
</style>