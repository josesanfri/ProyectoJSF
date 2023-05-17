<template>
    <section>
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
                <ul v-for="starter in starters" :key="starter.id">
                    <li>
                        {{ starter.name }} - {{ starter.price }} <br>
                        {{ starter.ingredients }}
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
                <ul v-for="main in mains" :key="main.id">
                    <li>
                        {{ main.name }} - {{ main.price }} <br>
                        {{ main.ingredients }}
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
                <ul v-for="dessert in desserts" :key="dessert.id">
                    <li>
                        {{ dessert.name }} - {{ dessert.price }} <br>
                        {{ dessert.ingredients }}
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
            console.log("platos:", this.allPlates)
        } catch (error) {
            console.log(error)
        }

        let starterIds = this.menuData.starter
        let mainIds = this.menuData.main
        let dessertIds = this.menuData.dessert

        this.starters = this.allPlates.filter(plate => starterIds.includes(plate.id))
        this.mains = this.allPlates.filter(plate => mainIds.includes(plate.id))
        this.desserts = this.allPlates.filter(plate => dessertIds.includes(plate.id))

        console.log("entrantes:", this.starters)
        console.log("principales:", this.mains)
        console.log("postres:", this.desserts)
    },  
}
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.menu
    &-section
        @include bg-primary
        @apply p-8 flex flex-col
</style>