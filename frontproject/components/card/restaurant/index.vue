<template>
    <section class="card-restaurant">
        <section class="card-restaurant-section">
            <article>
                <hgroup>
                    <basic-link
                        class="card-restaurant-title"
                        :href="'/'+data.slug_restaurant+'/'"
                        :label="'link-restaurant-'+data.slug_restaurant"
                        :text="data.name_restaurant"
                        :attrs="{
                            isHover: true,
                        }"
                    />
                </hgroup>
                <basic-text-paragraph
                    :text="data.address.street + ', ' + data.address.number + ', ' + data.address.city"
                />
                <basic-list
                    :items="cardRestaurant.times.items"
                />
            </article>
            <article>
                <basic-link
                    class="card-restaurant-title"
                    :href="'/'+data.slug_restaurant+'/'"
                    :label="'link-restaurant-'+data.slug_restaurant"
                    :text="cardRestaurant.button.label"
                    :icon="cardRestaurant.button.icon"
                    :attrs="cardRestaurant.button.attrs"
                />
            </article>
            <article>
                <basic-link-a
                    class="card-restaurant-title"
                    :href="'https://www.google.com/maps/search/?api=1&query='+data.address.latitude+','+data.address.longitude"
                    :label="'link-restaurant-'+data.slug_restaurant"
                    :text="cardRestaurant.map.label"
                    :icon="cardRestaurant.map.icon"
                    :attrs="cardRestaurant.map.attrs"
                />
            </article>
        </section>
    </section>
</template>

<script>
import cardRestaurant from '~/content/components/card/restaurant.json'

export default {
    data() {
        return {
            cardRestaurant: cardRestaurant
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

        &:hover
           @include bg-white-variant

        &-section
            @apply grid grid-cols-1 items-center

            @media ( min-width: $tablet-max)
                @apply grid-cols-3

        &-title
            @apply text-lg font-bold

.img-basic
        @apply m-auto h-auto
</style>