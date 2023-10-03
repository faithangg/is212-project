// Inside your Vue component
<template>
    <div>
        <div class="text-h3 mt-9 ">
            Role Listings
        </div>
        <!-- Search input field -->
        <v-container>
            <!-- Search input field -->
            <v-row class="d-flex justify-center mt-3 mb-0 ">
                <v-col cols="7" class="pe-0">
                    <v-text-field v-model="searchQuery" label="Search by Job title" outlined dense hide-details id="search_bar"
                        class="rounded-top-left rounded-bottom-left"></v-text-field>
                </v-col>
                <v-col cols="1" class="d-flex justify-start ms-0 ps-0">
                    <!-- Search button attached to the end of the search bar -->
                    <v-btn @click="performSearch" color="primary" class="ma-0" style="height: 100%;" id="search_btn">Search</v-btn>
                </v-col>
            </v-row>
            <!-- error message -->
            <v-row class="d-flex justify-center mt-0 mb-6" >
                <v-col cols="8" class="pt-0 h-25" >
                    <v-alert
                        v-if="searchQueryError == 400"
                        type="error" 
                        variant="outlined"
                        icon="$error"
                        
                        style="font-size: 12px; padding: 8px; height: auto;"
                        dismissible>
                        {{ searchQueryErrorMsg }}            
                    </v-alert>
                    <v-alert
                        v-if="searchQueryError == 404"
                        type="info" 
                        variant="outlined"
                        icon="$info"
                        
                        style="font-size: 12px; padding: 8px; height: auto;"
                        dismissible>
                        {{ searchQueryErrorMsg }}            
                    </v-alert>
                </v-col>
            </v-row>

            <!-- Search button -->
        </v-container>

        <ViewRoleListingsCard :role_listings_with_skill_match="displayListings" />

    </div>
</template>

<script>
import axios from 'axios';
import ViewRoleListingsCard from '../components/ViewRoleListingsCard.vue'; // Import the ViewRoleListingsCard component

export default {
    data() {
        return {
            rolesFromDb: [], // Initialize as an empty array
            displayListings: [],
            searchQuery: '', // Initialize as an empty string
            searchQueryError: null,  
            searchQueryErrorMsg:  '', // Initialize as an empty string
        };
    },
    mounted() {
        // Fetch role listings from the API
        // fetching role listings that staff has not applied for
        var userId = this.getUserId;

        axios.get(`http://127.0.0.1:5000/staff/role_listings/${userId}`)
            .then((response) => {
                console.log(response.data.data);

                this.rolesFromDb = response.data.data.role_listings_with_skill_match;
                this.displayListings = this.rolesFromDb;
                console.log(this.role_listings_with_skill_match);
                console.log(this.role_listings_with_skill_match[0].role_listing);
            })
            .catch((error) => {
                console.error('Error fetching role listings:', error);
            });

    },

    computed: {
        userIsHr() {
            // Access the user's role from your Vuex store getter
            return this.$store.getters.getUserRole === 'hr';
        },

        getUserId() {
            // Access the user's role from your Vuex store getter
            return this.$store.getters.getUserId;
        },

    },

    methods: {
        performSearch() {
            // This method is called when the Search button is clicked.
           this.searchQueryError = '';
           this.searchQueryErrorMsg = '';

            if (this.searchQuery == '') {
                this.displayListings = this.rolesFromDb;
                return;
            }
            // Fetch role listings from the API
            var userId = this.getUserId;

            axios.get(`http://127.0.0.1:5000/staff/browse_role_listings/${userId}/${this.searchQuery}`)
            .then((response) => {
                console.log(response.data.data);

                this.displayListings = response.data.data.role_listings_with_skill_match;
            })
            .catch((error) => {
                console.error('Error fetching role listings:', error);

                console.log(error.response.status);

                if (error.response.status == 404) {
                    this.searchQueryErrorMsg = 'No role listings found';
                    this.searchQueryError = 404;
                }
                else if (error.response.status == 400) {
                    this.searchQueryErrorMsg = 'Invalid search query - No special characters';
                    this.searchQueryError = 400;
                }
            });
        },
    },

    components: {
        ViewRoleListingsCard, // Register the RoleListings component
    },


};
</script>
