<template>
    <div>
        <div class="text-h3 mt-9 ">
            View Role Applicants
        </div>
        <v-container>
            <v-row class="mt-1">
                <v-col cols="6" class="text-center">
                    <div class="text-h6"><strong>Role Name:</strong> {{ role_name }}</div>
                </v-col>
                <v-col cols="6" class="text-center">
                    <div class="text-h6"><strong>Department:</strong> {{ department }}</div>
                </v-col>
            </v-row>
            <v-row class="mt-1">
                <v-col cols="6" class="text-center">
                    <div class="text-h6"><strong>Deadline:</strong> {{ deadline }}</div>
                </v-col>
                <v-col cols="6" class="text-center">
                    <div class="text-h6"><strong>Total Applicants:</strong> {{ total_applicants }}</div>
                </v-col>
            </v-row>
        </v-container>
        <v-container>
            <!-- Search input field -->
            <!--<v-row class="d-flex justify-center mt-3 mb-6 ">
                <v-col cols="7" class="pe-0">
                    <v-text-field v-model="searchQuery" label="Search by Job title" outlined dense hide-details id="search_bar"
                        class="rounded-top-left rounded-bottom-left"></v-text-field>
                </v-col>
                <v-col cols="1" class="d-flex justify-start ms-0 ps-0">-->
                    <!-- Search button attached to the end of the search bar -->
                    <!--<v-btn @click="performSearch" color="primary" class="ma-0" style="height: 100%;" id="search_btn">Search</v-btn>
                </v-col>
            </v-row>-->

            <!-- Search button -->
        </v-container>

        <RoleApplicantsCard :role_applicants="role_applicants" />

    </div>
</template>

<script>
import axios from 'axios';
import RoleApplicantsCard from '../components/RoleApplicantsCard.vue'; // Import the RoleApplicantsCard component

export default {
    data() {
        return {
            listing_id: null, // Initialize as an empty array
            role_applicants: [],
            deadline:null ,
            department: null,
            role_name: null,
            total_applicants: null,
            searchQuery: '', // Initialize as an empty string
        };
    },
    mounted() {
        // Fetch applicants from the API
        this.listing_id = this.$route.query.listing_id;
        axios.get(`http://127.0.0.1:5000/hr/role_applicants/${this.listing_id}`)
            .then((response) => {
                console.log(response.data.data);

                //this.rolesFromDb = response.data.data.role_listings_with_skill_match;
                this.role_applicants = response.data.data.applicants;
                console.log(this.role_applicants[0]);
                this.deadline = response.data.data.deadline,
                this.department = response.data.data.department,
                this.role_name = response.data.data.role_name,
                this.total_applicants = response.data.data.total_applicants;
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
                console.error('Error fetching role applicants:', error);
            });
        },
    },

    components: {
         // Register the RoleListings component
         RoleApplicantsCard,
    },


};
</script>
