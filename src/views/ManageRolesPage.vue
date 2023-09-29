// Inside your Vue component
<template>
    <div>
        <!-- <div class="text-h3 mt-9 ">
            Manage Role Listing
        </div>
        <v-btn v-if="userIsHr" to="/manageRolesPage" id="managed">Manage Role Listings</v-btn> -->

        <!-- Search input field -->
        <v-container>
            <!-- Title and Create Roles Btn-->
            <v-row dense>
                <v-col cols="9">
                    <h1 class="ps-0 pb-8 mt-9">Manage Role Listings</h1>
                </v-col>
                <v-col cols="3">
                    <v-btn class="ms-4 mb-8 mt-9" to="/CreateRoleListing">Create</v-btn>
                </v-col>
            </v-row>
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
        <EditRoleListingsCard :roleListings="roleListings" />

    </div>
</template>

<script>
import axios from 'axios';
import EditRoleListingsCard from '../components/EditRoleListingsCard.vue'; // Import the RoleListings component

export default {
    data() {
        return {
            roleListings: [], // Initialize as an empty array
            searchQuery: '', // Initialize as an empty string
        };
    },
    mounted() {
        // Fetch role listings from the API
        axios.get('http://127.0.0.1:5000/hr/role_listings')
            .then((response) => {
                console.log(response.data.data);

                this.roleListings = response.data.data.role_listing;

            })
            .catch((error) => {
                console.error('Error fetching role listings:', error);
            });

    },

    computed: {
    },

    methods: {
        performSearch() {
            // This method is called when the Search button is clicked.
           
            // Fetch role listings from the API
            // axios.get('http://
        },
    },

    components: {
        EditRoleListingsCard, // Register the RoleListings component
    },


};
</script>
