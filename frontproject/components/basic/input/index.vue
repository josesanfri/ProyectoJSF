<template>
    <label
        :for="id"
        class="basic-label"
        data-hide-during-focus="false"
        :class="{
            column: attrs.flexColumn,
            bold: attrs.isBold,
            'text-white': attrs.textWhite,
            'flex-checkbox': attrs.flexCheckbox,
        }"
    >
        <template v-if="type == 'checkbox'">
            <input
                class="basic-input-checkbox__input"
                :type="type"
                :name="name"
                :id="id"
                :checked="checked"
                :form="form"
                :tabindex="tabIndex"
                style="cursor: pointer"
            />
            <basic-image
                v-if="icon"
                :image="icon.image"
                :sources="icon.sources"
            />
            <template v-if="linkCheckbox.text">
                <div>
                    {{ text }} <nuxt-link :to="'/'+linkCheckbox.link">{{linkCheckbox.text}}</nuxt-link>
                </div>
            </template>
            <template v-else>
                {{ text }}
            </template>
        </template>

        <template v-else-if="type == 'select'">
            {{ text }}
            <select
                data-hide-during-focus="false"
                class="basic-select"
                :id="id"
                :name="name"
                :form="form"
                :tabindex="tabIndex"
                :disabled="readOnly" 
            >
                <option v-for="(item, index) in items" :key="index" :value="item.value">{{ item.text }}</option>
            </select>
        </template>

        <template v-else-if="type == 'file'">
            {{ text }}
            <input
                data-hide-during-focus="false"
                class="basic-input"
                :type="type"
                :placeholder="placeholder"
                :name="name"
                :id="id"
                :ref="id"
                :form="form"
                :list="datalist.list_id"
                :value="''"
                :tabindex="tabIndex"
                style="cursor: pointer"
            />
        </template>

        <template v-else-if="type == 'date'">
            {{ text }}
            <vc-date-picker 
                color="blue"
                :model-config="{type: 'string', mask: 'MM/DD/YYYY'}"
                class="basic-input date"
                :popover="{ visibility: 'click' }"
            >
                <template  v-slot="{ inputValue, inputEvents }">
                    <input
                        autocomplete="off"
                        :value="inputValue"
                        v-on="inputEvents"
                        :placeholder="placeholder"
                        :name="name"
                        :form="form"
                    />
                    <basic-image 
                        :image=" {
                            src: '/icon/base/black/calendar-days.webp',
                            alt: 'chevron up icon',
                            width: 20,
                            height: 20,
                            attrs: {
                                needContrast: true
                            }
                        }"
                        :sources=" [{
                            srcset: '/icon/base/black/calendar-days.webp',
                            media:'(min-width: 320px)',
                        }]"       
                    />
                </template>
            </vc-date-picker>
        </template>

        <template v-else-if="type == 'time'">
            {{ text }}
            <vc-date-picker 
                color="blue"
                mode="time"
                is24hr
                :valid-hours="{ min: 13, max: 23 }"
                :minute-increment="15"
                class="basic-input date"
            >
                <template  v-slot="{ inputValue, inputEvents }">
                    <input
                        autocomplete="off"
                        :value="inputValue"
                        v-on="inputEvents"
                        :placeholder="placeholder"
                        :name="name"
                        :form="form"
                    />
                </template>
            </vc-date-picker>
        </template>

        <template v-else-if="type == 'textarea'">
            {{ text }}
            <textarea
                data-hide-during-focus="false"
                class="basic-input-textarea"
                :placeholder="placeholder"
                :name="name"
                :id="id"
                :form="form"
                :value="value"
                :tabindex="tabIndex"
                inputmode="text"
            >
            </textarea>
        </template>

        <template v-else>
            {{ text }}
            <input
                data-hide-during-focus="false"
                inputmode="text"
                class="basic-input"
                :type="type"
                :placeholder="placeholder"
                :name="name"
                :id="id"
                :ref="id"
                :form="form"
                :list="datalist.list_id"
                :value="value"
                :tabindex="tabIndex"
                :readonly="readOnly"
            />
            <datalist v-if="datalist.items" :id="datalist.list_id">
                <template v-for="item in datalist.items">
                    <option :key="item.value" :value="item.value">
                        {{ item.value }}
                    </option>
                </template>
            </datalist>
        </template>
    </label>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            required: true,
        },
        placeholder: {
            type: String,
            required: false,
            default: "",
        },
        name: {
            type: String,
            required: true,
        },
        id: {
            type: String,
            required: false,
        },
        checked: {
            type: Boolean,
            required: false,
        },
        value: {
            type: String,
            required: false,
            default: "",
        },
        icon: {
            type: Object,
            required: false,
        },
        text: {
            type: String,
            required: false,
        },
        tabIndex: {
            type: Number,
            required: false,
            default: 0,
        },
        attrs: {
            type: Object,
            required: false,
            default: () => ({
                flexColumn: false,
                isBold: false,
                flexCheckbox: false,
            }),
        },
        readOnly: {
            type: Boolean,
            required: false,
            default: false

        },
        form: {
            type: String,
            required: false,
            default: "",
        },
        items: {
            type: Array,
            required: true
        },
        datalist: {
            type: Object,
            required: false,
            default: () => ({
                list_id: "",
            }),
        },
        linkCheckbox: {
            type: Object,
            required: false,
            default: () => ({})
        }
    },
    data() {
        return {
            showedPass: false,
            date: ''
        };
    },
    methods: {},
};
</script>

<style lang="sass" scoped>
    @import ~/assets/sass/components/basics/input/input
    @import ~/assets/sass/theme/light/color
    @import ~/assets/sass/components/basics/button/base

    .select
        @include btn
        @apply shadow appearance-none border rounded py-2 px-3 leading-tight bg-white focus:outline-none focus:bg-gray-200

    .column
        @apply flex-col

    .bold
        @include font-bold

    .basic
        &-input
            @include input-text
            @apply pt-2
            width: 100%

            &-textarea
                @include input-text
                @apply pt-2
                width: 100%
            &-width
                width: fit-content !important

        &-label
            @apply flex
            position: relative
            cursor: pointer

        &-select
            @include color-gray-dark
            @include input-text
            @apply cursor-pointer
            width: 100%

    .icon-check
        @apply w-4 h-4

    .basic-input-checkbox
        display: flex

        &__input
            @include input-check
            margin: auto .5rem

    .date
        display: flex
        justify-content: space-between
        align-items: center
        input
            outline: none
            width: 100%
            
</style>
