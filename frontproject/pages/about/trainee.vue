<template>
    <section>
        <!-- Section form -->
        <section class="trainee-form-section">
            <basic-text-title :title="textTrainee.request.title" />
            <form-work
                :title="formWork.title"
                :inputs="formWork.inputs"
                :submit="formWork.submit"
            />
        </section>

        <!-- Section info -->
        <section class="trainee-info-section">
            <!-- Article spanish -->
            <article class="trainee-info-article">
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.info.title"
                    :paragraph="textTrainee.info.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.responsable.title"
                    :paragraph="textTrainee.responsable.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.purpose.title"
                    :paragraph="textTrainee.purpose.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.data.title"
                    :paragraph="textTrainee.data.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.legitimation.title"
                    :paragraph="textTrainee.legitimation.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.addressee.title"
                    :paragraph="textTrainee.addressee.paragraph"
                />
                <card-info
                    class="trainee-info-card"
                    :title="textTrainee.rights.title"
                    :paragraph="textTrainee.rights.paragraph"
                />
            </article>

        </section>
    </section>
</template>

<script>
import textTrainee from "~/content/pages/about/trainee/text.json";
import formWork from "~/content/components/form/work.json";

export default {
    async asyncData() {
        return {
            textTrainee: textTrainee,
            formWork: formWork,
        };
    },
    head() {
        return {
            titleTemplate: "%s Haz prácticas con nosotros",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Quieres hacer prácticas en La Esquina Gourmet? Aquí encontraras información y un formulario. Mucha Suerte, te estamos esperando!",
                },
            ]
        };
    },
};
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.trainee
    &-form-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20

    &-info-section
        @include bg-gray-soft
        @apply grid p-8
        grid-template-columns: 1fr
        gap: 1rem

        @media ( min-width: $large-screen)
            @apply px-20
            gap: 5rem

    &-info-card
        @apply py-4
</style>
