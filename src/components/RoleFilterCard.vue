<template>
  
  <v-card-text>
    <!-- Filter section content here -->
    <!-- ... -->
    <v-card class="mx-auto" flat>

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
      filterError: null,
      filterErrorMsg: '',
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

  methods: {
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
    showFilter() {
      this.showFilterModal = true; // Show the filter modal
    },
    hideFilterModal() {
      this.showFilterModal = false; // Hide the filter modal
    },
  },

};
</script>