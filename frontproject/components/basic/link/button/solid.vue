<template>
    <NuxtLink
        :class="{'pink': isPink, 'blue': isBlue, 'white': isWhite, 'disabled': disabled}" 
        :to="{path: href != '#' ? href : href}"
        rel="noopener noreferrer" 
        :aria-label="label"
    >
        {{text}}
    </NuxtLink>
</template>

<script>
export default {
    props: {
        disabled: {
            type: Boolean,
            required: false,
            default: false
        },
        href: {
            type: String,
            required: true
        },
        label: {
            type: String,
            required: true
        },
        text: {
            type: String,
            required: true
        },
        isPink: {
            type: Boolean,
            required: false,
            default: false
        },
        isBlue: {
            type: Boolean,
            required: false,
            default: false
        },
        isWhite: {
            type: Boolean,
            required: false,
            default: false
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
        }
    }
}
</script>


<style lang="sass" scoped>
    @import ~/assets/sass/components/basics/button/solid

    .disabled
        pointer-events: none !important
        opacity: .5 !important
        cursor: not-allowed !important

    .pink
        @include solid-pink

    .blue
        @include solid-blue

    .white
        @include solid-white
</style>