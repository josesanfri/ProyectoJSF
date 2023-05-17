<template>
    <header>
        <nav class="navigation">
            <blur @click.native="navOpenClose" v-if="showedNav" :active="showedNav" style="z-index: 1" class="blur" />
            <picture class="navigation-logo-box">
                <span class="navigation-open-close">
                    <basic-image
                        v-if="!showedNav" 
                        :image="{
                        src: '/icon/base/black/bars.webp',
                        alt: 'bars icon',
                        width: 30,
                        height: 30,
                        attrs: {
                            needContrast: true
                        }
                        }"
                        :sources="[{
                            srcset: '/icon/base/black/bars.webp',
                            media:'(min-width: 320px)',
                        }]" 
                        @click.native="navOpenClose" 
                    />
                    <basic-image 
                        v-else 
                        :image="{
                            src: '/icon/base/black/xmark.webp',
                            alt: 'cross icon',
                            width: 30,
                            height: 30,
                            attrs: {
                                needContrast: true
                            }
                        }"
                        :sources="[{
                            srcset: '/icon/base/black/xmark.webp',
                            media:'(min-width: 320px)',
                        }]" 
                        @click.native="navOpenClose" 
                    />
                </span>
                <source srcset="/img/logo/logo.webp">
                <nuxt-link :to="'/'" class='navigation-logo-item'>
                <img
                    decoding="async"
                    width="55" height="30"
                    src="/img/logo/logo.webp"
                    alt="logo"
                    format="webp"
                />
                </nuxt-link>
            </picture>

            <ul class="list" :class="{'navTransition' : showedNav}">
                <li class="list-item" @click="navOpenClose">
                    <basic-link
                        :href="'/'"
                        :label="headerText.home.label" 
                        :text="headerText.home.text"
                    />
                </li>

                <li class="list-item" @click="navOpenClose">
                    <basic-link
                        :href="'/contact/'"
                        :label="headerText.contact.label" 
                        :text="headerText.contact.text"
                    />
                </li>

                <li class="list-item" @click="navOpenClose">
                    <basic-link
                        :href="'/search/'"
                        :label="headerText.search.label" 
                        :text="headerText.search.text"
                    />
                </li>

                <!-- IF USER IS CUSTOMER LINK TO PANEL -->
                <li class="list-item" 
                    @click="navOpenClose"
                    v-if="user_type"
                >
                    <basic-link
                        v-if="user_type=='CUS'"
                        :href="'/customer/profile/'"
                        :label="headerText.panel.label" 
                        :text="headerText.panel.text"
                    />
                </li>

                <li class="list-item" 
                    @click="navOpenClose"
                    v-if="user_type"
                >
                    <basic-link
                        v-if="user_type=='CUS'"
                        :href="'/customer/reserve/'"
                        :label="headerText.panelreserve.label" 
                        :text="headerText.panelreserve.text"
                    />
                </li>

                <li class="list-separator">
                    <basic-hr-text :text="'o'" />
                </li>
                <!-- IF USER IS NOT LOGGED IN BUTTON -->
                <li class="list-user">
                    <basic-button-solid
                        v-if="!isLoggedIn"
                        :attrs="{
                            isBlue: true
                        }" 
                        :text="headerText.login.text"
                        :id="'button-open-signinup'"
                        @click.native="showPopup"
                    />
                    <basic-button-solid 
                        v-else
                        :attrs="{
                            isBlue: true
                        }" 
                        :text="headerText.logout.text"
                        @click.native="logout"
                    />
                </li>
            </ul>
        </nav>
    </header>
</template>

<script>
import headerText from '~/content/components/header/web.json'
import getToken from '~/utils/token/getToken'
import Cookies from 'js-cookie'

export default {
    data(){
        return{
            headerText: headerText
        }
    },
    computed:{
        user(){
            return this.$store.state.auth.user
        },
        user_type() {
            return this.$store.state.auth.type
        },
        isLoggedIn(){
            return this.$store.state.auth.isLoggedIn
        },
        showedNav() {
            return this.$store.state.navigation.show
        }
    },
    mounted: function () {
        this.$nextTick(function () {
            this.onResizeHeader();
        })
        window.addEventListener('resize', this.onResizeHeader)
    },
    methods: {
        async logout() {
            let token = await getToken(this.$store)
            let res = await this.$axiosAPI.post('logout/', {}, 
                token ? {
                    'Authorization': token
                } 
                : {}
            ).catch(
                err => console.log(err)
            )

            this.$store.commit('auth/logout')

            Cookies.remove('leg__token')
            Cookies.remove('leg__id') 
            Cookies.remove('leg__email') 
            Cookies.remove('leg__user_type') 
        },
        navOpenClose() {
            if(document.documentElement.scrollWidth < 1024) {
            this.$store.commit('navigation/visibility', !this.$store.state.navigation.show)

            document.body.classList.toggle('body-overflow')
            }
        },
        onResizeHeader() {
            if(this.$store.state.devices.device.isDesktop) {
                if(document.querySelector('.list').scrollHeight + 60 < window.innerHeight) {
                document.querySelector('.list').style.overflowY = 'hidden'
                }
                else {
                document.querySelector('.list').style.overflowY = 'scroll'
                }

                if(this.$store.state.navigation.show && document.documentElement.scrollWidth >= 1024) {
                this.$store.commit('navigation/visibility', false)
                }
                
            }
        },
        showPopup() {
            if(this.$store.state.navigation.show) {
            this.navOpenClose()
            }
            
            if(!document.body.classList.contains('body-overflow')) {
            document.body.classList.add('body-overflow')
            }
            
            this.$store.commit('popup/visibility', true)
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/header/web/nav

.blur
    @media ( min-width: $tablet-max)
        display: none
</style>