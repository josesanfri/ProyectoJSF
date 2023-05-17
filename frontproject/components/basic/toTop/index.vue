<template>
    <span v-if="showToTop" @click="goTop" id="toTop" class="toTop" :class="{'pink': attrs.isPink, 'blue': attrs.isBlue}">
        <basic-image
            :image=" {
                src: '/icon/base/white/chevron-up.webp',
                alt: 'chevron up icon',
                width: 30,
                height: 30,
                attrs: {
                    needContrast: true
                }
            }"
            :sources=" [{
                srcset: '/icon/base/white/chevron-up.webp',
                media:'(min-width: 320px)',
            }]"       
        />
    </span>
</template>

<script>
export default {
props: {
    attrs: {
        type: Object,
        required: false,
        default: () => ({
            isPink: false,
            isBlue: true
        })
    }
},
data() {
    return {
        showToTop: false
    }
},
mounted() {
    window.addEventListener('scroll', this.showedToTop)
},
methods: {
    goTop() {
        document.body.scrollTop = 0 // For Safari
        document.documentElement.scrollTop = 0 // For all normal browsers
    },
    showedToTop() {
        this.showToTop = document.body.scrollTop > 50 || document.documentElement.scrollTop > 50
    }
}
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/theme/light/color

.pink
    @include bg-secondary

.blue
    @include bg-primary

.toTop
    position: fixed
    bottom: 1rem
    right: 1rem
    width: 50px
    height: 50px
    display: grid
    justify-content: center
    align-items: center
    border-radius: 50%
    color: #fff
    font-size: 1.2rem
    opacity: .5
    cursor: pointer
    transition: opacity 1s ease-in-out
    z-index: 1

    &:hover
        opacity: 1

</style>