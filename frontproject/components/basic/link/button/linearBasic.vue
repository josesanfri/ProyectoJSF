<template>
    <a
        :class="{'pink': isPink, 'blue': isBlue, 'green': isGreen}" 
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
        isGreen: {
            type: Boolean,
            required: false,
            default: false
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
    @import ~/assets/sass/components/basics/button/linear

    .pink
        @include linear-pink

    .blue
        @include linear-blue

    .green
        @include linear-green
</style>