<template>
    <button :class="{'pink': attrs.isPink, 'blue': attrs.isBlue, 'disabled': disabled}" :type="type" :disabled="disabled" >
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
            default: () => ({
                isPink: false,
                isBlue: false
            })
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

    .disabled
        @apply cursor-not-allowed opacity-50
</style>