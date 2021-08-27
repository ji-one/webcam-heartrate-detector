import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  plugins: [createPersistedState()],
  state: {
    login: false,
    username: "",
    token: null,
  },
  mutations: {
    get_token(state, token) {
      state.login = true;
      state.username = token.username;
    },
    del_token(state) {
      state.login = false;
      state.username = "";
      sessionStorage.clear();
    },
  },
  actions: {},
  modules: {},
});
