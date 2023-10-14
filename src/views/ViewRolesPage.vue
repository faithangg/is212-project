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
          <v-btn @click="performSearch" color="teal-lighten-3" style="height: 100%;"
            id="search_btn" text="Search"></v-btn>
        </v-col>
        <v-col cols="8" class="text-end pt-0">
          <v-btn @click="clearSearch" flat text size="small">Clear Search</v-btn>
        </v-col>
      </v-row>
      <!-- error message -->
      <v-row class="d-flex justify-center mt-0 mb-6">
        <v-col cols="8" class="pt-0 h-25" id="search_alert">
          <v-alert v-if="searchQueryError == 400" type="error" variant="outlined" icon="$error"
            style="font-size: 12px; padding: 8px; height: auto;" dismissible>
            {{ searchQueryErrorMsg }}
          </v-alert>
          <v-alert v-if="searchQueryError == 404" type="info" variant="outlined" icon="$info"
            style="font-size: 12px; padding: 8px; height: auto;" dismissible>
            {{ searchQueryErrorMsg }}
          </v-alert>
        </v-col>
      </v-row>

      <!-- Search button -->

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
              </v-card>
            </v-card-text>

            <v-card-actions>
              <v-btn @click="applyFilter();hideFilterModal()">Apply Filter</v-btn>
              <v-btn @click="clearFilter();hideFilterModal()" color="error">Clear All</v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </v-col>


      <v-col cols="3" class="d-none d-lg-block ms-2">
        <v-card class="mx-auto">
          <v-toolbar flat dark>
            <v-toolbar-title>Filter results</v-toolbar-title>
          </v-toolbar>

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
        </v-card>

        <!-- Clear filter button -->
        <v-col cols="4" sm="8" class="text-left">
          <v-btn @click="clearFilter" flat text size="small">Clear All</v-btn>
        </v-col>

        <!-- Apply filter button -->
        <v-col cols="8" sm="8" class="text-right">
          <v-btn @click="applyFilter" density="default" id="apply_filter_btn" >Apply Filter</v-btn>
        </v-col>
        <!-- </v-card> -->
      </v-col>

      <!-- </div> -->
      <!-- display role listings -->
      <v-col :cols="9" lg="" class="justify-end" id="filter_alert">
        <v-alert v-if="filterError == 404" type="info" variant="outlined" icon="$info"
          style="font-size: 16px; padding: 8px; height: auto;" dismissible>
          {{ filterErrorMsg }}
        </v-alert>
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
      filterError: null,
      searchQueryErrorMsg: '', // Initialize as an empty string
      filterErrorMsg: '',
      // percentageMatchItems: ["0-10", "11-20", "21-30", "31-40", "41-50", "51-60", "61-70", "71-80", "81-90", "91-100"],
      percentageMatchItems: ["0-20", "21-40", "41-60", "61-80", "81-100"],
      categoryItems: [],
      departmentItems: [],
      selectedCategory: [],
      selectedDepartment: [],
      selectedPercentage: [],
      showFilterModal: false, // Initialize as false to hide the modal initially
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
    isMobileScreen() {
      return window.innerWidth <= 768; // Adjust the width as needed
    },

  },

  methods: {
    performSearch() {
      // This method is called when the Search button is clicked.
      this.searchQueryError = '';
      this.searchQueryErrorMsg = '';
      this.filterError = '';
      this.filterErrorMsg = '';

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
            this.displayListings = [];
          }
          else if (error.response.status == 400) {
            this.searchQueryErrorMsg = 'Invalid search query - No special characters';
            this.searchQueryError = 400;
            this.displayListings = [];
          }
        });
    },
    applyFilter() {
      // Fetch results
      this.searchQueryError = '';
      this.searchQueryErrorMsg = '';
      this.filterError = '';
      this.filterErrorMsg = '';

      if (this.selectedCategory.length == 0 && this.selectedDepartment.length == 0 && this.selectedPercentage.length == 0) {
        this.displayListings = this.rolesFromDb;
        return;
      }

      console.log(this.selectedCategory);
      console.log(this.selectedDepartment);
      console.log(this.selectedPercentage);
      const selectedCategoriesArray = Array.from(this.selectedCategory);
      console.log(selectedCategoriesArray);
      let userId = this.getUserId;

      let payload = {
        category: Array.from(this.selectedCategory),
        department: Array.from(this.selectedDepartment),
        match_percentage: Array.from(this.selectedPercentage),
      };


      axios.post(`http://127.0.0.1:5000/staff/filter_role_listings/${userId}`, payload)
        .then((response) => {
          console.log(response.data.data);
          this.displayListings = response.data.data.role_listings;


        })
        .catch((error) => {
          console.error('Error fetching role listings:', error);
          this.filterErrorMsg = 'No role listings found based on your input filters';
          this.filterError = 404;
          this.displayListings = [];

        });



    },

    clearFilter() {
      // Clear all filters
      this.selectedCategory = [];
      this.selectedDepartment = [];
      this.selectedPercentage = [];
      this.displayListings = this.rolesFromDb;
      this.filterError = '';
      this.filterErrorMsg = '';
    },

    clearSearch() {
      // Clear search bar
      this.searchQuery = '';
      this.displayListings = this.rolesFromDb;
      this.searchQueryError = null;
      this.searchQueryErrorMsg = '';
    },
    showFilter() {
      this.showFilterModal = true; // Show the filter modal
    },

    hideFilterModal() {
      this.showFilterModal = false; // Hide the filter modal
    },
  },

  components: {
    ViewRoleListingsCard, // Register the RoleListings component
  },


};
</script>
<style> /* Styles for mobile screens */
 .sidebar {
   display: none;
   /* Hide the sidebar by default */
   /* Add any necessary styles for your sidebar, e.g., background color, width, etc. */
 }

 /* Styles for larger screens */
 .main-content {
   /* Add any necessary styles for the main content area, e.g., margin, padding, width, etc. */
 }

 /* Media query for mobile screens (adjust the max-width as needed) */
 @media (max-width: 768px) {
   .sidebar {
     display: block;
     /* Display the sidebar on mobile screens */
     /* Add styles to make the sidebar appear as a side panel, e.g., fixed position, width, background color, etc. */
   }

   .main-content {
     width: 100%;
     /* Full width for main content on mobile screens */
     /* Add styles to adjust the main content's appearance on mobile screens */
   }
 }

 /* Additional styles for larger screens (customize as needed) */
 @media (min-width: 769px) {
   .main-content.full-width {
     width: 100%;
     /* Adjust the width for larger screens as needed */
     /* Add any additional styles for larger screens */
   }
 }
</style> 