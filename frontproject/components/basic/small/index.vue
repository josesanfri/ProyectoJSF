<template>
    <small 
        class="basic"
        :class="{
            'color-white': attrs.isWhite,
            'bold': attrs.isBold,
            'center': attrs.isCenter
        }"
    >
        <basic-image
            v-if="icon"
            :image="icon.image"
            :sources="icon.sources"
        /> {{text}}
    </small>
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
                isBold: false
            })
        },
        icon: {
            type: Object,
            required: false
        }
    }
}
</script>

<style lang='sass' scoped>
@import ~/assets/sass/components/basics/text/paragraph/paragraph
@import ~/assets/sass/theme/light/color
  
.basic
    @include p-basic

.bold
    @include font-bold

.color-white
    @include color-white

.center
    @apply flex justify-center
</style>