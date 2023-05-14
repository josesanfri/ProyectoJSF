<template>
    <p 
        class="basic" 
        :class="{ 
            'color-white': attrs.isWhite, 
            'bold': attrs.isBold, 
            'font-xl': attrs.textXl
        }"
    >
        {{text}}
    </p>
</template>
  
<script>
export default {
    props: {
        text: {
            type: String,
            required: true
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                isWhite: false,
                isBold: false,
                textXl: false
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

    .bold
        @include font-bold

    .color-white
        @include color-white

    .font-xl
        @apply text-xl
</style>