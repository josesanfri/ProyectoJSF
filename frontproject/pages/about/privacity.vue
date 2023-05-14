<template>
    <section>
        <section class="privacity-section">
            <article>
                <basic-text-title 
                    :title="privacityText.politics.title"
                />
                <br>
                <basic-list 
                    :title="privacityText.compromise.title"
                    :items="privacityText.compromise.items"
                />
                <br>
                <basic-list 
                    :title="privacityText.data.title"
                    :items="privacityText.data.items"
                    :paragraph="privacityText.data.paragraph"
                />
                <br>
                <basic-text-title
                    :title="privacityText.veracity.title"
                />
                <br>
                <basic-list 
                    :title="privacityText.rights.title"
                    :items="privacityText.rights.items"
                    :paragraph="privacityText.rights.paragraph"
                />
                <br>
                <basic-text-title 
                    :title="privacityText.security.title"
                />
                <br>
                <basic-text-title 
                    :title="privacityText.personal.title"
                />
            </article>
        </section>
    </section>
</template>

<script>
import privacityText from '~/content/pages/about/privacity/text.json'

export default {
    async asyncData() {
        return {
            privacityText: privacityText
        }
    },
    head() {
        return {
            titleTemplate: '%s Política de privacidad',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'Información sobre los términos y condiciones de la privacidad ofrecida por La Esquina Gourmet'
                }
            ]
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.privacity
    &-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20
</style>