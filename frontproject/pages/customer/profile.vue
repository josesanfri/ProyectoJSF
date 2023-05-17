<template>
    <section class="min-height">
        <basic-text-title
            class="cover-title"
            :title="formCustomerProfile.cover.title" 
        />
        
        <article class="renter-profile-section">
            <form-profile
                :profile="formCustomerProfile.profile"
                :address="formCustomerProfile.address"
                :submit="formCustomerProfile.submit"
                :morePersonal="formCustomerProfile.morePersonal"
            />
        </article>
    </section>
</template>

<script>
import formCustomerProfile from '~/content/components/form/profile.json'

export default {
    async asyncData(){
        return{
            formCustomerProfile: formCustomerProfile
        }
    },
    head() {
        return {
            titleTemplate: '%s Mi perfil',
            meta: [
                {
                    hid: 'description',
                    name: 'description',
                    content: 'My profile'
                }
            ]
        }
    }
}
</script>

<style lang="sass">
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.min-height
    min-height: 65vh

.cover-title
    @include bg-gray-soft 
    @apply border-b-2 border-gray-400 text-center pt-20

    @media ( min-width: $large-screen)
        @apply text-left pl-12

.renter-profile
    &-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20
</style>