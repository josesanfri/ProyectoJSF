<template>
    <form id="contactForm" @submit.prevent="onSubmit" class="form-web-contact">
        <basic-text-title v-if="title" :title="title" />

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

        <section class="form-web-contact-section" @change="check('condicion1')">
            <basic-input
                type="checkbox"
                :text="formContact.usePrivacy.check1[1]"
                name="condicion1"
                id="condicion1"
                :linkCheckbox="{
                    text: formContact.usePrivacy.check1[2],
                    link: 'about/terms-conditions',
                }"
            />
        </section>

        <section class="form-web-contact-section" @change="check('condicion2')">
            <basic-input
                type="checkbox"
                :text="formContact.usePrivacy.check2[1]"
                name="condicion2"
                id="condicion2"
                :linkCheckbox="{
                    text: formContact.usePrivacy.check2[2],
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
import getToken from "~/utils/token/getToken";
import formContact from "~/content/components/form/contact.json";

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
            formContact: formContact,
            condicion1: false,
            condicion2: false,
        };
    },
    methods: {
        async onSubmit() {
            try {
                const form = document.querySelector("#contactForm");
                const formContact = new FormData(form);

                let token = await getToken(this.$store);
                let data;
                try {
                    if (process.client) {
                        data = await this.$axiosAPI.post("lead/contact/create/", formContact,
                            token ? { 'Authorization': token } : {}
                        );

                        
                    } else {
                        data = await this.$axiosIntern.post("lead/contact/create/", formContact,
                            token ? { 'Authorization': token } : {}
                        );

                    
                    }

                    let toTop = document.querySelector("#toTop");
                    if (toTop) {
                        toTop.click();
                    }
                } catch (error) {
                    console.log("Error: ", error);
                }
            } catch {
                this.$router.push("/error/ups/");
            }
        },
        check(id) {
            this[id] = document.getElementById(id).checked;
        },
    },
};
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints

.form-web-contact
    @apply grid grid-cols-1 gap-4 p-8 auto-rows-auto

    @media ( min-width: $large-screen)
        @apply grid-cols-2

    &-section
        @apply flex items-center

.grid-long
    @apply col-span-full
</style>
