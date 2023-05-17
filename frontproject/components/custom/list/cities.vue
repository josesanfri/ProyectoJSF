<template>
    <section class="section">
        <basic-text-paragraph 
            v-if="title" 
            :text="title.text"
            :attrs="title.attrs"
            class="section__title"
        />
        <template v-if="title.subtitle">
            <basic-text-paragraph 
                :text="title.subtitle.text"
                :attrs="title.subtitle.attrs"
                class="section__title"
            />
            <br>
        </template>
        <ul class="list">
            <li class="list__item" v-for="item in items" :key="item.label" :class="{'item__card': attrs.card}">
                <NuxtLink
                    :to="{path: item.href != '#' ? item.href : item.ref}"
                    rel="noopener noreferrer" 
                    :aria-label="item.label"
                >
                    <basic-image
                        v-if="item.picture"
                        :initialLoad="false"

                        :image="{
                            src: item.picture.link,
                            alt: item.picture.alt,
                            width: item.picture.width,
                            height: item.picture.height,
                            attrs: {
                                notLazy: false
                            }
                        }"
                        :sources="[
                            {
                                srcset: item.picture.link,
                                media: '(min-width: 320px)',
                            }
                        ]"
                    />
                    <basic-text-paragraph
                        class="list__item__paragraph"
                        v-if="item.text"
                        :text="item.text"
                        :attrs="item.attrs"
                    />
                </NuxtLink>
            </li>
        </ul>
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
        attrs: {
            type: Object,
            required: false,
            default: () => ({})
        }
    }
}
</script>

<style lang="sass" scoped>
.section
    @apply p-4 text-center

    &__title
        @apply flex justify-center

.list
    display: flex
    flex-wrap: wrap
    padding: 1rem
    gap: 1rem
    justify-content: space-evenly

    &__item
        position: relative
        height: 150px
        transform: scale(1)
        justify-content: center
        display: flex

        &:hover
            transform: scale(1.05)
            transition: transform 1s ease-in-out

        &__paragraph
            position: absolute
            bottom: 5px
            left: 10px

.item__card
    box-shadow: 1px 1px 5px 0 #000000aa
    border-radius: 4px
</style>