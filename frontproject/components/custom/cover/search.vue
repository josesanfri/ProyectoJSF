<template>
    <section :class="{
            'coverSearch': true,
            'coverSearch-background': loadImage
        }"
    >
        <article class="coverSearch-article">
            <basic-text-title
                class="coverSearch-title"
                :title="title"
            />
            <form @submit.prevent="goSearch" id="selectSearchForm" class="coverSearch-form">
                <basic-input
                    @click.native="$event.target.value = ''"
                    :type="'text'"
                    :placeholder="select.placeholder"
                    :name="'search-select'"
                    :id="'search-select'"
                    :form="'selectSearchForm'"
                    :datalist="select"
                    class="coverSearch-search-forn-btn radius-left"
                />
                
                <basic-button-solid
                    :type="button.type"
                    :text="button.text"
                    :attrs="{isBlue:true}"
                    class="coverSearch-search-forn-btn radius-right"
                />
            </form>
            <custom-list-search
                class="coverSearch-bottom"
                :items="bottom"
            />
        </article>
    </section>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: true
        },
        select: {
            type: Object,
            required: true
        },
        button: {
            type: Object,
            required: true
        },
        bottom: {
            type: Array,
            required: true
        }
    },
    data() {
        if(!this.$store.state.devices.bot) {
            return {
                loadImage: true
            }
        }

        return {
            loadImage: false
        }
    },
    methods: {
        goSearch() {
            let query = document.querySelector("#search-select").value

            this.$router.push({ 
                path: '/search/', 
                query:{ zone: query }
            })
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/pages/index

.radius
    &-left
        ::v-deep input
            border-radius: .25rem 0 0 .25rem

    &-right
        border-radius: 0 .25rem .25rem 0
</style>