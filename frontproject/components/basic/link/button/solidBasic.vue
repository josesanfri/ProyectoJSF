<template>
    <a
        :class="{'pink': isPink, 'blue': isBlue}" 
        :href="href"
        rel="noopener noreferrer" 
        :aria-label="label"
    >
        {{text}}
    </a>
</template>

<script>
export default {
    props: {
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

    .pink
        @include solid-pink

    .blue
        @include solid-blue
</style>