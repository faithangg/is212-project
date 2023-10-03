<!-- ViewRoleListingsCard.vue -->


<template>
    <div>
        <v-row class="d-flex justify-center">
            <!-- display role listings -->
            <v-card v-for="role in roleListings" :key="role.listing_id" class="role-card w-50 h-25">
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
                        <v-btn @click="viewApplicants(role.listing_id)" class="me-3" id="view_applicants" icon="mdi-account-multiple"></v-btn>
                        <v-btn class="me-3" density="default" icon="mdi-open-in-new" @click="openModal(role)" id="open_modal"></v-btn>
                        <!-- edit role -->
                        <v-btn icon><v-icon id="edit">mdi-pencil</v-icon></v-btn>
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
                                <v-chip color="primary">
                                    {{ roleToDisplay.category }}
                                </v-chip>
                            </v-col>
                            <v-col class="d-flex justify-end">
                                <v-btn icon><v-icon id="edit">mdi-pencil</v-icon></v-btn>
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
                                    <!-- Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus magnam aspernatur culpa consequatur corrupti modi quibusdam, vitae mollitia numquam ullam doloremque fuga beatae voluptate molestias itaque dolor soluta molestiae fugit! -->
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
        </v-row>
    </div>
</template>

<script>

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
        };
    },
    methods: {
        openModal(role) {
            this.roleToDisplay = role;
            this.showModal = true;
        },
        viewApplicants(listing_id) {
            // Navigate to the page where you can view all job applicants for the specific role
            // You can use Vue Router's push method or any other method you prefer
            this.$router.replace({ 
                name: 'RoleApplicantsPage', 
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
.role-card {
    border: 1px solid #ccc;
    padding: 16px;
    margin: 16px;
}
</style>
