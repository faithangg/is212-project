<template>
  <div class="profile-page">
    <v-container fluid class="py-0 px-0 position-absolute">
      <!-- Background Image -->
      <div style="z-index: -1; position: absolute; width: 100%">
        <img
          v-bind:src="require('../assets/office12.jpg')"
          style="width: 100%; height: 300px"
        />
      </div>
      <div style="position: relative; z-index: 1">
        <v-row>
          <v-col>
            <h1 class="py-8 mt-4 text-center text--white" color="white">
              Profile
            </h1>
          </v-col>
        </v-row>
        <!-- Profile Image -->
        <v-row class="d-flex pt-10">
          <v-col cols="12" md="4">
            <img
              v-bind:src="require('../assets/profile1.jpg')"
              style="width: 250px; height: 250px; border-radius: 50%"
            />
          </v-col>
          <!-- Profile Details Card -->
          <v-col cols="12" md="8" >
            <v-card
              class="profile-details-card w-60 mx-10 rounded-xl rounded-be-0 text-left"
              style="min-height: 250px; height: auto;background-color:;" 
            >
              <v-card-text class="text-h7 text-md-h6 py-8 ">
                <v-row>
                  <v-col cols="12" md="6" class="pt-0 pt-md-3" 
                    ><span
                      ><strong>Name:</strong> {{ staff_fname }}
                      {{ staff_lname }}</span
                    ></v-col
                  >
                  <v-col cols="12" md="6" class="pt-0 pt-md-3"
                    ><span><strong>Email:</strong> {{ email }}</span></v-col
                  >
                </v-row>
                <v-row>
                  <v-col cols="12" md="6" class="pt-0 pt-md-3"
                    ><span><strong>Country:</strong> {{ country }}</span></v-col
                  >
                  <v-col cols="12" md="6" class="pt-0 pt-md-3"
                    ><span><strong>Department:</strong> {{ dept }}</span></v-col
                  >
                </v-row>
                <v-row>
                  <v-col cols="12" md="6" class="pt-0 pt-md-3"
                    ><span><strong>Role:</strong> {{ role }}</span></v-col
                  >
                  <v-col cols="12" md="6" class="pt-0 pt-md-3"
                    ><span><strong>Staff ID:</strong> {{ userId }}</span></v-col
                  >
                </v-row>
                <v-row>
                  <v-col class="pt-0 pt-md-3">
                    <span><strong>Skills Held:</strong></span>
                    <span class="d-flex flex-wrap mt-2 ">
                      <v-chip
                        class="me-2 my-1 text-md-h7"
                        v-for="skill in skills"
                        :key="skill"
                        color="blue"
                      >
                        {{ skill }}
                      </v-chip>
                    </span>
                  </v-col>
                </v-row>
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>

        <v-row>
          <v-col>
            <h1 class="py-0 mt-4 text-center text--white" color="white">
              Jobs applied
            </h1>
          </v-col>
        </v-row>
        <v-container class="d-flex justify-center pb-0">
          <!--<v-card class="applied-roles-card">
            <v-scroll-x>
              <v-scroll-y>-->
                <RolesAppliedCard :applied_roles="applied_roles" />
              <!--</v-scroll-y>
            </v-scroll-x>
          </v-card>-->
        </v-container>
              
      </div>
    </v-container>
  </div>
</template>

<script>
import axios from "axios";
import RolesAppliedCard from "../components/RolesAppliedCard.vue";
export default {
  data() {
    return {
      result: [],
      applied_roles: [],
      userId: null,
      country: null,
      dept: null,
      email: null,
      role: null,
      staff_fname: null,
      staff_lname: null,
      skills: [],
    };
  },
  mounted() {
    this.userId = this.getUserId;
    axios
      .get(`http://127.0.0.1:5000/staff/profile/${this.userId}`)
      .then((response) => {
        this.result = response.data.data;
        console.log(this.result);
        this.applied_roles = this.result.applied_roles;
        this.country = this.result.staff_details.info.country;
        this.dept = this.result.staff_details.info.dept;
        this.email = this.result.staff_details.info.email;
        this.role = this.result.staff_details.info.role;
        this.staff_fname = this.result.staff_details.info.staff_fname;
        this.staff_lname = this.result.staff_details.info.staff_lname;
        this.skills = this.result.staff_details.skills;
      })
      .catch((error) => {
        console.error("Error fetching applicants:", error);
      });
  },
  computed: {
    getUserId() {
      // Access the user's role from your Vuex store getter
      return this.$store.getters.getUserId;
    },
  },
  components: {
    RolesAppliedCard,
  },
};
</script>

<style scoped>
.applied-roles-card {
  max-height: 500px;
  width: 70%;
  overflow-y: auto;
  margin-top: 20px;
  padding: 20px;
  border-radius: 10px;
  /*box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);*/
}
</style>
