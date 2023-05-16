import Vue from 'vue'
import VCalendar from 'v-calendar'

Vue.use(VCalendar, {
    componentPrefix: 'vc',
    masks: { input: "YYYY-MM-DD", data: "YYYY-MM-DD" }
})
