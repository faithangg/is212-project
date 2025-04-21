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
            try { // Add try...catch for fetch errors
                const data_fetch = await fetch(login_url)
                var data = await data_fetch.json();

                if (data['code'] >= 400) { // Check for any error code (4xx or 5xx)
                    console.error("Login API error:", data.message || "Unknown error");
                    commit('setIsLoggedIn', false); // Ensure logged out state on error
                    commit('setUserRole', null);
                    commit('setUserId', null);
                    return false; // Return false if the login failed
                }
                else {
                    var access_id = data["access_id"];
                    console.log("Received access_id:", access_id); // Log received ID

                    let role = 'staff'; // Default role
                    if (access_id === 4) { // Use === for strict comparison
                        role = "hr";
                    } else if (access_id === 1) {
                        role = "admin"; // Add mapping for Admin
                    } else if (access_id === 3) {
                        role = "manager"; // Add mapping for Manager
                    } else if (access_id === 2) {
                        role = "staff"; // Explicitly map User/Staff
                    } else {
                         console.warn("Unexpected access_id received:", access_id); // Warn about unexpected IDs
                         // Role remains the default 'staff'
                    }
                    
                    console.log("Setting role to:", role); // Log the role being set
                    commit('setIsLoggedIn', true);
                    commit('setUserRole', role); // Commit the determined role
                    commit('setUserId', userData.staffID);
                    
                    return true; // Return true if the login was successful
        
                }
            } catch (error) {
                console.error("Error during authentication fetch:", error);
                commit('setIsLoggedIn', false); // Ensure logged out state on fetch error
                commit('setUserRole', null);
                commit('setUserId', null);
                return false;
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
