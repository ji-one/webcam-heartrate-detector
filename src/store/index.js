import Vue from "vue";
import Vuex from "vuex";
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({
  // plugins: [createPersistedState()],
  state: {
    login: false,
    username: "",
    token: null,
    avgBPM: [],
    alertDialogToggle: false,
    alertDialogInfo: null,
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
    openAlertDialog(state, payload) {
      state.alertDialogInfo = payload
      state.alertDialogToggle = true
    },
    closeAlertDialog(state) {
      state.alertDialogInfo = null
      state.alertDialogToggle = false
    },
  },
  actions: {
  },
  modules: {},
});
