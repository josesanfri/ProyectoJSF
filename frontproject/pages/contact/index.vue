<template>
    <section class="min-height">
        <section class="contact">
            <form-contact
                :inputs="formContact.inputs"
                :submit="formContact.submit"
            />
        </section>
    </section>
</template>

<script>
import formContact from "~/content/components/form/contact.json";

export default {
    async asyncData() {
        return {
            formContact: formContact
        };
    },
    head() {
        return {
            titleTemplate: "%s Contacto",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Contacta con La Esquina Gourmet!",
                },
            ]
        };
    }
};
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints

.min-height
    min-height: 65vh

.contact
    @apply grid grid-cols-1
</style>
