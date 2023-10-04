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
        <!-- display filter listings -->
        <v-row class="d-flex justify-center">

           <v-col :cols="2" class="justify-start">
            <div class="text-h5 text-left">
              Filters
            </div>

          <v-col cols="12" sm="9" md="4" class="text-left">
            <v-btn @click="clearFilter" flat text size="small">Clear All</v-btn>
          </v-col>
          <v-expansion-panels
            multiple>
            <!--Category Filter-->
            <v-expansion-panel>
              <v-expansion-panel-title>Category</v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-container fluid>
                  <v-checkbox
                    v-for="(item, index) in categoryItems"
                    :key="index"
                    v-model="selectedItems"
                    :label="item"
                    :value="item"
                  ></v-checkbox>

                </v-container>
              </v-expansion-panel-text>  
            </v-expansion-panel>
            <!--Department Filter -->
            <v-expansion-panel>
              <v-expansion-panel-title>Department</v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-container fluid>
                  <v-checkbox
                    v-for="(item, index) in departmentItems"
                    :key="index"
                    v-model="selectedItems"
                    :label="item"
                    :value="item"
                  ></v-checkbox>

                </v-container>
              </v-expansion-panel-text>  
            </v-expansion-panel>
            <!--Match Percentage Filter hardcoded-->
            <v-expansion-panel>
              <v-expansion-panel-title>Match Percentage </v-expansion-panel-title>
              <v-expansion-panel-text>
                <v-container fluid>
                  <p>{{ selected }}</p>
                  <v-checkbox
                    v-model="selected"
                    label="0 - 10"
                    value="0 - 10"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="11-20"
                    value="11-20"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="21 - 30"
                    value="21 - 30"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="31 - 40"
                    value="31 - 40"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="41 - 50"
                    value="41 - 50"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="51 - 60"
                    value="51 - 60"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="61 - 70"
                    value="61 - 70"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="71 - 80"
                    value="71 - 80"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="81 - 90"
                    value="81 - 90"
                  ></v-checkbox>
                  <v-checkbox
                    v-model="selected"
                    label="91 - 100"
                    value="91 - 100"
                  ></v-checkbox>
                </v-container>
              </v-expansion-panel-text>
            </v-expansion-panel>
          </v-expansion-panels>
          <v-col cols="12" sm="9" md="4">
            <v-btn @click="applyFilter" density="default">Apply Filter</v-btn>
          </v-col>
        </v-col>
        <!-- display role listings -->
        <v-col :cols="8" class="justify-end">
        <ViewRoleListingsCard :role_listings_with_skill_match="displayListings" />
        </v-col>
        </v-row>
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
            items: [],
            selectedItems: [],
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
        
            // Fetch filter options from the API
        axios.get(`http://127.0.0.1:5000/staff/filter_options`)
            .then((response) => {
                console.log(response.data.data);
                console.log(response.data.data.category);

                this.categoryItems = response.data.data.category;
                this.departmentItems = response.data.data.department;
            })
            .catch((error) => {
                console.error('Error fetching filter options:', error);
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
        applyFilter(){
        // Fetch results
        },
        clearFilter(){
        // Clear all filters
        }
    },

    components: {
        ViewRoleListingsCard, // Register the RoleListings component
    },


};
</script>
