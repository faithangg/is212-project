<template>
    
    <div class="profile-page">
        <v-container fluid class="py-0 px-0 position-relative">
          <v-container fluid class="position-absolute d-flex justify-center" >
              <img
                  v-bind:src="require('../assets/profile.png')"
                  style=
                  "width: 200px;
                  height: 200px;
                  border-radius:50%;
                  position:absolute;
                  z-index:1;"
              />
            </v-container>
            <img
                v-bind:src="require('../assets/office12.jpg')"
                style="width: 100%; height: 300px;z-index: -1;"
            /> 
            
            <v-container class="d-flex justify-center pb-0">
                <v-card class="applied-roles-card">
                    <v-scroll-x>
                        <v-scroll-y>
                            <RolesAppliedCard :applied_roles="applied_roles" />
                        </v-scroll-y>
                    </v-scroll-x>
                </v-card>
            </v-container>
        </v-container>

    </div>
    
    
</template>

<script>
import axios from "axios";
import RolesAppliedCard from "../components/RolesAppliedCard.vue";
export default {
    data() {
        return {
            applicantsFromDb: [],
            listing_id: null, 
            role_applicants: [],
            deadline: null,
            department: null,
            role_name: null,
            total_applicants: null,
            userId:null,
            applied_roles:[]
        }
    },
  mounted() {
    this.userId = this.getUserId;
    axios
      .get(`http://127.0.0.1:5000/staff/profile/${this.userId}`)
      .then((response) => {
        console.log(response.data.data.applied_roles);
        this.applied_roles = response.data.data.applied_roles;
      })
      .catch((error) => {
        console.error("Error fetching applicants:", error);
      });
  },
  computed:{
    getUserId() {
      // Access the user's role from your Vuex store getter
      return this.$store.getters.getUserId;
    },
  },
  components: {
    RolesAppliedCard
  },

}
</script>

<style scoped>
.top-card {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1; /* Ensure the top card is above the image */
  /* Add any additional styling for the top card here */
}
.applied-roles-card {
    max-height: 400px;
    width:70%;
    overflow-y: auto;
    margin-top: 20px;
    padding: 20px;
    border-radius: 10px;
    /*box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);*/
}
</style>
