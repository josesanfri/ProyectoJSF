<template>
    <ul>
        <li class="list-field" v-if="title">
            <basic-text-paragraph
                :text="title.text"
                :attrs="title.attrs"
            />
        </li>
        <li class="list-field" v-for="item in items" :key="item.label">
            <basic-link
                :text="item.text" 
                :label="item.label" 
                :href="item.href"
                :attrs="item.attrs"
            />
        </li>
    </ul>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: false
        },
        items: {
            type: Array,
            required: true
        }
    },
}
</script>

<style lang="sass" scoped>
    .list-field
        padding: .1rem 0 0 .1rem
</style>
