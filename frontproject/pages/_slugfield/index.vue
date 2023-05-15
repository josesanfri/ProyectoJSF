<template>
    <section>
        <section>
            <basic-image
                class="view-main-section-picture"
                :image="{
                    src: '/img/restaurant/test.jpg',
                    alt: 'Imagen restaurante',
                    width: 750,
                    height: 150,
                    attrs: {
                        notLazy: true
                    }
                }"
                :initialLoad="false"
            />
            <details>
                <summary>
                    <basic-text-title
                        :title="'Menus'"
                        :attrs="{
                            isBold: true,
                        }"
                    />
                </summary>
            </details>
        </section>
        <section></section>
        <section></section>
    </section>
</template>

<script>
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

            console.log(restaurantData)
            console.log(menuData)
            
            return { 
                restaurantData,
                menuData,
                titlePage: `${restaurantData.address.street}, ${restaurantData.address.number}, ${restaurantData.address.region}`,
            }
        } catch {
            redirect(localePath('/error/ups/'))
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
            loadImages: false
        }
    },
    methods: {
        async submitReserve() {
            if(this.$store.state.auth.type == 'CUS') {
                let token = await getToken(this.$store)
                let profile
                try {
                    if(process.client) {
                        profile = await this.$axiosAPI.get(`profile/customer/${this.$store.state.auth.user.user_id}/`,
                            token ? { 'Authorization': token } : {}
                        )
                    }else{
                        profile = await this.$axiosIntern.get(`profile/customer/${this.$store.state.auth.user.user_id}/`,
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
                console.log(this.restaurantData, this.restaurantData.id)
                formData.append('restaurant', parseInt(this.restaurantData.id))
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

                if(res) {
                    this.$router.push(`/${this.$route.params.slugfield}/reserve/${res.controlpayment[0].payment.id}/`)
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
        showPopup() {
            if(!document.body.classList.contains('body-overflow')) {
                document.body.classList.add('body-overflow')
            }
            if(!this.$store.state.auth.isLoggedIn) {
                this.$store.commit('popup/visibility', true)
                return
            }
        },
    }
}
</script>

<style lang="sass" scoped>       
</style>