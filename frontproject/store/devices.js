export const state = () => ({
    device: {},
    bot: false
})

export const mutations = {
    setDevice(state, value){
        state.device = value
    },
    setBot(state, value) {
        state.bot = value
    }
}