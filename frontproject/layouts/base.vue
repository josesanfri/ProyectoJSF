<template>
    <main>
        <Nuxt />
    </main>
</template>

<script lang="ts">
export default {
}
</script>

<style lang="sass" scoped>
    .page-enter-active, .page-leave-active
        transition: all 0.4s

    .page-enter-from, .page-leave-to
        opacity: 0
        filter: blur(1rem)
</style>