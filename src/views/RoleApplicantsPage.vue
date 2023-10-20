<template>
  <div>
    <v-container fluid class="py-0 px-0 position-relative">
      <img v-bind:src="require('../assets/office12.jpg')" style="width: 100%; height: 300px; margin-top: 5px" />
      <v-container class="search_container">
        <v-row>
          <v-col cols="12" sm="3" md="3" lg="3" class="d-none d-lg-block">
            <v-btn class="text-left ml-12 mt-2" prepend-icon="mdi-arrow-left" variant="text" to="/ManageRolesPage">
              Back
            </v-btn>
          </v-col>
        </v-row>
        <v-row dense>
          <v-col>
            <h1 class="ps-0 pb-4 mt-4 text-center text--white" color="white">
              Applicants for {{ role_name }}
            </h1>
          </v-col>
        </v-row>
        <!-- <v-col cols="6" class="text-center">
                    <div class="text-h6" id="role_name"><strong>Role Name:</strong> {{ role_name }}</div>
                </v-col> -->
        <v-row class="mt-1 mb-4">
          <v-col class="text-center">
            <div class="text-h6">
              <strong>Department:</strong> {{ department }}
            </div>
          </v-col>
          <v-col class="text-center">
            <div class="text-h6"><strong>Deadline:</strong> {{ deadline }}</div>
          </v-col>
          <v-col class="text-center">
            <div class="text-h6">
              <strong>Total Applicants:</strong> {{ total_applicants }}
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-container>

    <v-row class="d-flex justify-center">
      <v-col cols="3" class="d-none d-lg-block ms-2">
        <!--Filter component 2-->
        <v-card>
          <v-toolbar flat dark>
            <v-toolbar-title>Filters</v-toolbar-title>
          </v-toolbar>

          <ApplicantFilterCard :departmentItems="departmentItems" :percentageMatchItems="percentageMatchItems"
            @filter-applied="handleFilterApplied" @filter-cleared="handleFilterCleared"></ApplicantFilterCard>
        </v-card>
      </v-col>

      <!-- display applicants -->
      <v-col :cols="9" lg="" class="justify-end" id="filter_alert">
        <!-- add a sort by dropdown -->
        <v-row class="d-flex justify-end">
          <!-- Display filter button on mobile screens -->
          <v-col cols="6" class="d-lg-none d-flex justify-center">
            <v-btn @click="showFilter()" class="" color="teal-lighten-3" style="height: 56px; width: 300px;">
              Filter By

              <v-icon class="ms-2">mdi-filter</v-icon>

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
                <ApplicantFilterCard :departmentItems="departmentItems" :percentageMatchItems="percentageMatchItems"
                  @filter-applied="handleFilterApplied" @filter-cleared="handleFilterCleared"
                  @filter-modal-closed="hideFilterModal"></ApplicantFilterCard>
              </v-card>
            </v-dialog>
          </v-col>

          <!-- sort select -->
          <v-col cols="6" class="d-flex d-md-block ">
            <v-select label="Sort by"
              :items="['Newest', 'Match Percentage (High to Low)', 'Match Percentage (Low to High)']"
              style="width: 300px;" v-model="selectedSort" >

            </v-select>
          </v-col>
        </v-row>

        <v-row>
          <v-alert v-if="filterError == 404" type="info" variant="outlined" icon="$info"
            style="font-size: 16px; padding: 8px; height: auto" dismissible>
            {{ filterErrorMsg }}
          </v-alert>
        </v-row>

        <v-row>
          <v-col>
            <RoleApplicantsCard :role_applicants="role_applicants" />
          </v-col>
        </v-row>

      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import RoleApplicantsCard from "../components/RoleApplicantsCard.vue"; // Import the RoleApplicantsCard component
import ApplicantFilterCard from "../components/ApplicantFilterCard.vue"; // Import the ApplicantFilterCardCard component

export default {
  data() {
    return {
      applicantsFromDb: [],
      listing_id: null, // Initialize as an empty array
      role_applicants: [],
      deadline: null,
      department: null,
      role_name: null,
      total_applicants: null,
      searchQuery: "", // Initialize as an empty string
      showFilterModal: false, // Initialize as false to hide the modal initially
      filterError: null,
      filterErrorMsg: "",
      categoryItems: [],
      departmentItems: [],
      selectedDepartment: [],
      selectedPercentage: [],
      showFilterModal: false, // Initialize as false to hide the modal initially
      selectedSort: "newest",
    };
  },
  watch: {
    // when the selected sort changes, call the apply filter method
    selectedSort: function (newVal, oldVal) {
      if (newVal == oldVal) {
        return;
      }

      this.applyFilter();
    },
  },

  mounted() {
    // Fetch applicants from the API
    this.listing_id = this.$route.query.listing_id;
    axios
      .get(`http://127.0.0.1:5000/hr/role_applicants/${this.listing_id}?sort_by=${this.selectedSort}`)
      .then((response) => {
        console.log(response.data.data);
        this.applicantsFromDb = response.data.data.applicants;
        console.log(this.role_applicants[0]);
        this.role_applicants = this.applicantsFromDb;
        (this.deadline = response.data.data.deadline),
          (this.department = response.data.data.department),
          (this.role_name = response.data.data.role_name),
          (this.total_applicants = response.data.data.total_applicants);
      })
      .catch((error) => {
        console.error("Error fetching applicants:", error);
      });
  },

  computed: {},

  methods: {
    applyFilter() {
      // Fetch results
      this.filterError = "";
      this.filterErrorMsg = "";

      let sortInput = '' 

      // determine sort input to match backend
      if (this.selectedSort == "Newest") {
        sortInput = "newest";
      }

      else if (this.selectedSort == "Match Percentage (High to Low)") {
        sortInput = "match_desc"
      }

      else if (this.selectedSort == "Match Percentage (Low to High)") {
        sortInput = "match_asc"
      }

      let payload = {
        department: Array.from(this.selectedDepartment),
        match_percentage: Array.from(this.selectedPercentage),
        sort_by: sortInput, 
      };
      
      // console.log(this.selectedDepartment);
      // console.log(this.selectedPercentage);

      axios
        .post(
          `http://127.0.0.1:5000/hr/filter_applicants/${this.listing_id}`,
          payload
        )
        .then((response) => {
          console.log(response.data.data);
          this.role_applicants = response.data.data.applicants;
        })
        .catch((error) => {
          console.error("Error fetching applicants:", error);
          this.filterErrorMsg =
            "No applicants found based on your input filters";
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
      this.filterError = "";
      this.filterErrorMsg = "";
      this.selectedSort = "newest";
    },
    showFilter() {
      this.showFilterModal = true; // Show the filter modal
    },

    hideFilterModal() {
      this.showFilterModal = false; // Hide the filter modal
    },

    sortListings() {
      // Sort the listings
      console.log("in sort listings");
      this.listing_id = this.$route.query.listing_id;
      axios
        .get(`http://127.0.0.1:5000/hr/role_applicants/${this.listing_id}?sort_by=${this.selectedSort}`)
        // .get(`http://127.0.0.1:5000/hr/role_applicants/${this.listing_id}?sort_by=${newVal}`)
        .then((response) => {
          console.log(response.data.data);
          this.applicantsFromDb = response.data.data.applicants;
          console.log(this.role_applicants[0]);
          this.role_applicants = this.applicantsFromDb;
          (this.deadline = response.data.data.deadline),
            (this.department = response.data.data.department),
            (this.role_name = response.data.data.role_name),
            (this.total_applicants = response.data.data.total_applicants);
        })
        .catch((error) => {
          console.error("Error fetching applicants:", error);
        });
    }

  },

  components: {
    // Register the RoleListings component
    RoleApplicantsCard,
    ApplicantFilterCard,
  },
};
</script>

<style>
.search_container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
</style>
