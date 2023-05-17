<template>
    <main :class="{'main': prevented}">
        <header-customer />
        <Nuxt />
        <basic-to-top />
        <popup-web-sign-in-up v-show="showedPopup" />
        <footer-web />
    </main>
</template>

<script>
    export default {
        computed: {
            showedPopup() {
                return this.$store.state.popup.show
            }
        },
        data() {
            if(!this.$store.state.devices.bot) {
                return {
                    prevented: false
                }
            }
            return {
                prevented: true
            }
        }
    }
</script>

<style lang="sass" scoped>
    main
        position: relative
    
    .main::v-deep *
        font-size: 1rem !important
        font-family: inital !important
        font-weight: normal !important
</style>