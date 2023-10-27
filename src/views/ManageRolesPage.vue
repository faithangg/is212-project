// Inside your Vue component
<template>
  <div>
    <!-- <div class="text-h3 mt-9 ">
            Manage Role Listing
        </div>
        <v-btn v-if="userIsHr" to="/manageRolesPage" id="managed">Manage Role Listings</v-btn> -->

    <!-- Search input field -->
    <v-container fluid class="py-0 px-0 position-relative">
      <img
        v-bind:src="require('../assets/office8.jpg')"
        style="width: 100%; height: 300px; margin-top: 5px"
      />
      <!-- Title and Create Roles Btn-->
      <v-container class="search_container">
        <v-row dense>
          <v-col>
            <h1 class="ps-0 pb-4 mt-4 text-center text--white" color="white">
              Manage Role Listings
            </h1>
          </v-col>
        </v-row>
        <!-- Search input field -->
        <v-row class="d-flex mt-3 mb-0 justify-sm-center">
          <v-col cols="10" md="7" class="pe-0">
            <v-text-field
              v-model="searchQuery"
              label="Search by Job Title, Category or Skills"
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

      <!-- Search button -->
    </v-container>

    <v-col cols="11" class="d-flex justify-center justify-sm-end">
      <v-btn
        class="ms-sm-4 mb-4 mt-9 mr-sm-8 ml-4"
        to="/CreateRoleListing"
        id="create_role_listing_btn"
        ><b>Create Role Listing</b></v-btn
      >
    </v-col>
    <EditRoleListingsCard :roleListings="roleListings" />
  </div>
</template>

<script>
import axios from "axios";
import EditRoleListingsCard from "../components/EditRoleListingsCard.vue"; // Import the RoleListings component

export default {
  data() {
    return {
      roleListings: [], // Initialize as an empty array,
      searchQuery: "", // Initialize as an empty string
      searchQueryError: null,
      searchQueryErrorMsg: "", // Initialize as an empty string
    };
  },
  mounted() {
    // Fetch role listings from the API
    axios
      .get("http://127.0.0.1:5000/hr/role_listings")
      .then((response) => {
        // console.log(response.data.data);
        this.rolesFromDb = response.data.data.role_listing;
        this.roleListings = this.rolesFromDb;
      })
      .catch((error) => {
        console.error("Error fetching role listings:", error);
      });
  },

  computed: {},

  methods: {
    performSearch() {
      // This method is called when the Search button is clicked.
      // Fetch role listings from the API
      this.searchQueryError = "";
      this.searchQueryErrorMsg = "";

      if (this.searchQuery == "") {
        this.roleListings = this.rolesFromDb;
        return;
      }
      // Fetch role listings from the API
      // var userId = this.getUserId;
      console.log("performSearch() called");
      axios
        .get(
          `http://127.0.0.1:5000/hr/browse_role_listings/${this.searchQuery}`
        )
        .then((response) => {
          console.log(response.data.data);

          this.roleListings =
            response.data.data.role_listings;
        })
        .catch((error) => {
          console.error("Error fetching role listings:", error);

          console.log(error.response.status);

          if (error.response.status == 404) {
            this.searchQueryErrorMsg = "No role listings found";
            this.searchQueryError = 404;
            this.roleListings = [];
          } else if (error.response.status == 400) {
            this.searchQueryErrorMsg =
              "Invalid search query: No special characters or numbers allowed.";
            this.searchQueryError = 400;
            this.roleListings = [];
          }
        });
    },
    clearSearch() {
      // Clear search bar
      this.searchQuery = "";
      this.roleListings = this.rolesFromDb;
      this.searchQueryError = null;
      this.searchQueryErrorMsg = "";
    },
  },

  components: {
    EditRoleListingsCard, // Register the RoleListings component
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

.search-bar {
  background-color: white;
  border-top-left-radius: 20px; /* Adjust the value to change the roundness of the top-left corner */
  border-bottom-left-radius: 20px;
}
</style>
