// Inside your Vue component
<template>
    <div>
        <div class="text-h3 mt-9 ">
            Role Listings
        </div>
        <!-- Search input field -->
        <v-container>
            <!-- Search input field -->
            <v-row class="d-flex justify-center mt-3 mb-6 ">
                <v-col cols="7" class="pe-0">
                    <v-text-field v-model="searchQuery" label="Search by Job title" outlined dense hide-details
                        class="rounded-top-left rounded-bottom-left"></v-text-field>
                </v-col>
                <v-col cols="1" class="d-flex justify-start ms-0 ps-0">
                    <!-- Search button attached to the end of the search bar -->
                    <v-btn @click="performSearch" color="primary" class="ma-0" style="height: 100%;">Search</v-btn>
                </v-col>
            </v-row>

            <!-- Search button -->
        </v-container>

        <ViewRoleListingsCard :role_listings_with_skill_match="role_listings_with_skill_match" />

    </div>
</template>

<script>
import axios from 'axios';
import ViewRoleListingsCard from '../components/ViewRoleListingsCard.vue'; // Import the ViewRoleListingsCard component

export default {
    data() {
        return {
            role_listings_with_skill_match: [], // Initialize as an empty array
            searchQuery: '', // Initialize as an empty string
        };
    },
    mounted() {
        // Fetch role listings from the API
        // fetching role listings that staff has not applied for
        var userId = this.getUserId;

        axios.get(`http://127.0.0.1:5000/staff/role_listings/${userId}`)
            .then((response) => {
                console.log(response.data.data);

                this.role_listings_with_skill_match = response.data.data.role_listings_with_skill_match;
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
           
            // Fetch role listings from the API
            // axios.get('http://
        },
    },

    components: {
        ViewRoleListingsCard, // Register the RoleListings component
    },


};
</script>
