<!-- EditRoleListingCard.vue -->


<template>
    <div>
        <v-row class="d-flex justify-center">
            <!-- display role listings -->
            <v-card v-for="role in roleListings" :key="role.listing_id" class="role-cards w-75 h-20" variant="elevated">
                <v-row class="mt-3">
                    <v-col class="d-flex justify-start">
                        <v-card-title class="text-h5 font-weight-bold">
                            {{ role.role_name }}
                        </v-card-title>
                    </v-col>
                    <v-col class="d-flex justify-end me-2">
                        <v-chip color="primary">
                            {{ role.category }}
                        </v-chip>
                    </v-col>
                </v-row>

                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ role.department }}</span>
                        </v-card-text>
                        <v-card-text class="d-flex justify-start text-h6 pt-0">
                            <span class="font-weight-bold">Deadline: </span>&nbsp;<span :style="isDeadlinePassed(role.deadline)">{{ role.deadline }}</span>
                        </v-card-text>
                    </v-col>
                    <v-col class="d-flex justify-end me-4 mb-4 align-end">
                        <!-- open role description page -->
                        <v-btn @click="viewApplicants(role.listing_id)" class="me-3" id="view_applicants" icon round>
                            <v-icon>mdi-account-multiple</v-icon>
                            <v-tooltip activator="parent" location="top">View Applicants</v-tooltip>
                        </v-btn>
                        <v-btn class="me-3" density="default" icon round @click="openModal(role)" id="open_modal">
                            <v-icon>mdi-open-in-new</v-icon>
                            <v-tooltip activator="parent" location="top">Open Modal</v-tooltip>
                        </v-btn>
                        <!-- edit role -->
                        <v-btn @click="editRole(role.listing_id)" icon round>
                            <v-icon id="edit">mdi-pencil</v-icon>
                            <v-tooltip activator="parent" location="top">Edit Listing</v-tooltip>
                        </v-btn>
                    </v-col>
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
                            <v-col class="d-flex justify-start align-center">
                                <v-card-title class="text-h5 font-weight-bold">
                                    {{ roleToDisplay.role_name }}
                                </v-card-title>
                            </v-col>
                            <v-col class="d-flex justify-end me-2" cols="12" sm="4">
                                <v-chip color="primary">
                                    {{ roleToDisplay.category }}
                                </v-chip>
                            </v-col>
                            <v-col class="d-flex justify-end  me-4 mb-4 ">
                                <v-btn @click="editRole(roleToDisplay.listing_id)" icon><v-icon id="edit">mdi-pencil</v-icon>                             <v-tooltip activator="parent" location="top">Edit Listing</v-tooltip>  
                                </v-btn>

                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ roleToDisplay.department }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6 pt-0">
                                    <span class="font-weight-bold">Deadline: </span>&nbsp;<span :style="isDeadlinePassed(roleToDisplay.deadline)">{{ roleToDisplay.deadline }}</span>
                                </v-card-text>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="text-h6">
                                    {{ roleToDisplay.role_desc }}
                                </v-card-text>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col >
                                <v-card-text>
                                    <!-- loop thru requied skils -->
                                    <span class="font-weight-bold text-h6">Skills Required: </span>
                                    <v-chip class="me-2" v-for="skill in roleToDisplay.skills_required" :key="skill" color="blue">
                                        {{ skill }}
                                    </v-chip>
                                    
                                </v-card-text>
                            </v-col>
                        </v-row>
                    </v-container>

                </v-card>
            </v-dialog>
            <v-dialog v-model="showAlert" hide-overlay class="w-50" id="no_applicants_alert">
                <v-alert
                    color="blue"
                    outlined
                    icon="$info"
                    title="Alert"
                    text="No applicants for this role."
                    
                ></v-alert>
            </v-dialog>
        </v-row>
    </div>
</template>

<script>
import axios from 'axios';
export default {
    props: {
        roleListings: [], // Receive role listings as props
    },
    data() {
        return {
            showModal: false, // Control the visibility of the full-screen modal
            roleToDisplay: null, // Store the role data for the modal
            deadlineStyle: {
                color: 'red',
            },
            showAlert: false,
        };
    },
    methods: {
        openModal(role) {
            this.roleToDisplay = role;
            this.showModal = true;
        },
        async viewApplicants(listing_id) {
            // Fetch the number of applicants for the specific role using the listing_id
            axios.get(`http://127.0.0.1:5000/hr/role_applicants/${listing_id}`)
                .then((response) => {
                    console.log(response.data);
                    // Navigate to the RoleApplicantsPage
                    this.$router.replace({ 
                        name: 'RoleApplicantsPage', 
                        query: { listing_id: listing_id } 
                    });
                })
                .catch((error) => {
                    if (error.response.status === 404) {
                        // Display an error message using a Vue Toast or Snackbar
                        this.showAlert = true;
                        setTimeout(() => {
                            this.showAlert= false;
                            }, 3000);
                        //alert('No applicants for this role.');
                    } else {
                        // Handle other errors or display a generic error message
                        error('An error occurred while fetching the applicants.');
                    }
                });
            
        },
        editRole(listing_id) {
            // Navigate to the page where you can edit the specific role
            this.$router.replace({ 
                name: 'UpdateRoleListing', 
                query: { listing_id: listing_id } 
            });
        },
        isDeadlinePassed(date) {
            // Check if the deadline has passed
            // Return true if the deadline has passed, false otherwise
            console.log(new Date());
            console.log(new Date(date) > new Date());

            console.log(date);
            return (new Date(date) < new Date()) ? {color: 'red'} : '';
        },
    },

    computed: {

    },
};
</script>

<style>
/* Add CSS styles for role cards here */
.role-cards {
  border: 1px solid #ccc;
  padding: 16px;
  margin-left: 16px;
  margin-right: 16px;
  margin-top: 16px;
  margin-bottom: 16px;

}

@media (max-width: 768px) {
  .role-cards {
    margin-left: 0px !important;
    margin-right: 0px !important;
  }
}
</style>
