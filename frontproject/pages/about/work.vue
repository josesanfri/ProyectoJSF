<template>
    <section>
        <!-- Section form -->
        <section class="work-form-section">
            <basic-text-title :title="textWork.request.title" />
            <form-work
                :title="formWork.title"
                :inputs="formWork.inputs"
                :submit="formWork.submit"
            />
        </section>
        <!-- Section info -->
        <section class="work-info-section">
            <article class="work-info-article">
                <card-info
                    class="work-info-card"
                    :title="textWork.info.title"
                    :paragraph="textWork.info.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.responsable.title"
                    :paragraph="textWork.responsable.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.purpose.title"
                    :paragraph="textWork.purpose.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.data.title"
                    :paragraph="textWork.data.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.legitimation.title"
                    :paragraph="textWork.legitimation.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.addressee.title"
                    :paragraph="textWork.addressee.paragraph"
                />
                <card-info
                    class="work-info-card"
                    :title="textWork.rights.title"
                    :paragraph="textWork.rights.paragraph"
                />
            </article>

        </section>
    </section>
</template>

<script>
import textWork from "~/content/pages/about/work/text.json";
import formWork from "~/content/components/form/work.json";

export default {
    async asyncData() {
        return {
            textWork: textWork,
            formWork: formWork,
        };
    },
    head() {
        return {
            titleTemplate: "%s Trabaja con nosotros",
            meta: [
                {
                    hid: "description",
                    name: "description",
                    content: "Información sobre como trabajar en La Esquina Gourmet. El mejor ambiente laboral y empresarial, no te lo pierdas!",
                },
            ]
        };
    },
};
</script>

<style lang="sass" scoped>
@import ~/assets/sass/utils/breakpoints
@import ~/assets/sass/theme/light/color

.work
    &-form-section
        @include bg-gray-soft
        @apply p-8

        @media ( min-width: $large-screen)
            @apply px-20

    &-info-section
        @include bg-gray-soft
        @apply grid grid-cols-1 gap-4 p-8

        @media ( min-width: $large-screen)
            @apply px-20
            gap: 5rem

    &-info-card
        @apply py-4
</style>
