// store.js
import { createStore } from 'vuex';

export default createStore({
    state: {
        isLoggedIn: false,
        // userRole: "hr", // temp set as "hr"
        // userId: 1, // temp set as 1
        userRole: null, // temp set as "hr"
        userId: null, // temp set as 1
    },
    mutations: {
        setIsLoggedIn(state, status) {
            state.isLoggedIn = status;
        },

        setUserRole(state, role) {
            state.userRole = role;
        },

        setUserId(state, id) {
            state.userId = id;
        },
    },
    actions: {
        async authenticate({ commit }, userData) {

            var login_url = "http://127.0.0.1:5000/staff/login_details/" + String(userData.staffID) + "/" + userData.password;
            const data_fetch = await fetch(login_url)

            var data = await data_fetch.json();

            if (data['code'] == 500) {
                alert('The password or staff id is incorrect')

                return false; // Return false if the login failed
            }
            else {
                var access_id = data["access_id"]
                console.log(access_id)
                if (access_id == 4) {
                    var role = "hr"
                }
                else if (access_id == 2) {
                    var role = "staff"
                }
                
                commit('setIsLoggedIn', true);
                commit('setUserRole', role);
                commit('setUserId', userData.staffID);
                
                // this.$router.push('/rolesPage')                
                return true; // Return true if the login was successful
    
            }



        },
    },
    getters: {
        getIsLoggedIn(state) {
            return state.isLoggedIn;
        },
        getUserRole(state) {
            return state.userRole;
        },
        getUserId(state) {
            return state.userId;
        },
    },
});
