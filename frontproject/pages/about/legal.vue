<template>
    <section>
        <section class="legal-section">
            <article>
                <basic-list 
                    :title="textLegal.legal.title"
                    :items="textLegal.legal.items"
                />
                <br>
                <card-info
                    :title="textLegal.users.title"
                    :paragraph="textLegal.users.paragraph"
                />
                <br>
                <basic-list 
                    :title="textLegal.use.title"
                    :items="textLegal.use.items"
                />
                <br>
                <card-info 
                    :title="textLegal.property.title"
                    :paragraph="textLegal.property.paragraph"
                />
                <br>
                <card-info 
                    :title="textLegal.guarantee.title"
                    :paragraph="textLegal.guarantee.paragraph"
                />
                <br>
                <card-info 
                    :title="textLegal.modifications.title"
                    :paragraph="textLegal.modifications.paragraph"
                />
                <br>
                <card-info 
                    :title="textLegal.links.title"
                    :paragraph="textLegal.links.paragraph"
                />
                <br>
                <card-info 
                    :title="textLegal.rights.title"
                    :paragraph="textLegal.rights.paragraph"
                />
                <br>
                <card-info 
                    :title="textLegal.generalities.title"
                    :paragraph="textLegal.generalities.paragraph"
                />
                <br>
                <basic-list 
                    :title="textLegal.terms.title"
                    :items="textLegal.terms.items"
                />
                <br>
                <card-info 
                    :title="textLegal.legislation.title"
                    :paragraph="textLegal.legislation.paragraph"
                />
                <br>
            </article>
        </section>
    </section>
</template>

<script>
import textLegal from '~/content/pages/about/legal/text.json'

export default {
    async asyncData() {
        return {
            textLegal: textLegal
        }
    },
    head() {
        return {
            titleTemplate: '%s Aviso legal',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'Información de las condiciones legales de La Esquina Gourmet'
                }
            ]
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.legal

    &-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20
</style>