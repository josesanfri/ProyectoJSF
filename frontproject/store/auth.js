export const state = () => ({
	isLoggedIn: false,
	user: {},
	type: "",
});

export const mutations = {
	user(state, user) {
		state.isLoggedIn = !!user;
		state.user = user || {};
		state.type = user.user_type || "";
	},
	logout(state) {
		state.isLoggedIn = false;
		state.user = {};
		state.type = "";
	},
};

export const getters = {
	getUser: (state) => {
		return state.user;
	},
	getToken: (state) => {
		return state.user?.token;
	},
};

export const strict = false;
