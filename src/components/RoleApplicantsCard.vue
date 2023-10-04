
<template>
    <div>
        <v-row class="d-flex justify-center">
            <!-- display role listings -->
            <v-card v-for="applicant in role_applicants" :key="applicant.email" class="role-card w-50 h-25">
                <v-row>
                    <v-col><v-row class="my-0 py-1 px-2">
                            <v-col class="d-flex justify-start">
                                <v-card-title class="text-h7 font-weight-bold">
                                    {{ applicant.name }}
                                </v-card-title>
                            </v-col>
                        </v-row>
                        <v-row class="pt-0 mt-0">
                            <v-col>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Email: </span>&nbsp;<span>{{ applicant.email }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ applicant.department }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Application Date: </span> &nbsp; <span>{{ applicant.application_date }}</span>
                                </v-card-text>
                                
                            </v-col>
                            <!--<v-col class="d-flex justify-end me-4 mb-4 align-end">
                                
                                <v-btn @click="viewApplicants(role.listing_id)" class="me-3" id="view_applicants" icon="mdi-account-multiple"></v-btn>
                                <v-btn class="me-3" density="default" icon="mdi-open-in-new" @click="openModal(role)" id="open_modal"></v-btn>
                                
                                <v-btn icon><v-icon id="edit">mdi-pencil</v-icon></v-btn>
                            </v-col>-->
                        </v-row>
                    </v-col>
                    <v-col>
                        <v-card-text>
                        <span class="font-weight-bold text-h6">Your Match: </span>
                        <v-progress-circular
                            :rotate="180"
                            :size="100"
                            :width="15"
                            :model-value="applicant.match_percentage"
                            color="teal"
                        >
                            {{ applicant.match_percentage }}%
                        </v-progress-circular>
                        </v-card-text>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Skills held: </span>&nbsp;
                                <v-chip
                            class="me-2"
                            v-for="skill in applicant.skills_have"
                            :key="skill"
                            color="red">
                            {{ skill }}
                                </v-chip>
                        </v-card-text>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Skills missing: </span>&nbsp;
                            <v-chip
                                class="me-2"
                                v-for="skill in applicant.skills_dont"
                                :key="skill"
                                color="blue">
                                {{ skill }}
                            </v-chip>
                        </v-card-text>
                    </v-col>
                </v-row>
            </v-card>
            <!-- Modal content goes here -->
            <!--
            <v-dialog v-model="showModal" hide-overlay>

                
                <v-card>
                    <v-card-actions>
                        <v-btn @click="showModal = false">Close</v-btn>
                    </v-card-actions>
                    <v-container>
                        <v-row class="mt-3">
                            <v-col class="d-flex justify-start align-center">
                                <v-card-title class="text-h6 font-weight-bold">
                                    {{ roleToDisplay.role_name }}
                                </v-card-title>
                                <v-chip color="primary">
                                    {{ roleToDisplay.category }}
                                </v-chip>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ roleToDisplay.department }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6 pt-0">
                                    <span class="font-weight-bold">Deadline: </span>&nbsp;<span>{{ roleToDisplay.deadline }}</span>
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
                                    <span class="font-weight-bold text-h6">Skills Required: </span>
                                    <v-chip class="me-2" v-for="skill in roleToDisplay.skills_required" :key="skill" color="blue">
                                        {{ skill }}
                                    </v-chip>
                                    
                                </v-card-text>
                            </v-col>
                        </v-row>
                    </v-container>

                </v-card>
            </v-dialog>-->
        </v-row>
    </div>
</template>

<script>

export default {
    props: {
        role_applicants: [], // Receive role applicants as props

    },
    data() {
        return {
            //showModal: false, // Control the visibility of the full-screen modal
            //roleToDisplay: null, // Store the role data for the modal
            
        };
    },
    methods: {
        //openModal(role) {
            //this.roleToDisplay = role;
            //this.showModal = true;
        //},
        
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
