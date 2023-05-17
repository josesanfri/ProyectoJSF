<template>
    <section class="notification-box" 
        v-if="notifications"
    >
        <notification-message
            v-for="key in Object.entries(notifications)"
            :key="key[0]"
            :icon="key[1].icon"
            :text="key[1].text"
            :type="key[1].type"
            :id="key[0]"
            :reference="key[0]"
        />
    </section>
</template>

<script>
export default {
    data() {
        return {
            notifications: this.$store.state.message.items
        }
    }
}
</script>

<style lang="sass" scoped>
    .notification-box
        position: fixed
        display: flex
        flex-direction: column
        bottom: 1rem
        right: 2rem
        z-index: 20
        gap: .5rem
</style>