<template>
    <section>
        <basic-text-title 
            v-if="title" 
            :title="title"
            :attrs="title.attrs"
        />
        <basic-hr
            v-if="hr"
            :attrs="hr.attrs"  
        />
        <ul class="list-y">
            <li :class="image ? 'list-y-image' : 'list-y-fields'" v-for="item in items" :key="item.text">
                <basic-image
                    v-if="item.image"
                    :image="item.image"
                    :sources="item.sources"
                />
                <basic-text-paragraph
                    v-if="item.text"
                    :text="item.text"
                    :attrs="item.attrs"
                />
            </li>
        </ul>
        <basic-text-paragraph 
            v-if="paragraph"
            :text="paragraph.text" 
            :attrs="paragraph.attrs"
        />
    </section>
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
    },
    hr: {
        type: Object,
        required: false
    },
    paragraph: {
        type: Object,
        required: false
    },
    attrs: {
        type: Object,
        required: false,
        default: () => ({})
    },
    image: {
        type: Boolean,
        required: false,
        default: () => false
    }
},
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/basics/list/list

.list-y
    @include list-y

    &-fields
        @apply py-2

    &-image
        @apply flex p-2
        justify-content: flex-start
        align-items: flex-start
        gap: .2rem
        p
            @apply w-full
        
</style>