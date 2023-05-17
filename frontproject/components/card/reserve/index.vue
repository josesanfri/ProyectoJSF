<template>
    <section v-if="resReserves.length != 0">
        <article v-for="(reserve, index) in resReserves" :key="reserve.id" class="reserve-customer-separator">
            <section :id="'reserve-'+index" class="reserve-customer-box">
                <article class="reserve-customer-one">
                    <basic-text-title
                        :title="{
                            text: `${reserve.restaurant.address.street}, ${reserve.restaurant.address.city}, ${reserve.restaurant.address.number}`,
                            attrs: {
                                isWhite: true,
                                isBold: true
                            },
                        }"
                    />
                </article>

                <article class="reserve-customer-two">
                    <section class="reserve-customer-media">
                        <basic-list
                            class="text-center"
                            :items="[
                                {
                                    text: `${reserveText.reserveCode} ${reserve.id}`,
                                    attrs: {} 
                                }
                            ]"
                        />
                    </section>

                    <section class="reserve-customer-data">
                        <div class="flex">
                            <!-- Status of the reserve -->
                            <basic-small
                                v-if="reserve.status == 'Confirmed'"
                                class="reserve-customer-state reserve-customer-state-success"
                                :text="`Confirmada`"
                            />
                            <basic-small
                                v-else-if="reserve.status == 'Denied'"
                                class="reserve-customer-state reserve-customer-state-danger"
                                :text="`Denegada`"
                            />
                        </div>
                        <div class="m-auto">
                            <!-- Date and status of the reserve contract -->
                            <basic-list
                                :items="[
                                    {
                                        text: `${reserveText.from} ${reserve.confirmed_date} ${reserveText.time} ${reserve.confirmed_time}`,
                                        attrs: {} 
                                    },
                                ]"
                            />
                        </div>
                    </section>
                </article>
            </section>
        </article>
    </section>
</template>

<script>
import getToken from '~/utils/token/getToken'
import reserveText from '~/content/components/card/reserve.json'

export default {
    props: {
    },
    data() {
        return {
            resReserves: [],
            reserveText: reserveText
        };
    },
    async mounted() {
        try {
            let token = await getToken(this.$store)
            let getReserves

            if(process.client){

                getReserves = await this.$axiosAPI.get("reserve/", 
                    token ? { 'Authorization': token } : {}
                )
                .then(getReserves => (this.resReserves = getReserves.data.results))

            }else{

                getReserves = await this.$axiosIntern.get("reserve/", 
                    token ? { 'Authorization': token } : {}
                )
                .then(getReserves => (this.resReserves = getReserves.data.results))

            }
            
            this.resReserves = this.resReserves.sort(function(a, b) {
                return a.id-b.id; /* Modificar si se desea otra propiedad */
            });

            console.log(this.resReserves)

        } catch (error) {
            console.log(error);
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color
@import ~/assets/sass/components/basics/button/base
@import ~/assets/sass/components/basics/button/solid
@import ~/assets/sass/components/basics/list/list

.d-none
    display: none

.reserve-customer
    &-separator
        @apply mb-4

    &-box
        @include border-gray-light
        @include bg-white
        @apply shadow rounded

    /* ARTICLE ONE ADDRESS */

    &-one
        @include bg-primary
        @apply grid items-center border-b border-gray-200 p-2
        grid-template-columns: 1fr
        gap: 1rem
        border-radius: 3px 3px 0px 0px

    &-state
        grid-column: 2 / -1
        grid-row: 1/-1
        margin: auto .7rem auto auto

        &-warning
            @include btn-warning
            cursor: default !important

        &-success
            @include btn-success
            cursor: default !important

        &-danger
            @include btn-danger
            cursor: default !important

    /* ARTICLE TWO DATA */

    &-two
        @apply grid items-center
        grid-template-columns: 1fr
        gap: 1rem

        @media ( min-width: $large-screen)
            grid-template-columns: repeat(2, 1fr)

    &-media
        @apply grid items-center p-4 border-gray-200
        grid-template-columns: 1fr
        gap: 1rem

        @media ( min-width: $large-screen)
            @apply border-r h-full
            grid-template-columns: repeat(2, 1fr)

    &-data
        @apply grid items-center p-4 border-t border-gray-200

        @media ( min-width: $large-screen)
            @apply border-0

    /* ARTICLE THREE MORE */

    &-three
        @apply border-t border-gray-200

    &-seemore
        @apply p-4

    &-btn-more
        @include solid-pink
        @apply w-full

    &-more
        @apply shadow border border-gray-200

.list-y
    @include list-y

    &-fields
        @apply py-2    
</style>