<!-- ViewRoleListingsCard.vue -->

<template>
    <div>
      <v-row class="d-flex justify-center">
   
        <!-- display role listings -->
  
        <v-card variant="elevated"
          v-for="role in displayListings"
          :key="role.role_listing.listing_id"
          class="role-card w-100 h-20"
          
          @click="openModal(role)"
        >
          <v-row class="mt-3">
            <v-col class="d-flex justify-start">
              <v-card-title class="text-h5 font-weight-bold" id="role_name"
              >
                {{ role.role_listing.role_name }}
               
              </v-card-title>
            </v-col>
            <v-col class="d-flex justify-end me-2">
              <v-chip color="primary">
                {{ role.role_listing.category }}
              </v-chip>
            </v-col>
          </v-row>
  
          <v-row>
            <v-col col="8" >
              <v-card-text class="d-flex justify-start text-h6">
                <span class="font-weight-bold">Department: </span> &nbsp;
                <span id="listing_department">{{ role.role_listing.department }}</span>
              </v-card-text>
              <v-card-text class="d-flex justify-start text-h6 pt-0 ">
                <span class="font-weight-bold">Deadline: </span>&nbsp;<span
                  >{{ role.role_listing.deadline }}
                </span>
              </v-card-text>
            </v-col>
            <v-col col="4" style="padding-top: 0px">
              <v-card-text>
                <span class="font-weight-bold text-h6">Your Match: </span>
                <v-progress-circular
                  :rotate="180"
                  :size="100"
                  :width="15"
                  :model-value="role.role_skill_match.match_percentage"
                  :color="calculateColor(role.role_skill_match.match_percentage)"              >
                  {{ role.role_skill_match.match_percentage }}%
                </v-progress-circular>
              </v-card-text>
            </v-col>
            <!-- <v-col class="d-flex justify-end me-4 mb-4 align-end"> -->
              <!-- open role description page -->
              <!-- <v-btn
                id="open_modal"
                class="me-3"
                density="default"
                icon="mdi-open-in-new"
                @click="openModal(role)"
              ></v-btn> -->
            <!-- </v-col> -->
          </v-row>
        </v-card>
    
  
        <v-dialog v-model="showModal" hide-overlay>
          <!-- Modal content goes here -->
          <v-card>
            <v-card-actions>
              <v-btn @click="showModal = false">Close</v-btn>
            </v-card-actions>
            <v-container>
              <v-row class="mt-3">
                <v-col class="d-flex justify-start align-center" sm="2">
                  <v-card-title class="text-h5 font-weight-bold">
                    {{ roleToDisplay.role_listing.role_name }}
                  </v-card-title>
                </v-col>  
                <v-col class="d-flex justify-end align-center">
                  <v-chip color="primary">
                    {{ roleToDisplay.role_listing.category }}
                  </v-chip>
                </v-col>
              </v-row>
              <v-row>
                <v-col>
                  <v-card-text class="d-flex justify-start text-h6">
                    <span class="font-weight-bold" id="dept">Department: </span>
                    &nbsp;
                    <span>{{ roleToDisplay.role_listing.department }}</span>
                  </v-card-text>
                  <v-card-text class="d-flex justify-start text-h6 pt-0">
                    <span class="font-weight-bold">Deadline: </span>&nbsp;<span>{{
                      roleToDisplay.role_listing.deadline
                    }}</span>
                  </v-card-text>
                </v-col>
              </v-row>
              <!--<v-row>
                <v-col>
                  <v-card-text class="text-h6">
                    {{ roleToDisplay.role_listing.role_desc }}
                  </v-card-text>
                </v-col>
              </v-row> no desc in this endpoint-->
              <v-row>
                <v-col col="12">
                  <v-card-text>
                    <!-- loop thru requied skils -->
                    <span class="font-weight-bold text-h6"
                      >Skills Required:
                    </span>
                    <v-chip
                      class="me-2"
                      v-for="skill in roleToDisplay.role_skill_match.dont"
                      :key="skill"
                      color="red"
                    >
                      {{ skill }}
                    </v-chip>
                    <br />
                    <span class="font-weight-bold text-h6">Your Skills: </span>
                    <v-chip
                      class="me-2"
                      v-for="skill in roleToDisplay.role_skill_match.have"
                      :key="skill"
                      color="blue"
                    >
                      {{ skill }}
                    </v-chip>
                  </v-card-text>
                </v-col>
                <v-col cols="12">
                  <v-card-text>
                    <span class="font-weight-bold text-h6">Your Match: </span>
                    <v-progress-circular
                      :rotate="180"
                      :size="100"
                      :width="15"
                      :model-value="
                        roleToDisplay.role_skill_match.match_percentage
                      "
                      :color="calculateColor(roleToDisplay.role_skill_match.match_percentage)"   
                    >
                      {{ roleToDisplay.role_skill_match.match_percentage }}%
                    </v-progress-circular>
                  </v-card-text>
                </v-col>
              </v-row>
            </v-container>
          </v-card>
        </v-dialog>
  
        <!-- show success message -->
          <v-dialog v-model="success_model" hide-overlay class="w-50" id="apply_success_alert">
            <!-- Modal content goes here -->
            <v-alert
              id="success_alert"
              color="success"
              icon="$success"
              title="Successful Application"
              text="You have successfully applied for the role!"
            ></v-alert>
          </v-dialog>
  
          <!-- show success message -->
          <v-dialog v-model="failure_model" hide-overlay class="w-50">
            <!-- Modal content goes here -->
            <v-alert
              id="failure_alert"
              color="error"
              icon="$error"
              title="Application Failed"
              text="Your application for the role has failed. Please try again later"
            ></v-alert>
          </v-dialog>
      </v-row>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    props: {
      applied_roles: [], // Receive role listings as props
    },
    data() {
      return {
        showModal: false, // Control the visibility of the full-screen modal
        roleToDisplay: null, // Store the role data for the modal
        success_model: false, // Control the visibility of the full-screen success modal
        failure_model: false, // Control the visibility of the full-screen failure modal
        appliedRole: null,
  
      };
    },
    mounted(){
  
  
    },
  
    computed: {
      displayListings() {
        let filtered = this.applied_roles.filter(
          (role) => role.role_listing.listing_id
        );
        return filtered;
      },
    },
  
    methods: {
      openModal(role) {
        this.roleToDisplay = role;
        this.showModal = true;
      },
      calculateColor(percentage) {
        // Define your color logic based on percentage here
        if (percentage <= 20) {
          return 'red-darken-1';
        } else if (percentage <= 40) {
          return 'orange-darken-1';
        } else if (percentage <= 60) {
          return 'yellow-darken-1';
        } else if (percentage <= 80) {
          return 'light-green-darken-1';
        } else {
          return 'teal-darken-1';
        }
      },
  
    },
  
  };
  </script>
  
  <style>
  /* Add CSS styles for role cards here */
  .role-card {
    border: 1px solid #ccc;
    padding: 16px;
    margin-left: 16px;
    margin-right: 16px;
    margin-top: 16px;
    margin-bottom: 16px;
  
  }
  
  @media (max-width: 768px) {
    .role-card {
      margin-left: 0px !important;
      margin-right: 0px !important;
    }
  }
  
  </style>
  