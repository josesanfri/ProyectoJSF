<template>
    <ul class="list">
        <li class="list-title" v-if="title">
            <basic-text-paragraph
                :text="title.text"
                :attrs="title.attrs"
            />
            <br>
            <basic-text-paragraph
                :text="title.subtitle.text"
                :attrs="title.subtitle.attrs"
            />
        </li>

        <li class="list-contact" v-for="item in items" :key="item.id">
            <ul class="list-office">
                <li class="list-fields">
                    <basic-link-a
                        class="mx-1 items-center"
                        style="min-width: 20px; min-height: 20px"
                        :text="item.location" 
                        :label="item.locationLabel" 
                        :href="item.locationLink"
                        :attrs="item.attrs"
                        :icon="{
                            image: {
                                src: '/icon/base/white/location-dot.webp',
                                alt: 'location icon',
                                width: 20,
                                height: 20,
                                attrs: {
                                    noWHauto: true,
                                    needContrast: true
                                }
                            }, 
                            sources: [{
                                srcset: '/icon/base/white/location-dot.webp',
                                media:'(min-width: 320px)',
                            }]
                        }"
                        :newTab="true"
                    />
                </li>

                <li class="list-fields">
                    <basic-link-a
                        class="mx-1 items-center"
                        :text="item.phone" 
                        :label="item.phoneLabel" 
                        :href="item.phoneLink"
                        :attrs="item.attrs"
                        :icon="{
                            image: {
                                src: '/icon/base/white/phone.webp',
                                alt: 'phone icon',
                                width: 20,
                                height: 20,
                                attrs: {
                                    needContrast: true
                                }
                            }, 
                            sources: [{
                                srcset: '/icon/base/white/phone.webp',
                                media:'(min-width: 320px)',
                            }]
                        }"
                        :newTab="true"
                    />
                </li>

                <li class="list-fields">
                    <basic-link-a
                        class="mx-1 items-center"
                        :text="item.email" 
                        :label="item.emailLabel" 
                        :href="item.emailLink"
                        :attrs="item.attrs"
                        :icon="{
                            image: {
                                src: '/icon/base/white/envelope.webp',
                                alt: 'mail icon',
                                width: 20,
                                height: 20,
                                attrs: {
                                    needContrast: true
                                }
                            }, 
                            sources: [{
                                srcset: '/icon/base/white/envelope.webp',
                                media:'(min-width: 320px)',
                            }]
                        }"
                        :newTab="true"                        
                    />
                </li>

                <li class="list-fields">
                    <basic-link-a
                        class="mx-1 items-center"
                        :text="item.whatsapp" 
                        :label="item.whatsappLabel" 
                        :href="item.whatsappLink"
                        :attrs="item.attrs"
                        :icon="{
                            image: {
                                src: '/icon/base/white/whatsapp.webp',
                                alt: 'whatsapp icon',
                                width: 20,
                                height: 20,
                                attrs: {
                                    needContrast: true
                                }
                            }, 
                            sources: [{
                                srcset: '/icon/base/white/whatsapp.webp',
                                media:'(min-width: 320px)',
                            }]
                        }"
                        :newTab="true"
                    />
                </li>
            </ul>
        </li>
    </ul>
</template>

<script>
export default {
    props: {
        title: {
            type: Object,
            required: false
        },
        items: {
            type: Array,
            required: true
        }
    },
}
</script>

<style lang="sass" scoped>  
    .list
        @apply flex flex-col gap-4
    
    .list-field
        padding: .1rem 0 0 .1rem
</style>