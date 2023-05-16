<template>
    <article
        class="message" 
        :ref="reference"
        :class="{
            'message-danger': type.isDanger,
            'message-warning': type.isWarning,
            'message-success': type.isSuccess,
            'message-info': type.isInfo
        }"
    >
        <basic-text-paragraph-icon
            :icon="icon"
            :text="text"
            :attrs="{
                isCenter: true
            }"
        />

        <basic-image
            class="message-close-icon"
            @click="hide"
            :image="{
                  src: '/icon/base/black/xmark.webp',
                  alt: 'cross icon',
                  width: 30,
                  height: 30,
                  attrs: {
                      needContrast: true
                  }
              }"
            :sources="[{
                srcset: '/icon/base/black/xmark.webp',
                media:'(min-width: 320px)',
            }]"
        />
        
    </article>
</template>

<script>
export default {
    mounted() {
        setTimeout(this.hide, 10000)
    },
    methods: {
        hide() {
            this.$store.commit('message/removeItem', this.reference)
        }
    },
    props: {
        icon: {
            type: Object,
            required: false
        },
        text: {
            type: String,
            required: true
        },
        id: {
            type: String,
            required: false
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({})
        },
        type: {
            type: Object,
            required: false,
            default: () => ({})
        },
        reference: {
            type: String,
            required: true
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/notification/notification

.message-close-icon
    position: absolute
    top: .3rem
    right: .3rem
    cursor: pointer

.message
    @include message-alert
    position: relative

    &-danger
        @include danger-alert

    &-warning
        @include warning-alert

    &-success
        @include success-alert

    &-info
        @include info-alert
</style>