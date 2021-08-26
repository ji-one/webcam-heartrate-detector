import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
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
