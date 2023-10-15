<template>
    <div>
        <v-container>
            <v-row dense>
                <v-col >
                    <v-row>
                        <v-col cols="1">
                             <v-btn class="ml-12 mt-2" prepend-icon="mdi-arrow-left" variant="text" to="/ManageRolesPage">
                             Back
                             </v-btn>
                        </v-col>
                        <v-col cols="11">
                            <h1 class="ps-0 pb-8 mt-9 pr-16 text-center">View Role Applicants</h1>  
                        </v-col>
                    </v-row>
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
            <ApplicantFilterCard
              :departmentItems="departmentItems"
              :percentageMatchItems="percentageMatchItems"
              @filter-applied="handleFilterApplied"
              @filter-cleared="handleFilterCleared"
            ></ApplicantFilterCard>
          </v-card>
        </v-dialog>
      </v-col>


      <v-col cols="3" class="d-none d-lg-block ms-2">
            <!--Filter component 2-->
            <ApplicantFilterCard
              :departmentItems="departmentItems"
              :percentageMatchItems="percentageMatchItems"
              @filter-applied="handleFilterApplied"
              @filter-cleared="handleFilterCleared"
              ></ApplicantFilterCard> 
      </v-col>
      <!-- display applicants -->
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
import ApplicantFilterCard from '../components/ApplicantFilterCard.vue'; // Import the ApplicantFilterCardCard component


export default {
    data() {
        return {
            applicantsFromDb:[],
            listing_id: null, // Initialize as an empty array
            role_applicants: [],
            deadline:null ,
            department: null,
            role_name: null,
            total_applicants: null,
            searchQuery: '', // Initialize as an empty string
            showFilterModal: false, // Initialize as false to hide the modal initially
            filterError: null,
            filterErrorMsg: '',
            categoryItems: [],
            departmentItems: [],
            selectedDepartment: [],
            selectedPercentage: [],
            showFilterModal: false, // Initialize as false to hide the modal initially
        };
    },
    mounted() {
        // Fetch applicants from the API
        this.listing_id = this.$route.query.listing_id;
        axios.get(`http://127.0.0.1:5000/hr/role_applicants/${this.listing_id}`)
            .then((response) => {
                console.log(response.data.data);
                this.applicantsFromDb = response.data.data.applicants;
                console.log(this.role_applicants[0]);
                this.role_applicants=this.applicantsFromDb
                this.deadline = response.data.data.deadline,
                this.department = response.data.data.department,
                this.role_name = response.data.data.role_name,
                this.total_applicants = response.data.data.total_applicants;
            })
            .catch((error) => {
                console.error('Error fetching applicants:', error);
            });

    },

    computed: {
    },

    methods: {
    applyFilter() {
      // Fetch results
      this.filterError = '';
      this.filterErrorMsg = '';

      if (this.selectedDepartment.length == 0 && this.selectedPercentage.length == 0) {
        this.role_applicants = this.rolesFromDb;
        return;
      }

      console.log(this.selectedDepartment);
      console.log(this.selectedPercentage);

      let payload = {
        department: Array.from(this.selectedDepartment),
        match_percentage: Array.from(this.selectedPercentage),
      };


      axios.post(`http://127.0.0.1:5000/hr/filter_applicants/${this.listing_id}`, payload)
        .then((response) => {
          console.log(response.data.data);
          this.role_applicants = response.data.data.applicants;


        })
        .catch((error) => {
          console.error('Error fetching applicants:', error);
          this.filterErrorMsg = 'No applicants found based on your input filters';
          this.filterError = 404;
          this.role_applicants = [];

        });



    },
    handleFilterApplied(selectedOptions) {
      // Handle the applied filter here
      this.selectedDepartment = selectedOptions.selectedDepartment;
      this.selectedPercentage = selectedOptions.selectedPercentage;

      this.applyFilter(); // Call the method to apply the filter with the updated options
    },

    handleFilterCleared() {
      // Handle the cleared filter here
      this.selectedDepartment = [];
      this.selectedPercentage = [];      
      this.clearFilter(); // Call the method to clear the filter with the updated options
    },

    clearFilter() {
      // Clear all filters
      this.selectedDepartment = [];
      this.selectedPercentage = [];
      this.role_applicants = this.applicantsFromDb;
      this.filterError = '';
      this.filterErrorMsg = '';
    },
    showFilter() {
      this.showFilterModal = true; // Show the filter modal
    },

    hideFilterModal() {
      this.showFilterModal = false; // Hide the filter modal
    },

    },

    components: {
         // Register the RoleListings component
         RoleApplicantsCard,
         ApplicantFilterCard,
    },


};
</script>
