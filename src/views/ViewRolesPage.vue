<template>
  <div>
    <v-container fluid class="py-0 px-0 position-relative" >
      <img
          v-bind:src="require('../assets/office5.jpg')"
          style="width: 100%; height: 300px; margin-top: 5px;" 
      />

      <v-container class="search_container">
        <v-row dense>
            <v-col>
                <h1 class="ps-0 pb-4 mt-4 text-center">Role Listings</h1>
            </v-col>
        </v-row>
        <!-- Search input field -->
        <v-row class="d-flex mt-3 mb-0 justify-sm-center">
          <v-col cols="10" md="7" class="pe-0">
            <v-text-field
              v-model="searchQuery"
              label="Search by Job title"
              outlined
              dense
              hide-details
              id="search_bar"
              class="rounded-input search-bar"
            ></v-text-field>
          </v-col>
          <v-col cols="1" class="d-flex justify-start ms-0 ps-0">
            <!-- Search button attached to the end of the search bar -->
            <v-btn
              @click="performSearch"
              color="teal-lighten-3"
              style="height: 100%"
              id="search_btn"
              icon="mdi-magnify"
              class="square-button"
              border-radius="0"
              density="default"
            >
            </v-btn>
          </v-col>
          <v-col cols="12" md="8" class="text-end pt-0">
            <v-btn @click="clearSearch" flat text size="small"
              >Clear Search</v-btn
            >
          </v-col>
        </v-row>

        <!-- error message -->
        <v-row class="d-flex justify-center mt-0 mb-6">
          <v-col cols="12" md="8" class="pt-0 h-25" id="search_alert">
            <v-alert
              v-if="searchQueryError == 400"
              type="error"
              icon="$error"
              style="font-size: 12px; padding: 8px; height: auto"
              dismissible
            >
              {{ searchQueryErrorMsg }}
            </v-alert>
            <v-alert
              v-if="searchQueryError == 404"
              type="info"
              icon="$info"
              style="font-size: 12px; padding: 8px; height: auto"
              dismissible
            >
              {{ searchQueryErrorMsg }}
            </v-alert>
          </v-col>
        </v-row>
      </v-container>
    </v-container>

    <v-row class="d-flex justify-center">
      <!-- Display filter button on mobile screens -->
      <v-col cols="11" class="d-lg-none d-flex justify-end">
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
            <RoleFilterCard
              :categoryItems="categoryItems"
              :departmentItems="departmentItems"
              :percentageMatchItems="percentageMatchItems"
              @filter-applied="handleFilterApplied"
              @filter-cleared="handleFilterCleared"
              @filter-modal-closed="hideFilterModal"
            ></RoleFilterCard>
          </v-card>
        </v-dialog>
      </v-col>

      <v-col cols="3" class="d-none d-lg-block ms-2">
        <!--Filter component 2-->
        <v-card>
          <v-toolbar flat dark>
            <v-toolbar-title>Filters</v-toolbar-title>
          </v-toolbar>
          <RoleFilterCard
            :categoryItems="categoryItems"
            :departmentItems="departmentItems"
            :percentageMatchItems="percentageMatchItems"
            @filter-applied="handleFilterApplied"
            @filter-cleared="handleFilterCleared"
          ></RoleFilterCard>
        </v-card>
      </v-col>
      <!-- display role listings -->
      <v-col :cols="9" lg="" class="justify-end" id="filter_alert">
        <v-alert
          v-if="filterError == 404"
          type="info"
          variant="outlined"
          icon="$info"
          style="font-size: 16px; padding: 8px; height: auto"
          dismissible
        >
          {{ filterErrorMsg }}
        </v-alert>
        <ViewRoleListingsCard
          :role_listings_with_skill_match="displayListings"
        />
      </v-col>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";
import ViewRoleListingsCard from "../components/ViewRoleListingsCard.vue"; // Import the ViewRoleListingsCard component
import RoleFilterCard from "../components/RoleFilterCard.vue"; // Import the ViewRoleListingsCard component

export default {
  data() {
    return {
      rolesFromDb: [], // Initialize as an empty array
      displayListings: [],
      searchQuery: "", // Initialize as an empty string
      searchQueryError: null,
      filterError: null,
      searchQueryErrorMsg: "", // Initialize as an empty string
      filterErrorMsg: "",
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

    axios
      .get(`http://127.0.0.1:5000/staff/role_listings/${userId}`)
      .then((response) => {
        console.log(response.data.data);

        this.rolesFromDb = response.data.data.role_listings_with_skill_match;
        this.displayListings = this.rolesFromDb;
        console.log(this.role_listings_with_skill_match);
        console.log(this.role_listings_with_skill_match[0].role_listing);
      })
      .catch((error) => {
        console.error("Error fetching role listings:", error);
      });

    // Fetch filter options from the API
    axios
      .get(`http://127.0.0.1:5000/staff/filter_options`)
      .then((response) => {
        console.log(response.data.data);
        console.log(response.data.data.category);

        this.categoryItems = response.data.data.category;
        this.departmentItems = response.data.data.department;
      })
      .catch((error) => {
        console.error("Error fetching filter options:", error);
      });
  },

  computed: {
    userIsHr() {
      // Access the user's role from your Vuex store getter
      return this.$store.getters.getUserRole === "hr";
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
      this.searchQueryError = "";
      this.searchQueryErrorMsg = "";
      this.filterError = "";
      this.filterErrorMsg = "";

      if (this.searchQuery == "") {
        this.displayListings = this.rolesFromDb;
        return;
      }
      // Fetch role listings from the API
      var userId = this.getUserId;

      axios
        .get(
          `http://127.0.0.1:5000/staff/browse_role_listings/${userId}/${this.searchQuery}`
        )
        .then((response) => {
          console.log(response.data.data);

          this.displayListings =
            response.data.data.role_listings_with_skill_match;
        })
        .catch((error) => {
          console.error("Error fetching role listings:", error);

          console.log(error.response.status);

          if (error.response.status == 404) {
            this.searchQueryErrorMsg = "No role listings found";
            this.searchQueryError = 404;
            this.displayListings = [];
          } else if (error.response.status == 400) {
            this.searchQueryErrorMsg =
              "Invalid search query - No special characters";
            this.searchQueryError = 400;
            this.displayListings = [];
          }
        });
    },
    applyFilter() {
      // Fetch results
      this.searchQueryError = "";
      this.searchQueryErrorMsg = "";
      this.filterError = "";
      this.filterErrorMsg = "";

      if (
        this.selectedCategory.length == 0 &&
        this.selectedDepartment.length == 0 &&
        this.selectedPercentage.length == 0
      ) {
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

      axios
        .post(
          `http://127.0.0.1:5000/staff/filter_role_listings/${userId}`,
          payload
        )
        .then((response) => {
          console.log(response.data.data);
          this.displayListings = response.data.data.role_listings;
        })
        .catch((error) => {
          console.error("Error fetching role listings:", error);
          this.filterErrorMsg =
            "No role listings found based on your input filters";
          this.filterError = 404;
          this.displayListings = [];
        });
    },
    handleFilterApplied(selectedOptions) {
      // Handle the applied filter here
      this.selectedCategory = selectedOptions.selectedCategory;
      this.selectedDepartment = selectedOptions.selectedDepartment;
      this.selectedPercentage = selectedOptions.selectedPercentage;

      this.applyFilter(); // Call the method to apply the filter with the updated options
    },

    handleFilterCleared() {
      // Handle the cleared filter here
      this.selectedCategory = [];
      this.selectedDepartment = [];
      this.selectedPercentage = [];
      // Handle other selected options...
      this.clearFilter(); // Call the method to clear the filter with the updated options
    },

    clearFilter() {
      // Clear all filters
      this.selectedCategory = [];
      this.selectedDepartment = [];
      this.selectedPercentage = [];
      this.displayListings = this.rolesFromDb;
      this.filterError = "";
      this.filterErrorMsg = "";
    },

    clearSearch() {
      // Clear search bar
      this.searchQuery = "";
      this.displayListings = this.rolesFromDb;
      this.searchQueryError = null;
      this.searchQueryErrorMsg = "";
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
    RoleFilterCard, // Register the RoleFilterCard component
  },
};
</script>
<style>
/* Styles for mobile screens */
.sidebar {
  display: none;
  /* Hide the sidebar by default */
  /* Add any necessary styles for your sidebar, e.g., background color, width, etc. */
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

  .search_container {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
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
.square-button {
  border-top-right-radius: 10px !important; /* Adjust the value to change the roundness of the top-left corner */
  border-bottom-right-radius: 0px !important;
  border-top-left-radius: 0px !important; /* Adjust the value to change the roundness of the top-left corner */
  border-bottom-left-radius: 0px !important;
  min-width: 56px !important ;
  min-height: 56px !important;
  height: 36px;
  padding: 0 16px;
}

/* .search-container { */
/* position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 1;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative; */
/* } */

.search_container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.search-bar {
  background-color: white;
  border-top-left-radius: 20px; /* Adjust the value to change the roundness of the top-left corner */
  border-bottom-left-radius: 20px;
}
.image_container{
  width: 100%;
  height: 400px;
}
</style>
