// store.js
import { createStore } from 'vuex';

export default createStore({
  state: {
    userRole: "hr", // Initially, the user role is null
  },
  mutations: {
    setUserRole(state, role) {
      state.userRole = role;
    },
  },
  actions: {
    login({ commit }, userData) {
      // Assuming you have an API call to authenticate the user
      // After successful login, set the user's role
      const role = userData.role; // Replace with actual role data from the API
      commit('setUserRole', role);
    },
  },
  getters: {
    getUserRole(state) {
      return state.userRole;
    },
  },
});
