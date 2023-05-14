<template>
    <figure>
        <picture class="flex">
          <template v-if="loadImage">
            <source
                v-for="source in sources"
                :key="source.srcset"
                :media="source.media"
                :srcset="source.srcset"
            >
            <img
                :loading="image.attrs.notLazy ? 'eager' : 'lazy'"
                decoding="async"
                class="img-basic"
                :class="{
                    'width-auto': image.attrs.autoWidth,
                    'width-height-auto': image.attrs.autoSize,
                    'circle': image.attrs.isRounded,
                    'border-rounded': image.attrs.borderRounded,
                    'no-width-height-auto': image.attrs.noWHauto,
                    'top-rounded': image.attrs.topRounded,
                    'img-contrast': image.attrs.needContrast,
                    'center-item': image.attrs.isItemCenter
                }"
                :src="image.src"
                :alt="image.alt"
                :width="image.width"
                :height="image.height"
            >
          </template>
        </picture>
    </figure>
  </template>
  
<script>
export default {
    props: {
        image: {
            type: Object,
            required: true
        },
        sources: {
            type: Array,
            required: false
        },
        initialLoad: {
            type: Boolean,
            required: false,
            default: true
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                autoWidth: false,
                isRounded: false,
                borderRounded: false,
                noWHauto: false,
                topRounded: false,
                needContrast: false,
                notLazy: true
            })
        }
    },
    data() {
        return {
            loadImage: false
        }
    },
    created() {
        if(!this.initialLoad) {
        if(!this.$store.state.devices.bot) {
            this.loadImage = true
        }
        } else {
        this.loadImage = true
        }
    }
}
</script>
  
<style lang="sass" scoped>
    .img-basic
        @apply m-auto h-auto

    .img-contrast
        image-rendering: -webkit-optimize-contrast

    .width-auto
        @apply w-auto

    .circle
        @apply rounded-full

    .border-rounded
        @apply rounded

    .no-width-height-auto
        max-width: none
        height: none

    .width-height-auto
        @apply w-full h-full

    .top-rounded
        border-radius: .25rem .25rem 0 0
</style>
  