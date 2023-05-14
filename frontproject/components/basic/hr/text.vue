<template>
    <span 
        :id="id" 
        class="span-br"
    >
        {{text}}
    </span>
</template>

<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        },
        id: {
            type: String,
            required: false
        }
    }
}
</script>

<style lang="sass" scoped>
    @import ~/assets/sass/theme/light/color

    .span-br
        @include color-gray-light
        @apply flex items-center text-center
        gap: 10px

        &::before
            @apply block
            border-bottom: 1px solid #9CA3AF
            content: ""
            flex: 1 1
            height: 1px

        &::after
            @apply block
            border-bottom: 1px solid #9CA3AF
            content: ""
            flex: 1 1
            height: 1px
</style>