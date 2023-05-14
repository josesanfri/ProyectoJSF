<template>
    <article>
        <basic-text-title 
            v-if="title" 
            :title="title"
            :attrs="title.attrs"
        />
        <basic-hr
            v-if="hr"
            :attrs="hr.attrs"  
        />
        <basic-text-paragraph 
            v-if="paragraph"
            :text="paragraph.text" 
            :attrs="paragraph.attrs"
        />
    </article>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: false
        },
        paragraph: {
            type: Object,
            required: false
        },
        hr: {
            type: Object,
            required: false
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({})
        }
    },
}
</script>

<style lang="sass" scoped>
</style>