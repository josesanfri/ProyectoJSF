<template>
    <section>
        <hgroup style="grid-column: 1 / -1">
            <h1>La zona {{ zone || "La esquina gourmet" }}</h1>
        </hgroup>
        <nav class="search-box">
            <card-restaurant
                v-for="restaurant in results"
                :key="restaurant.id"
                :data="restaurant"
                @click.native="goOutPage"
            />
            <section class="search-box-buttons">
                <basic-button-solid
                    :attrs="{
                        isBlue: true,
                    }"
                    :text="'Atras'"
                    :type="'button'"
                    :disabled="!dataResponse || dataResponse.previous == null"
                    @click.native="dataResponse.previous ? remakeQuery(dataResponse.previous.split('?').length > 1 ? dataResponse.previous.split('?').at(-1) : '') : null"
                />
                <basic-button-solid
                    :attrs="{
                        isBlue: true,
                    }"
                    :text="'Siguiente'"
                    :type="'button'"
                    :disabled="!dataResponse || dataResponse.next == null"
                    @click.native="dataResponse.next ? remakeQuery(dataResponse.next.split('?').length > 1 ? dataResponse.next.split('?').at(-1) : '') : null"
                />
            </section>
        </nav>
    </section>
</template>

<script>
import getToken from "~/utils/token/getToken";

export default {
    head() {
        return {
            titleTemplate: this.query?.zone ? `%s Reservar en ${this.query.zone} mi restaurante favorito` : "%s Reservar en mi restaurante favorito",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Reserva en tu restaurante favorito",
                },
            ],
        };
    },
    async asyncData(ctx) {
        let { $axiosAPI, $axiosIntern, redirect, query, store } = ctx;
        let resRestaurant;

        try {
            let token = await getToken(store);

            if (process.client) {
                if (query?.zone) {
                    resRestaurant = await $axiosAPI.get(`restaurant/`,
                        {params: { zone: query.zone }},
                        token ? { 'Authorization': token } : {}
                    );
                } else {
                    resRestaurant = await $axiosAPI.get(`restaurant/`,
                        token ? { 'Authorization': token } : {}
                    );
                }
            } else {
                if (query?.zone) {
                    resRestaurant = await $axiosIntern.get(`restaurant/`,
                        {params: { zone: query.zone }},
                        token ? { 'Authorization': token } : {}
                    );
                } else {
                    resRestaurant = await $axiosIntern.get(`restaurant/`,
                        token ? { 'Authorization': token } : {}
                    );
                }
            }
        } catch {
            redirect("/error/ups/");
        }

        let { results, ...dataResponse } = resRestaurant.data;

        let zone = query?.zone;
        return {
            results,
            dataResponse,
            zone
        };
    },
    mounted() {
        this.scroll_search();
    },
    methods: {
        showPopupSearch() {
            if (this.$route.path != "/search/") {
                return;
            }
        },
        scroll_search() {
            setTimeout(this.showPopupSearch, 10000);
        },
        smallScreenSize() {
            return process.client ? document.documentElement.scrollWidth < 1024 : undefined;
        },
        goOutPage() {
            if (document.body.classList.contains("body-overflow")) {
                document.body.classList.remove("body-overflow");
            }
        },
        async remakeQuery(value) {
            try {
                this.zone = value.zone;
                let token = await getToken(this.$store);
                let params = new URLSearchParams(value).toString();
                let res;

                if (process.client) {
                    res = await this.$axiosAPI.get("restaurant/?" + params,
                        token ? { 'Authorization': token } : {}
                    );
                } else {
                    res = await this.$axiosIntern.get("restaurant/?" + params,
                        token ? { 'Authorization': token } : {}
                    );
                }

                let { results, ...dataResponse } = res.data;

                this.results = results;
                this.dataResponse = dataResponse;
            } catch (error) {
                console.log("Error: ", error);
            }

            document.querySelector(".search-box").scrollTo(0, 0);

            document.body.scrollTop = 0; // For Safari
            document.documentElement.scrollTop = 0; // For all normal browsers
        },
    },
};
</script>

<style lang="sass" scoped>
    .search
        &-box
            overflow-y: scroll
            display: grid
            grid-template-columns: 1fr

            &::-webkit-scrollbar
                display: none

            &-buttons
                grid-column: 1 / -1
                display: flex
                justify-content: center
                gap: 2rem
                max-height: 40px    
</style>