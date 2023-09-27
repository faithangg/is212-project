// Inside your Vue component
<template>
  <div>
    <!-- Display role listings using the RoleListings component -->
    <RoleListings :roleListings="roleListings" />
  </div>
</template>

<script>
import axios from 'axios';   
import RoleListings from '../components/RoleListings.vue'; // Import the RoleListings component

export default {
  data() {
    return {
      roleListings: [], // Initialize as an empty array
    };
  },
  mounted() {
    // Fetch role listings from the API
    axios.get('http://127.0.0.1:5000/hr/role_listings') 
      .then((response) => {
        console.log(response.data.data);
        this.roleListings = response.data.data.role_listing; // Set the retrieved data to roleListings
      })
      .catch((error) => {
        console.error('Error fetching role listings:', error);
      });
    
  },
  
  components: {
    RoleListings, // Register the RoleListings component
  },


};
</script>
