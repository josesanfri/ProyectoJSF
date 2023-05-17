<template>
    <section class="popup-sign-in-up">
        <basic-link
            @click.native="hidePopup" 
            class="blur"            
            :label="'blur-popup'"
            :text="''" 
        />
        <nav class="popup-nav">
            <hgroup class="popup-nav-hgroup">
                <basic-link-a
                    id="btn-back"
                    @click.native="move('back')"
                    style="display: none; position: absolute; top: 0; left: 0; font-weight: bolder;"
                    :icon="{
                        image: {
                            src: '/icon/base/black/arrow-left.webp',
                            alt: 'arrow left icon',
                            width: 30,
                            height: 30,
                            attrs: {
                                needContrast: true
                            }
                        }, 
                        sources: [{
                            srcset: '/icon/base/black/arrow-left.webp',
                            media:'(min-width: 320px)',
                        }]
                    }"
                    :label="'close-popup'"
                    :attrs="{
                        iconIsMarginAuto: false
                    }"

                />
                <img
                    loading="lazy"
                    decoding="async"
                    src="/img/logo/logo.webp"
                    alt="Logo Popup"
                    width="160"
                    height="120"
                    format="webp"
                    class='popup-nav-hgroup-title'
                />
                <basic-link 
                    :icon="{
                        image: {
                            src: '/icon/base/black/xmark.webp',
                            alt: 'check icon',
                            width: 30,
                            height: 30,
                            attrs: {
                                needContrast: true
                            }
                        }, 
                        sources: [{
                            srcset: '/icon/base/black/xmark.webp',
                            media:'(min-width: 320px)',
                        }]
                    }"
                    :label="'close-popup'" 
                    :href="`${(this.$route.path)}#`"
                    :attrs="{
                        iconIsMarginAuto: false
                    }"
                    @click.native="hidePopup"
                    class="popup-close"
                />
            </hgroup>
            <section class="popup-nav-content" ref="scrollPopUp">
                <article class="popup-nav-content-nav-inside">
                    <p style="margin-bottom: 1rem; font-size: 1.5rem; font-weight: bold; text-align: center;">
                        {{signInText.title["1"]}} <br> {{signInText.title["2"]}} <br> {{signInText.title["3"]}}
                    </p>

                    <basic-hr-text style="margin-top: 1rem;" :text="'o'" />
                    <a class="email" :href="`${(this.$route.path)}#sign-in`" @click="move('signin')">
                        {{signInText.link["1"]}}
                        <u style="color: blue !important;">
                            {{signInText.link["2"]}}
                        </u>
                    </a>
                    <a class="register" :href="`${(this.$route.path)}#sign-up`" @click="move('signup')">
                        {{signUpText.link["1"]}} 
                        <u style="color: blue !important;">
                            {{signUpText.link["2"]}}
                        </u>
                    </a>
                </article>

                <form @submit.prevent="submitLogin" id="formLogin" class="popup-nav-content-login">
                    <p style="color: #5da9ff">                        
                        {{signInText.form.title}}
                    </p>
                    <basic-input
                        :type="'email'"
                        :placeholder="signInText.form.inputs[1]"
                        :name="'email'"
                        :id="'form-email-login'"
                        :form="'formLogin'"
                    />
                    <basic-input
                        :type="'password'"
                        :placeholder="signInText.form.inputs[2]"
                        :name="'password'"
                        :id="'form-password-login'"
                        :form="'formLogin'"
                    />
                    <basic-button-solid 
                        :type="'submit'"
                        class="shadow rounded w-full"
                        :text="signInText.form.btnText"
                        :attrs="{
                            isBlue: true
                        }"
                    />
                </form>
                
                <form @submit.prevent="submitLogup" id="formLogup" class="popup-nav-content-signup">
                    <p  style="color: #5da9ff;">
                        {{signUpText.title}}
                    </p>
                    <input type="email" style="display: block; margin: 1rem 0; width: 100%;" form="formLogup" :placeholder="signUpText.inputs[1]" name="email" id="form-email-logup">
                    <input type="tel" style="display: block; margin: 1rem 0; width: 100%;" :placeholder="signUpText.inputs[2]" name="phone" id="form-tel-logup">
                    
                    <label style="position: relative; display: block;" for="form-pass-logup">
                        <basic-input
                            :type="'password'"
                            :placeholder="signUpText.inputs[3]"
                            :name="'password'"
                            :id="'form-pass-logup'"
                            :form="'formLogup'"
                            :ref="'form-pass-logup'"
                            @change.native="validPass($event)"
                            style="display: block; margin: 1rem 0; width: 100%;" 
                        />
                        <span @click="showPass('form-pass-logup')" class="icon-show-password" >
                            <basic-image
                                v-if="showedFirstPass"
                                :image="{
                                    src: '/icon/base/black/eye-slash.webp',
                                    alt: 'eye slash icon',
                                    width: 20,
                                    height: 20,
                                    attrs: {
                                        needContrast: true
                                    }
                                }"
                                :sources="[{
                                    srcset: '/icon/base/black/eye-slash.webp',
                                    media:'(min-width: 320px)',
                                }]"
                            />
                            <basic-image
                                v-else
                                :image="{
                                    src: '/icon/base/black/eye.webp',
                                    alt: 'eye icon',
                                    width: 20,
                                    height: 20,
                                    attrs: {
                                        needContrast: true
                                    }
                                }"
                                :sources="[{
                                    srcset: '/icon/base/black/eye.webp',
                                    media:'(min-width: 320px)',
                                }]"
                            />
                        </span>
                    </label>

                    <label style="position: relative; display: block;" for="form-pass-logup">
                        <basic-input
                            :type="'password'"
                            :placeholder="signUpText.inputs[3]"
                            :name="'password_check'"
                            :id="'form-pass-check-logup'"
                            :form="'formLogup'"
                            :ref="'form-pass-check-logup'"
                            @change.native="checkPass($event)"
                            style="display: block; margin: 1rem 0; width: 100%;" 
                        />
                        <span @click="showPass('form-pass-check-logup')" class="icon-show-password" >
                            <basic-image
                                v-if="showedSecondPass"
                                :image="{
                                    src: '/icon/base/black/eye-slash.webp',
                                    alt: 'eye slash icon',
                                    width: 20,
                                    height: 20,
                                    attrs: {
                                        needContrast: true
                                    }
                                }"
                                :sources="[{
                                    srcset: '/icon/base/black/eye-slash.webp',
                                    media:'(min-width: 320px)',
                                }]"
                            />
                            <basic-image
                                v-else
                                :image="{
                                    src: '/icon/base/black/eye.webp',
                                    alt: 'eye icon',
                                    width: 20,
                                    height: 20,
                                    attrs: {
                                        needContrast: true
                                    }
                                }"
                                :sources="[{
                                    srcset: '/icon/base/black/eye.webp',
                                    media:'(min-width: 320px)',
                                }]"
                            />
                        </span>
                    </label>

                    <section style="display: flex; font-size: .85rem;" @change='check("condicion1")'>
                        <basic-input type="checkbox" :text="signUpText.usePrivacy.check1[1]" name="condicion1" id="condicion1" :linkCheckbox="{text:signUpText.usePrivacy.check1[2], link:'about/terms-conditions'}"/>
                    </section>
                    <section style="display: flex; font-size: .85rem; margin: 1rem 0;" @change='check("condicion2")'>
                        <basic-input type="checkbox" :text="signUpText.usePrivacy.check2[1]" name="condicion2" id="condicion2" :linkCheckbox="{text:signUpText.usePrivacy.check2[2], link:'about/privacity'}"/>
                    </section>

                    <basic-button-solid 
                        :type="'submit'" 
                        :disabled="condicion1 == false || condicion2 == false" 
                        class="shadow rounded w-full"
                        :text="signUpText.btnSignup"
                        :attrs="{
                            isBlue: true
                        }"
                    />
                </form>
            </section>
        </nav>
    </section>
</template>

<script>
import {setUserCookies} from '~/utils/cookies/setUser'
import getToken from '~/utils/token/getToken'
import signInText from "~/content/pages/signin/text.json"
import signUpText from '~/content/pages/signup/text.json'

export default {
    data() {
        return {
            showedFirstPass: false,
            showedSecondPass: false,
            condicion1: false,
            condicion2: false,
            signInText: signInText,
            signUpText: signUpText
        }
    },
    methods: {
        restartPopUp() {
            document.querySelector('#btn-back').style.display = 'none',
            document.querySelector('.popup-nav-content-nav-inside').style.zIndex = 1
            document.querySelector('.popup-nav-content-signup').style.zIndex = -1
            document.querySelector('.popup-nav-content-login').style.zIndex = -1
        },
        move(to=null) {
            if(to == 'signin') {
                document.querySelector('#btn-back').style.display = 'block'
                document.querySelector('.popup-nav-content-nav-inside').style.zIndex = -1
                document.querySelector('.popup-nav-content-signup').style.zIndex = -1
                document.querySelector('.popup-nav-content-login').style.zIndex = 1
            }
            else if(to == 'signup') {
                document.querySelector('#btn-back').style.display = 'block'
                document.querySelector('.popup-nav-content-nav-inside').style.zIndex = -1
                document.querySelector('.popup-nav-content-signup').style.zIndex = 1
                document.querySelector('.popup-nav-content-login').style.zIndex = -1
            }
            else {
                this.restartPopUp()
            }
        },
        hidePopup() {

            if(document.body.classList.contains('body-overflow')) {
                document.body.classList.remove('body-overflow')
            }

            this.restartPopUp()

            this.$store.commit('popup/visibility', false)
        },
        onResize() {
            if(this.$store.state.devices.device.isDesktop) {
                this.hidePopup()
            }
        },
        submitLogup: async function() {
            const form = document.querySelector('#formLogup')
            const formData = new FormData(form)

            let isValidPass = this.validPass()
            if(!isValidPass) {
                return
            }

            let token = await getToken(this.$store)
            
            try{
                let data
                if(process.client){
                    data = await this.$axiosAPI.post('sign-up/', formData,
                        token ? { 'Authorization': token } : {}
                    )
                }else{
                    data = await this.$axiosIntern.post('sign-up/', formData,
                        token ? { 'Authorization': token } : {}
                    )
                }
                if(data) {
                    this.$store.commit('auth/user', data)
                    setUserCookies(data)
                    this.hidePopup()
                }
            }catch(error){
                console.log("Error: ", error)
            }
        },
        async submitLogin() {
            let token = getToken(this.$store)
            
            const form = document.querySelector('#formLogin')
            const formData = new FormData(form)

            try{
                let data
                if(process.client){
                    data = await this.$axiosAPI.post('login/', formData,
                        token ? { 'Authorization': token } : {}
                    )
                }else{
                    data = await this.$axiosIntern.post('login/', formData,
                        token ? { 'Authorization': token } : {}
                    )
                }

                console.log(data)

                if(data) {
                    this.$store.commit('auth/user', data)
                    setUserCookies(data)
                    this.hidePopup()
                }
            } catch(error){
                console.log("Error: ", error)
            }
        },
        showPass(id) {
            if(document.querySelector('#'+id).type=='password'){

                document.querySelector('#'+id).type='text'
                id == 'form-pass-logup'
                ? this.showedFirstPass = true
                : this.showedSecondPass = true
            }
            else {
                document.querySelector('#'+id).type='password'
                id == 'form-pass-logup'
                ? this.showedFirstPass = false
                : this.showedSecondPass = false
            }
            
        },
        validPass: function(event=undefined) {
            let regex = [/[0-9]/, /[a-z]/, /[A-Z]/, /(?:[¡!$€_#?¿]{1})/]

            let isValid = regex.map( (expression) => {
                let eventTarget = event ? !event.target?.value?.match(expression) : false

                if(eventTarget || !document.querySelector('#form-pass-logup').value.match(expression)){
                    document.querySelector('#form-pass-logup').setCustomValidity('Las contraseña debe contener al menos 1 minuscula, 1 MAYUSCULA, 1 ¡!$€_#?¿ y 1 número!')
                    document.querySelector('#form-pass-logup').reportValidity()
                    setTimeout(() => {
                        document.querySelector('#form-pass-logup').setCustomValidity('')
                        document.querySelector('#form-pass-logup').reportValidity()
                    }, 3000)
                    return false
                }

                return true
            })

            if(isValid.includes(false)) return false

            return true
        },
        checkPass: function(event) {
            let checked
            if (event) {
                checked = event.target.value == document.querySelector(`input[form="formLogup"][name="password"]`).value
            }
            else {
                checked = document.querySelector(`input[form="formLogup"][name="password_check"]`) == document.querySelector(`input[form="formLogup"][name="password"]`).value
            }

            if(!checked) {
                document.querySelector('#form-pass-logup').setCustomValidity('Las contraseñas no son iguales!')
                document.querySelector('#form-pass-logup').reportValidity()
            }

            return checked
        },
        check(id){
            console.log(document.getElementById(id).checked)
            this[id] = document.getElementById(id).checked
        }
    },
    mounted: function () {
      this.$nextTick(function () {
        this.onResize
      })
      window.addEventListener('resize', this.onResize)
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/components/popup/loginInUp
@import ~/assets/sass/theme/light/color

@keyframes blurActive
    0%
        backdrop-filter: blur(0px)
    100%
        backdrop-filter: blur(5px)

@keyframes popupActive
    0%
        opacity: 0
    100%
        opacity: 1

.icon-show-password
    position: absolute
    right: 10px
    top: 0
    bottom: 0
    display: grid
    justify-content: center
    align-items: center

.blur
    position: absolute
    width: 100vw
    height: 100vh
    top: 0
    left: 0
    right: 0
    bottom: 0
    backdrop-filter: blur(5px)
    z-index: 9
    animation: blurActive
    animation-duration: .5s
    animation-fill-mode: forwards

.label-button
    @apply shadow rounded justify-center
    padding: .5rem .2rem .5rem 0
    margin: .5rem 0
    font-size: .8rem
    letter-spacing: 1px
    display: flex
    color: #fff
</style>
