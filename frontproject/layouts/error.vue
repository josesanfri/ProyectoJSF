<template>
    <main class="main-default">
        <notification-box />
        <figure>
            <picture>
                <source srcset="/img/logo/logo.webp">
                <img
                    loading="lazy"
                    decoding="async"
                    width="80" height="60"
                    src="/img/logo/logo.webp"
                    alt="logo"
                    format="webp"
                    class="main-default__picture"
                />
            </picture>
        </figure>
        <section class="main-default__section">
            <basic-text-title 
                class="main-default__section__titles"
                :title="{
                    text: 'textUps.title',
                    attrs: {},
                    subtitle: {
                        text: 'textUps.subtitle',
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
                        :text="'home'"
                        :isWhite="true"
                    />
                </li>
                <li>
                    <basic-link-button-solid
                        :href="'/'"
                        :label="'contact-page'"
                        :text="'contact'"
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