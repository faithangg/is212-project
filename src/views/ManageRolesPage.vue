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
      </v-container>

      <!-- Search button -->
    </v-container>

    <v-col cols="11" class="d-flex justify-end">
      <v-btn
        class="ms-4 mb-4 mt-9 mr-8"
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
      roleListings: [], // Initialize as an empty array
      searchQuery: "", // Initialize as an empty string
    };
  },
  mounted() {
    // Fetch role listings from the API
    axios
      .get("http://127.0.0.1:5000/hr/role_listings")
      .then((response) => {
        console.log(response.data.data);

        this.roleListings = response.data.data.role_listing;
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
      // axios.get('http://
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
