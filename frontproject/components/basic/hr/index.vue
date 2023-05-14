<template>
    <hr 
        class="hr-basic"
        :class="{
            'color-primary': attrs.isBlue,
            'color-secondary': attrs.isPink,
            'color-gray-dark': attrs.isGray
        }"
    >
</template>

<script>
export default {
    props: {
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                isPink: false,
                isBlue: false,
                isGray: true
            })
        }
    }
}
</script>

<style lang="sass" scoped>
    @import ~/assets/sass/theme/light/color

    .hr-basic
        @apply my-2
        height: 2px
        border: none

    .color-primary
        @include bg-primary

    .color-secondary
        @include bg-secondary

    .color-gray-dark
        @include bg-gray-dark
</style>