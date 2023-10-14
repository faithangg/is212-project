<template>
  
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
</template>

<script>
import axios from 'axios';

export default {
  props:['categoryItems', 'departmentItems'],

  data() {
    return {
      // rolesFromDb: [], // Initialize as an empty array
      // displayListings: [],
      // searchQuery: '', // Initialize as an empty string
      // searchQueryError: null,
      filterError: null,
      // searchQueryErrorMsg: '', // Initialize as an empty string
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
    // var userId = this.getUserId;

    // axios.get(`http://127.0.0.1:5000/staff/role_listings/${userId}`)
    //   .then((response) => {
    //     console.log(response.data.data);

    //     this.rolesFromDb = response.data.data.role_listings_with_skill_match;
    //     this.displayListings = this.rolesFromDb;
    //     console.log(this.role_listings_with_skill_match);
    //     console.log(this.role_listings_with_skill_match[0].role_listing);
    //   })
    //   .catch((error) => {
    //     console.error('Error fetching role listings:', error);
    //   });

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

  // computed: {
  //   userIsHr() {
  //     // Access the user's role from your Vuex store getter
  //     return this.$store.getters.getUserRole === 'hr';
  //   },

  //   getUserId() {
  //     // Access the user's role from your Vuex store getter
  //     return this.$store.getters.getUserId;
  //   },
  //   isMobileScreen() {
  //     return window.innerWidth <= 768; // Adjust the width as needed
  //   },

  // },

  methods: {
    // performSearch() {
    //   // This method is called when the Search button is clicked.
    //   this.searchQueryError = '';
    //   this.searchQueryErrorMsg = '';
    //   this.filterError = '';
    //   this.filterErrorMsg = '';

    //   if (this.searchQuery == '') {
    //     this.displayListings = this.rolesFromDb;
    //     return;
    //   }
    //   // Fetch role listings from the API
    //   var userId = this.getUserId;

    //   axios.get(`http://127.0.0.1:5000/staff/browse_role_listings/${userId}/${this.searchQuery}`)
    //     .then((response) => {
    //       console.log(response.data.data);

    //       this.displayListings = response.data.data.role_listings_with_skill_match;
    //     })
    //     .catch((error) => {
    //       console.error('Error fetching role listings:', error);

    //       console.log(error.response.status);

    //       if (error.response.status == 404) {
    //         this.searchQueryErrorMsg = 'No role listings found';
    //         this.searchQueryError = 404;
    //         this.displayListings = [];
    //       }
    //       else if (error.response.status == 400) {
    //         this.searchQueryErrorMsg = 'Invalid search query - No special characters';
    //         this.searchQueryError = 400;
    //         this.displayListings = [];
    //       }
    //     });
    // },
    applyFilter() {
            // Handle the filter application here
            this.$emit('filter-applied', {
        selectedCategory: this.selectedCategory,
        selectedDepartment: this.selectedDepartment,
        selectedPercentage: this.selectedPercentage,
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
      this.$emit('filter-cleared');

    },

    // clearSearch() {
    //   // Clear search bar
    //   this.searchQuery = '';
    //   this.displayListings = this.rolesFromDb;
    //   this.searchQueryError = null;
    //   this.searchQueryErrorMsg = '';
    // },
    showFilter() {
      this.showFilterModal = true; // Show the filter modal
    },

    hideFilterModal() {
      this.showFilterModal = false; // Hide the filter modal
    },
  },



};
</script>