<template>
    <div>
        <v-container>
            <v-row dense>
                <v-col >
                    <v-row>
                        <v-col cols="3">
                             <v-btn class="ml-12 mt-2" prepend-icon="mdi-arrow-left" variant="text" to="/ManageRolesPage">
                             Back
                             </v-btn>
                        </v-col>
                        <v-col cols="6">
                            <h1 class="ps-0 pb-8 mt-9 pr-16 text-center">View Role Applicants</h1>  
                        </v-col>
                    </v-row>
                </v-col>
            </v-row>
            <!-- Search input field -->
            <v-row class="d-flex justify-center mt-3 mb-6 ">
                <v-col cols="7" class="pe-0">
                    <v-text-field v-model="searchQuery" label="Search by ??" outlined dense hide-details
                        class="rounded-top-left rounded-bottom-left"></v-text-field>
                </v-col>
                <v-col cols="1" class="d-flex justify-start ms-0 ps-0">
                    <!-- Search button attached to the end of the search bar -->
                    <v-btn @click="performSearch" color="teal-lighten-3" class="ma-0" style="height: 100%;">Search</v-btn>
                </v-col>
            </v-row>
        </v-container>
        <v-container>
            <v-row class="mt-1">
                <v-col cols="6" class="text-center">
                    <div class="text-h6" id="role_name"><strong>Role Name:</strong> {{ role_name }}</div>
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

        <v-row class="d-flex justify-center">
      <!-- Display filter button on mobile screens -->
      <v-col cols="9" class="d-lg-none d-flex justify-end">

        <v-btn @click="showFilter()" class=" " color="teal-lighten-3">
          Filter
        </v-btn>
        <v-dialog v-model="showFilterModal" hide-overlay max-width="400px">
          <v-card>
            <v-toolbar flat dark>
              <v-toolbar-title>Filter Results</v-toolbar-title>
              <v-spacer></v-spacer>
              <v-btn icon @click="hideFilterModal">
                <v-icon>mdi-close</v-icon>
              </v-btn>
            </v-toolbar>
            <!--Filter component 1-->
            <v-card-text>
  <!-- Filter section content here -->
  <!-- ... -->
  <v-card class="mx-auto">


    <v-card-text>
      <h2 class="text-h6 mb-2">
        Category
      </h2>

      <v-chip-group v-model="selectedCategory" column multiple>
        <v-chip class="me-2" filter variant="outlined" v-for="category in categoryItems" :key="category"
          :value="category" :id="'category_' + category">
          {{ category }}

        </v-chip>

      </v-chip-group>
    </v-card-text>

    <v-card-text>
      <h2 class="text-h6 mb-2">
        Department
      </h2>

      <v-chip-group v-model="selectedDepartment" column multiple>
        <v-chip class="me-2" filter variant="outlined" v-for="department in departmentItems" :key="department"
          :value="department" :id="'department_' + department">
          {{ department }}

        </v-chip>

      </v-chip-group>
    </v-card-text>
    
    <v-card-text>
      <h2 class="text-h6 mb-2">
        Match Percentage(%)
      </h2>

      <v-chip-group v-model="selectedPercentage" column multiple>
        <v-chip class="me-2" filter variant="outlined" v-for="percentageMatch in percentageMatchItems"
          :key="percentageMatch" :value="percentageMatch" :id="percentageMatch">
          {{ percentageMatch }}

        </v-chip>

      </v-chip-group>
    </v-card-text>

    <v-card-actions>
              <v-btn @click="applyFilter();hideFilterModal()">Apply Filter</v-btn>
              <v-btn @click="clearFilter();hideFilterModal()" color="error">Clear All</v-btn>
            </v-card-actions>
  </v-card>
            </v-card-text>
          </v-card>
        </v-dialog>
      </v-col>


      <v-col cols="3" class="d-none d-lg-block ms-2">
            <!--Filter component 2-->
            <v-card-text>
            <!-- Filter section content here -->
            <!-- ... -->
            <v-card class="mx-auto">


                <v-card-text>
                <h2 class="text-h6 mb-2">
                    Category
                </h2>

                <v-chip-group v-model="selectedCategory" column multiple>
                    <v-chip class="me-2" filter variant="outlined" v-for="category in categoryItems" :key="category"
                    :value="category" :id="'category_' + category">
                    {{ category }}

                    </v-chip>

                </v-chip-group>
                </v-card-text>

                <v-card-text>
                <h2 class="text-h6 mb-2">
                    Department
                </h2>

                <v-chip-group v-model="selectedDepartment" column multiple>
                    <v-chip class="me-2" filter variant="outlined" v-for="department in departmentItems" :key="department"
                    :value="department" :id="'department_' + department">
                    {{ department }}

                    </v-chip>

                </v-chip-group>
                </v-card-text>
                
                <v-card-text>
                <h2 class="text-h6 mb-2">
                    Match Percentage(%)
                </h2>

                <v-chip-group v-model="selectedPercentage" column multiple>
                    <v-chip class="me-2" filter variant="outlined" v-for="percentageMatch in percentageMatchItems"
                    :key="percentageMatch" :value="percentageMatch" :id="percentageMatch">
                    {{ percentageMatch }}

                    </v-chip>

                </v-chip-group>
                </v-card-text>

                <v-card-actions>
                        <v-btn @click="applyFilter();hideFilterModal()">Apply Filter</v-btn>
                        <v-btn @click="clearFilter();hideFilterModal()" color="error">Clear All</v-btn>
                        </v-card-actions>
            </v-card>
            </v-card-text>
      </v-col>
      <!-- display role listings -->
      <v-col :cols="9" lg="" class="justify-end" id="filter_alert">
        <v-alert v-if="filterError == 404" type="info" variant="outlined" icon="$info"
          style="font-size: 16px; padding: 8px; height: auto;" dismissible>
          {{ filterErrorMsg }}
        </v-alert>
        <RoleApplicantsCard :role_applicants="role_applicants" />
      </v-col>
        </v-row>  
        

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
