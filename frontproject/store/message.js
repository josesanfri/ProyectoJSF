export const state = () => ({
  	items: {},
});

export const mutations = {
	addItem(state, status) {
		let { reference, ...data } = status;
		this._vm.$set(state.items, reference, data);
	},
	removeItem(state, status) {
		this._vm.$delete(state.items, status);
	},
	resetItems(state) {
		state.items = {};
	},
};

export const getters = {
    getMessages: (state) => {
      	return state.items;
    },
};
