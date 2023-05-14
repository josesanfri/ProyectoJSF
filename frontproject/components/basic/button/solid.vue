<template>
    <button 
        :class="{'pink': attrs.isPink, 'blue': attrs.isBlue, 'full': attrs.isFull, 'disabled': disabled}" 
        :type="type" 
        :disabled="disabled"
    >
        {{text}}
    </button>
</template>

<script>
export default {
    props: {
        disabled: {
            type: Boolean,
            required: false,
            default: false
        },
        type: {
            type: String,
            required: false,
            default: 'button'
        },
        text: {
            type: String,
            required: true
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
    @import ~/assets/sass/components/basics/button/solid

    .pink
        @include solid-pink

    .blue
        @include solid-blue

    .full
        @apply w-full

    .disabled
        @apply cursor-not-allowed opacity-50
</style>