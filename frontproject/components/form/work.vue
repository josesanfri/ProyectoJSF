<template>
    <form id="workForm" class="form-web-work" @submit.prevent="onSubmit">
        <basic-input
            v-for="input in inputs"
            :key="input.id"
            :text="input.text"
            :type="input.type"
            :placeholder="input.placeholder"
            :name="input.name"
            :id="input.id"
            :attrs="input.attrs"
            :form="input.form"
            :class="{ 'grid-long': input.attrs.isLong }"
        />

        <section class="form-web-work-section" @change="check('condicion1')">
            <basic-input
                type="checkbox"
                :text="formWork.usePrivacy.check1[1]"
                name="condicion1"
                id="condicion1"
                :linkCheckbox="{
                    text: formWork.usePrivacy.check1[2],
                    link: 'about/terms-conditions',
                }"
            />
        </section>

        <section class="form-web-work-section" @change="check('condicion2')">
            <basic-input
                type="checkbox"
                :text="formWork.usePrivacy.check2[1]"
                name="condicion2"
                id="condicion2"
                :linkCheckbox="{
                    text: formWork.usePrivacy.check2[2],
                    link: 'about/privacity',
                }"
            />
        </section>

        <basic-button-solid
            :disabled="condicion1 == false || condicion2 == false"
            :class="{ 'grid-long': submit.attrs.isLong }"
            :type="submit.type"
            :text="submit.text"
            :attrs="submit.attrs"
        />
    </form>
</template>

<script>
import getToken from '~/utils/token/getToken';
import formWork from "~/content/components/form/work.json";

export default {
    props: {
        title: {
            type: Object,
            required: false,
        },
        inputs: {
            type: Array,
            required: true,
        },
        submit: {
            type: Object,
            required: true,
        },
    },
    data() {
        return {
            formWork: formWork,
            condicion1: false,
            condicion2: false,
        };
    },
    methods: {
        async onSubmit() {
            try {
                const form = document.querySelector('#workForm')
                const formWork = new FormData(form);

                if(this.$route.path != '/about/trainee/'){
                    formWork.append("type_job", "J")
                } else {
                    formWork.append("type_job", "I")
                }

                let file = document.getElementById('user_curriculum').value;
                let allowedExtensions = /(\.pdf)$/i

                let token = await getToken(this.$store)
                let data

                if(!allowedExtensions.exec(file)){
                    alert('Solo se acepta pdf');
                } else {
                    try{
                        if(process.client){
                            data = await this.$axiosAPI.post("lead/job/create/", formWork,
                                token ? { 'Authorization': token } : {}
                            );
                        }else{
                            data = await this.$axiosIntern.post("lead/job/create/", formWork,
                                token ? { 'Authorization': token } : {}
                            );
                        }

                        let toTop = document.querySelector('#toTop')
                        if(toTop) {
                            toTop.click()
                        }
                    } catch(error){
                        console.log("Error: ", error)
                    }
                }

            } catch {
                this.$router.push('/error/ups/')
            }
        },
        check(id) {
            this[id] = document.getElementById(id).checked;
        }
    }
};
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints

.form-web-work
    @apply grid grid-cols-1 gap-4 auto-rows-auto p-4 items-center
    grid-template-columns: 1fr
    grid-auto-rows: auto
    gap: 1rem

    @media ( min-width: $large-screen)
        grid-template-columns: repeat(2, 1fr)

    &-section
        @apply flex items-center

.grid-long
    grid-column: 1 / -1
</style>
