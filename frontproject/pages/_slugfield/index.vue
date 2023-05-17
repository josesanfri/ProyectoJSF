<template>
    <section>
        <section>
            <section>
                <section class="carousel-restaurants-slider">
                    <section class="slider-restaurants" ref="slider">
                        <section
                            class="slider-restaurants-content"
                            v-for="(slide, index) in restaurantData.media_restaurant"
                            :key="index"
                        >
                            <nuxt-picture
                                class="img-basic"
                                decoding="async"
                                loading="lazy"
                                :src="slide.image"
                                :alt="slide.image"
                            />
                        </section>
                    </section>
                </section>
                <section class="mt-4">
                    <div v-if="restaurantData.media_restaurant.length != 0" class="slider-restaurants-controls">
                        <button
                            type="button"
                            @click="moveSlider(n)"
                            v-for="n in restaurantData.media_restaurant.length"
                            :key="n"
                            class="slider-restaurants-controls-link"
                        >
                        </button>
                    </div>
                </section>
            </section>  
            <details class="details-basic">
                <summary class="summary-basic">
                    <basic-text-title
                        :title="textSlug.menu.title"
                        :attrs="textSlug.menu.attrs"
                    />
                </summary>
                <basic-link
                    class="p-4 block"
                    v-for="menu in menuData"
                    :key="menu.id"
                    :href="'/menu/'+menu.id+'/'"
                    :label="'link-restaurant-'+menu.id"
                    :text="menu.name"
                    :attrs="{
                        isHover: true,
                    }"
                />
            </details>
        </section>
        <section class="restaurant-section-data">
            <section class="restaurant-section-info">
                <basic-text-title
                    :title="{
                        text:`${restaurantData.name_restaurant}`,
                        attrs: {
                            textXl: true
                        }
                    }"
                />
                <basic-text-paragraph
                    v-if="restaurantData.description != null"
                    :text="`${restaurantData.description}`"
                />
                <basic-list
                    :items="textSlug.times.items"
                />
                <basic-link-a
                    :href="'https://www.google.com/maps/search/?api=1&query='+restaurantData.address.latitude+','+restaurantData.address.longitude"
                    :label="'link-restaurant-'+restaurantData.slug_restaurant"
                    :text="textSlug.map.label"
                    :icon="textSlug.map.icon"
                    :attrs="textSlug.map.attrs"
                />
                <basic-text-paragraph-icon
                    :text="`${restaurantData.primary_phone}`"
                    :icon="textSlug.phone.icon"
                    :attrs="textSlug.phone.attrs"
                />
            </section>
            <form @submit.prevent="submitReserve" id="reserveForm" class="restaurant-form">
                <basic-text-title
                    :title="textSlug.reserve.title"
                    :attrs="textSlug.reserve.attrs"
                />
                <basic-input
                    :type="'date'"
                    :placeholder="'aaaa-mm-dd'"
                    :value="''"
                    :name="'confirmed_date'"
                    :id="'confirmed_date'"
                    :form="'reserveForm'"
                />

                <basic-text-title
                    :title="textSlug.time.title"
                    :attrs="textSlug.time.attrs"
                />
                <basic-input
                    :type="'time'"
                    :placeholder="'Hora'"
                    :value="''"
                    :name="'confirmed_time'"
                    :id="'confirmed_time'"
                    :form="'reserveForm'"
                />

                <basic-text-title
                    :title="textSlug.select.title"
                    :attrs="textSlug.select.attrs"
                />
                <basic-input
                    :type="'select'"
                    :placeholder="textSlug.select.placeholder"
                    :name="'num_customers'"
                    :id="'num_customers'"
                    :form="'reserveForm'"
                    :items="textSlug.select.items"
                />
                <basic-button-solid
                    :text="textSlug.reservebtn.button"
                    :type="'submit'"
                    :attrs="textSlug.reservebtn.attrs"  
                />
            </form>
        </section>
    </section>
</template>

<script>
import textSlug from '~/content/pages/slugfield/restaurant.json'
import getToken from '~/utils/token/getToken'

export default {
    async asyncData(ctx) {
        let {params, $axiosAPI, $axiosIntern, redirect, store} = ctx

        try {
            let restaurantData
            let menuData
            let token = await getToken(store)
            if(process.client) {
                restaurantData = await $axiosAPI.get(`restaurant/${params.slugfield}`,
                    token ? { 'Authorization': token } : {}
                ).then(
                    res => res.data
                ).catch( err => redirect('/error/ups/'))

            } else {
                restaurantData = await $axiosIntern.get(`restaurant/${params.slugfield}`,
                    token ? { 'Authorization': token } : {}
                ).then(
                    res => res.data
                ).catch( err => redirect('/error/ups/'))
            }

            if(process.client) {
                menuData = await $axiosAPI.get('menu/',
                    token ? { 'Authorization': token } : {}
                ).then(
                    res => res.data
                ).catch( err => redirect('/error/ups/'))

            } else {
                menuData = await $axiosIntern.get('menu/',
                    token ? { 'Authorization': token } : {}
                ).then(
                    res => res.data
                ).catch( err => redirect('/error/ups/'))
            }

            menuData = menuData.results
            
            return { 
                restaurantData,
                menuData,
                textSlug: textSlug,
                titlePage: `${restaurantData.address.street}, ${restaurantData.address.number}, ${restaurantData.address.region}`,
            }
        } catch {
            redirect('/error/ups/')
        }
    },
    head() {
        return {
            titleTemplate: `%s `+ this.titlePage,
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'Reserva mesa, ubicada en '+this.titlePage
                }
            ]
        }
    },
    data() {
        return {
            loadImages: false,
            slider: null,
            width: null,
        }
    },
    methods: {
        async submitReserve() {
            if(this.$store.state.auth.type == 'CUS') {
                let token = await getToken(this.$store)
                let profile
                try {
                    if(process.client) {
                        profile = await this.$axiosAPI.get(`profile/user/${this.$store.state.auth.user.user_id}/`,
                            token ? { 'Authorization': token } : {}
                        )
                    }else{
                        profile = await this.$axiosIntern.get(`profile/user/${this.$store.state.auth.user.user_id}/`,
                            token ? { 'Authorization': token } : {}
                        )
                    }   
                } catch {
                    this.$store.commit('message/addItem', {
                        text: 'Para reservar es necesario tener su perfil completo!',
                        icon: {
                            image: {
                                src: '/icon/base/black/triangle-exclamation.webp',
                                alt: 'triangle exclamation icon',
                                width: 30,
                                height: 30,
                                attrs: {
                                    needContrast: true
                                }
                            }, 
                            sources: [{
                                srcset: '/icon/base/black/triangle-exclamation.webp',
                                media:'(min-width: 320px)',
                            }]
                        },
                        reference: new Date().getTime().toString(),
                        type: {
                            isDanger: true
                        }
                    })
                    return
                }
        
                const form = document.querySelector('#reserveForm')
                const formData = new FormData(form)
                formData.append('restaurant', parseInt(this.restaurantData.id))
                console.log(formData)
                let res
                try {
                    if(process.client){
                        res = await this.$axiosAPI.post( 'reserve/create/', formData, 
                            token ? { 'Authorization': token } : {}
                        )
                    }else {
                        res = await this.$axiosIntern.post( 'reserve/create/', formData, 
                            token ? { 'Authorization': token } : {}
                        )
                    }  
                } catch(error) {
                    console.log("Error", error)
                }
            }
            else if (!this.$store.state.auth.user.token) {
                document.querySelector('#button-open-signinup').click()
            }
            else {
                this.$store.commit('message/addItem', {
                    text: 'Para reservar es necesario tener una cuenta!',
                    icon: {
                        image: {
                            src: '/icon/base/black/triangle-exclamation.webp',
                            alt: 'triangle exclamation icon',
                            width: 30,
                            height: 30,
                            attrs: {
                                needContrast: true
                            }
                        }, 
                        sources: [{
                            srcset: '/icon/base/black/triangle-exclamation.webp',
                            media:'(min-width: 320px)',
                        }]
                    },
                    reference: new Date().getTime().toString(),
                    type: {
                        isWarning: true
                    }
                })
            }
        },
        moveSlider(n) {
            n = n - 1;
            this.slider.scrollTo({
                left: this.width * n,
                behavior: "smooth",
            });
        },
        showPopup() {
            if(!document.body.classList.contains('body-overflow')) {
                document.body.classList.add('body-overflow')
            }
            if(!this.$store.state.auth.isLoggedIn) {
                this.$store.commit('popup/visibility', true)
                return
            }
        },
    },
    async mounted() {
        this.slider = this.$refs.slider;
        this.width = this.slider.offsetWidth;
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color
@import ~/assets/sass/components/basics/dropdown/dropdown

.carousel-restaurants
    &-section
        @include bg-gray-soft
        @apply p-4

    &-slider
        @apply flex items-center justify-between
        flex-flow: column nowrap

.slider-restaurants
    @apply flex overflow-scroll relative flex-none w-full h-full
    flex-flow: row nowrap
    scroll-snap-type: x mandatory

    &::-webkit-scrollbar
        display: none

    &-controls
        @apply flex justify-center items-center gap-4 h-full text-center

        &-link
            @apply w-4 h-4 rounded-full inline-block
            background-color: #333
            background-clip: content-box
            border: 0.25rem solid transparent

    &-content
        @apply text-center flex-none flex justify-center items-center h-full w-screen
        scroll-snap-align: center
        scroll-snap-align: center

.details-basic
    @include details-basic
    @include bg-primary

.summary-basic
    @include summary-basic
    @apply items-center
    display: block

    @media ( min-width: $large-screen)
        white-space: nowrap 

@keyframes sweep
    0%
        opacity: 1
        transform: translateX(-10px)
    100%
        opacity: 1
        transform: translateX(0)

details[open] summary ~ * 
    animation: sweep .5s ease-in-out

summary::-webkit-details-marker
    display: none

summary:after
    display: none
    content: ""
    font-size: 1rem
    padding-left: 1rem

.list-y-fields
    @apply pt-0 pb-0

.restaurant
    &-section
        &-data
            @apply flex flex-col gap-4

            @media ( min-width: $large-screen)
                @apply grid grid-cols-2

        &-info
            @apply p-4

    &-form
        @apply flex flex-col gap-4 p-4
</style>