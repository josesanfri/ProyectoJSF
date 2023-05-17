<template>
    <main class="main-default">
        <notification-box />
        <section class="main-default__section">
            <basic-text-title 
                class="main-default__section__titles"
                :title="{
                    text: `¡UPS!`,
                    attrs: {},
                    subtitle: {
                        text: `Parece que no hemos podido encontrar la página que buscas.`,
                        attrs: {}
                    }
                }"
                :attrs="{
                    isWhite: true,
                    isBold: true,
                    textXl: true
                }"
            />
            <ul class="main-default__section__links">
                <li>
                    <basic-link-button-linear
                        :href="'/'"
                        :label="'home-page'"
                        :text="'Volver al inicio'"
                        :isWhite="true"
                    />
                </li>
                <li>
                    <basic-link-button-solid
                        :href="'/contact/'"
                        :label="'contact-page'"
                        :text="'Contáctanos'"
                        :isWhite="true"
                    />
                </li>
            </ul>
        </section>
    </main>
</template>

<script>
export default {
    head() {
        return {
            titleTemplate: '%s No hemos encontrado la página.',
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Página informativa de url no disponible.",
                },
            ],
        }
    },
    data() {
        return {
        };
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/theme/light/color

.main-default
    display: flex
    flex-direction: column
    width: 100vw
    max-width: 100vw
    height: 100vh
    max-height: 100vh
    @include bg-primary

    &__section
        display: grid
        @include color-white
        margin: auto
        text-align: center

        &__titles::v-deep h1
            font-size: 6rem

        &__links
            margin-top: 1rem
            display: flex
            gap: 1rem
            justify-content: center
</style>