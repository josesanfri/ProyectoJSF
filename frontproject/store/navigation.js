export const state = () => ({
    show: false
})

export const mutations = {
    visibility(state, status) {
        state.show = status
    }
}