<template>
    <section class="min-height">
        <section class="menu-section">
            <basic-text-title
                :title="{
                    text:`${menuData.name}`,
                    attrs: {
                        textXl: true
                    }
                }" 
            />
            <article class="menu-article">
                <basic-text-title
                    :title="{
                        text:`Entrantes`,
                        attrs: {
                            textXl: true
                        }
                    }" 
                />
                <ul>
                    <li class="menu-li" v-for="starter in starters" :key="starter.id">
                        <basic-text-paragraph
                            :text="`${ starter.name } - ${ starter.price }€`"
                        />
                        <basic-text-paragraph
                            :text="`${ starter.ingredients }`"
                        />
                    </li>
                </ul>
            </article>
            <article class="menu-article">
                <basic-text-title
                    :title="{
                        text:`Principales`,
                        attrs: {
                            textXl: true
                        }
                    }" 
                />
                <ul>
                    <li class="menu-li" v-for="main in mains" :key="main.id">
                        <basic-text-paragraph
                            :text="`${ main.name } - ${ main.price }€`"
                        />
                        <basic-text-paragraph
                            :text="`${ main.ingredients }`"
                        />
                    </li>
                </ul>
            
            </article>
            <article class="menu-article">
                <basic-text-title
                    :title="{
                        text:`Postres`,
                        attrs: {
                            textXl: true
                        }
                    }" 
                />
                <ul>
                    <li class="menu-li" v-for="dessert in desserts" :key="dessert.id">
                        <basic-text-paragraph
                            :text="`${ dessert.name } - ${ dessert.price }€`"
                        />
                        <basic-text-paragraph
                            :text="`${ dessert.ingredients }`"
                        />
                    </li>
                </ul>
            </article>
        </section>
    </section>
</template>

<script>
import getToken from '~/utils/token/getToken'

export default {
    data() {
        return {
            menuData: {},
            allPlates: [],
            starters: [],
            mains: [],
            desserts: [],
        }
    },
    async mounted() {
        let token = await getToken(this.$store)

        /* GET THIS MENU DATA */
        try {
            let getMenu
            if(process.client){
                getMenu = await this.$axiosAPI.get(`menu/${this.$route.params.id}`,
                    token ? { 'Authorization': token } : {}
                )
                .then((getMenu) => (this.menuData = getMenu.data));
            } else {
                getMenu = await this.$axiosIntern.get(`menu/${this.$route.params.id}`,
                    token ? { 'Authorization': token } : {}
                )
                .then((getMenu) => (this.menuData = getMenu.data));
            }
            
        } catch (error) {
            console.log(error)
        }

        /* GET ALL PLATES DATA */
        try {
            let getPlates
            if(process.client){
                getPlates = await this.$axiosAPI.get("plate/",
                    token ? { 'Authorization': token } : {}
                )
                .then((getPlates) => (this.allPlates = getPlates.data.results));
            } else {
                getPlates = await this.$axiosIntern.get("plate/",
                    token ? { 'Authorization': token } : {}
                )
                .then((getPlates) => (this.allPlates = getPlates.data.results));
            }
        } catch (error) {
            console.log(error)
        }

        let starterIds = this.menuData.starter
        let mainIds = this.menuData.main
        let dessertIds = this.menuData.dessert

        this.starters = this.allPlates.filter(plate => starterIds.includes(plate.id))
        this.mains = this.allPlates.filter(plate => mainIds.includes(plate.id))
        this.desserts = this.allPlates.filter(plate => dessertIds.includes(plate.id))
    },  
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.min-height
    min-height: 65vh

.menu
    &-section
        @include bg-primary
        @apply p-8 flex flex-col

    &-li
        @apply flex flex-col gap-2 pb-2 pt-2
        border-bottom: 1px solid black
</style>