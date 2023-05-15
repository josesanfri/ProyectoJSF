<template>
    <section class="card-restaurant">
        <section class="card-restaurant-section">
            <figure v-if="data.media_restaurant.length > 0">
                <picture class="flex">
                    <nuxt-img
                        class="img-basic"
                        decoding="async"
                        loading="lazy"
                        :src="data.media_restaurant[0].image"
                        :alt="data.media_restaurant[0].image"
                    />
                </picture>
            </figure>
            <article>
                <hgroup>
                    <basic-link
                        class="card-restaurant-title"
                        :href="'/'+data.slug_restaurant+'/'"
                        :label="'link-restaurant-'+data.slug_restaurant"
                        :text="data.name_restaurant"
                        :attrs="{
                            isBlue: true,
                        }"
                    />
                </hgroup>
                <basic-text-paragraph
                    :text="data.address.street + ', ' + data.address.number + ', ' + data.address.city"
                />
            </article>
            <article>
                <basic-link
                    class="card-restaurant-title"
                    :href="'/'+data.slug_restaurant+'/'"
                    :label="'link-property-'+data.slug_restaurant"
                    :text="'Ver restaurante'"
                    :attrs="{
                        isBlue: true,
                    }"
                />
            </article>
        </section>
    </section>
</template>

<script>
import getToken from "~/utils/token/getToken";

export default {
    data() {
        return {
        };
    },
    props: {
        data: {
            type: Object,
            required: true
        }
    },
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.card
    &-restaurant
        @apply p-8
        border-bottom: 1px solid #e4e9f2

        &::hover
           @include bg-gray-light

        &-section
            @apply grid grid-cols-1 items-center

            @media ( min-width: $tablet-max)
                @apply grid-cols-3

        &-title
            @apply text-lg font-bold

.img-basic
        @apply m-auto h-auto
</style>