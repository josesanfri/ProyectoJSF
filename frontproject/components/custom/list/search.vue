<template>
    <ul class="basic-list-y-custom">
        <li class="basic-list-y-fields" v-for="item in items" :key="item.text">
            <basic-text-paragraph
                v-if="item.text"
                :text="item.text"
                :attrs="item.attrs"
            />
        </li>
    </ul>
</template>

<script>
export default {
    props: {
        items: {
            type: Array,
            required: true
        }
    },
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/basics/list/list
@import ~/assets/sass/utils/breakpoints

.basic
    &-list-y-custom
        @apply flex flex-col m-auto w-full gap-4
        margin-bottom: 0px

        @media ( min-width: $large-screen)
            @apply grid items-center m-auto grid-cols-3
            margin-bottom: 0px

    &-list-y-fields
        @apply py-2
</style>