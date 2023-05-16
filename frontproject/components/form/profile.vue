<template>
    <form id="profileForm" @submit.prevent="onSubmit">
        <section class="custaccount-section-main">
            <!-- Foto perfil -->
            <picture class="custaccount-section-main-img">
                <label for="customer_img">
                    <nuxt-img loading="lazy" decoding="async" class="m-auto" :src="resProfile.image ? resProfile.image : 'img/logo/default.avif'" alt="Image profile">
                    <input type="file" name="customer_img" id="customer_img" class="customer-photo" style="display: none;">
                </label>
            </picture>
            <!-- Datos personales -->
            <ul class="custaccount-section-main-list">
                <li
                    v-for="input in profile.main.inputs"
                    :key="input.id"
                    class="custaccount-section-main-list-inputs"
                    :class="{'grid-long': input.attrs.isLong}"
                >
                    <basic-input
                        :text="input.text"
                        :type="input.type"
                        :placeholder="input.placeholder"
                        :name="input.name"
                        :attrs="input.attrs"
                        :form="input.form"
                        :id="input.id"
                        :value="resProfile[input.name] ? resProfile[input.name] : ''"
                    />
                </li>
            </ul>
        </section>
        
        <details class="custaccount-details">
            <summary class="custaccount-summary">
                {{address.title.text}}
            </summary>
            <!-- Domicilio -->
            <ul class="custaccount-details-list">
                <li
                    v-for="input in address.inputs"
                    :key="input.id"
                    :class="{'grid-long': input.attrs.isLong}"
                >
                    <basic-input
                        :text="input.text"
                        :type="input.type"
                        :placeholder="input.placeholder"
                        :name="input.name"
                        :attrs="input.attrs"
                        :form="input.form"
                        :id="input.id"
                        :class="{'grid-long': input.attrs.isLong}"
                        :value="resProfile[input.name] ? resProfile[input.name] : ''"
                    />
                </li>
            </ul>
        </details>
        
        <details class="custaccount-details">
            <summary class="custaccount-summary">
                {{morePersonal.title}}
            </summary>
                    
            <!-- Extra info -->
            <section>
                <basic-text-title
                    v-if="profile.about" 
                    :title="profile.about.title"
                    :attrs="profile.about.title.attrs"
                />
                <ul class="custaccount-details-list">
                    <li
                        v-for="input in profile.genre.inputs"
                        :key="input.id"
                        :class="{'grid-long': input.attrs.isLong}"
                        class="py-2"
                    >
                        <basic-input
                            :text="input.text"
                            :type="input.type"
                            :placeholder="input.placeholder"
                            :name="input.name"
                            :attrs="input.attrs"
                            :form="input.form"
                            :id="input.id"
                            :class="{'grid-long': input.attrs.isLong}"
                            :value="resProfile[input.name] ? resProfile[input.name] : ''"
                        />
                    </li>
                </ul>
            </section>
        </details>
    
        <basic-button-solid
            class="w-full"
            :type="submit.type"
            :text="submit.text"
            :attrs="submit.attrs"
        />
        <form id="addressForm" style="display: none;"></form>
    </form>
</template>

<script>
import getToken from '~/utils/token/getToken'

export default {
    data() {
        return { 
            resProfile: {},
        }
    },
    async mounted() {
        let token = await getToken(this.$store)
        const user = this.$store.state.auth.user
        
        /* GET CUSTOMER PROFILE */
        try{
            if(process.client){
                let response = await this.$axiosAPI.get(`profile/user/${user.user_id}/`,
                    token ? { 'Authorization': token } : {}
                ).then( res => {

                    let {address, ...data} = res.data
                    Object.keys(address).forEach( element => data[element] = address[element] )
                    return data

                })
            } else {
                let response = await this.$axiosIntern.get(`profile/user/${user.user_id}/`,
                    token ? { 'Authorization': token } : {}
                ).then( res => {

                    let {address, ...data} = res.data
                    Object.keys(address).forEach( element => data[element] = address[element] )
                    return data

                })
            }
            
            this.resProfile = response

        } catch(error){
            console.log("Error: ", error)
            this.resProfile = {}
        }

        document.getElementById('customer_gender').addEventListener('change', this.other_genre)
        this.other_genre()
    },
    methods: {
        async onSubmit() {
            let token = await getToken(this.$store)

            let profileForm = document.querySelector('#profileForm')
            let addressForm = document.querySelector('#addressForm')

            const formProfile = new FormData(profileForm)
            const formAddress = new FormData(addressForm)

            formAddress.set('zone', 2)
            formProfile.set('address', JSON.stringify(Object.fromEntries(formAddress)))
            formProfile.append('user', parseInt(this.$store.state.auth.user.user_id))

            console.log("formProfile: ", formProfile)

            let data
            if( Object.keys(this.resProfile).length == 0 ) {
                data = await this.$axiosAPI.post( 'profile/user/', formProfile,
                    token ? { 'Authorization': token } : {}
                )
            } 
            else {
                data = await this.$axiosAPI.put( `profile/user/${this.$store.state.auth.user.user_id}/`, formProfile,
                    token ? { 'Authorization': token } : {}
                )
            }
            
            let {address, ...newData} = data
            Object.keys(address).forEach( element => newData[element] = address[element] )
            this.resProfile = newData

            let toTop = document.querySelector('#toTop')
            if(toTop) {
                toTop.click()
            }
        },
        other_genre(){
            if ( ['M','F'].includes( document.getElementById('customer_gender').value ) ){
                document.querySelector('label[for="customer_gender_other"]').style.display = 'none'
            }
            else {
                document.querySelector('label[for="customer_gender_other"]').style.display = 'grid'
            }
        }
    },
    props: {
        profile: {
            type: Object,
            required: false
        },
        address: {
            type: Object,
            required: false
        },
        submit: {
          type: Object,
          required: true
        },
        morePersonal: {
            type: Object,
            required: true
        }
    }
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color
@import ~/assets/sass/components/basics/text/paragraph/paragraph
@import ~/assets/sass/components/basics/input/input

.basic-input
    @include input-text
    @apply pt-2 w-full

.grid-long
    grid-column: 1 / -1

.d-none
    display: none

.visible
    display: flex
    flex-direction: column
    position: relative
    width: 100%

.custaccount
    &-details
        @include border-gray-light
        @apply shadow rounded p-4 my-2
        background: #fff

        &-list
            @apply grid
            gap: 1rem
            grid-template-columns: 1fr

            @media ( min-width: $tablet-min)
                grid-template-columns: repeat(2, 1fr)

    &-summary
        @apply items-center rounded justify-center font-semibold cursor-pointer

    &-article
        &-options
            @apply grid items-center py-2
            grid-template-columns: 1fr
            gap: 1rem

            @media ( min-width: $tablet-min)
                grid-template-columns: repeat(3, 1fr)

        &-occupation
            @apply grid items-center py-2
            grid-template-columns: 1fr
            gap: 1rem

            @media ( min-width: $tablet-min)
                grid-template-columns: repeat(2, 1fr)

    &-section
        &-checkbox
            &-list
                @apply grid
                grid-template-columns: 1fr
                gap: 1rem

                @media ( min-width: $tablet-min)
                    grid-template-columns: repeat(4, 1fr)

            &-label
                @apply inline-flex justify-center items-center cursor-pointer
                gap: .5rem

        &-main
            @include border-gray-light
            @include bg-white
            @apply shadow rounded border grid p-4 my-2
            min-width: 100%
            min-height: 100px
            grid-template-rows: auto
            grid-template-columns: 1fr
            gap: .5rem

            @media ( min-width: $tablet-min)
                grid-template-columns: repeat(2, 1fr)

            &-img
                width: max-content
                height: max-content
                align-self: center
                justify-self: center

                @media ( min-width: $tablet-min)
                    grid-column: 1 / 2
                    grid-row: 1 / -1

                ::v-deep label img
                    margin: auto

            &-list 
                @apply grid
                grid-template-columns: 1fr
                grid-template-rows: repeat(3, auto)
                gap: .5rem 1.5rem

                @media ( min-width: $tablet-min)
                    grid-template-columns: auto 1fr
                
                &-inputs
                    @apply grid
                    
                    label
                        ::v-deep select
                            text-align: left !important
                    
                    input
                        padding: .25rem
                        border-radius: 4px
</style>