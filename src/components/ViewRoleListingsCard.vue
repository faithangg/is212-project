<!-- ViewRoleListingsCard.vue -->


<template>
    <div>
        <v-row class="d-flex justify-center">
            <!-- display role listings -->
            <v-card v-for="role in role_listings_with_skill_match" :key="role.role_listing.listing_id" class="role-card w-50 h-25">
                <v-row class="mt-3">
                    <v-col class="d-flex justify-start">
                        <v-card-title class="text-h5 font-weight-bold">
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
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ role.role_listing.department }}</span>
                        </v-card-text>
                        <v-card-text class="d-flex justify-start text-h6 pt-0">
                            <span class="font-weight-bold">Deadline: </span>&nbsp;<span>{{ role.role_listing.deadline }}</span>
                        </v-card-text>
                    </v-col>
                    <v-col class="d-flex justify-end me-4 mb-4 align-end">
                        <!-- open role description page -->
                        <v-btn class="me-3" density="default" icon="mdi-open-in-new" @click="openModal(role)"></v-btn>
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
                                    {{ roleToDisplay.role_listing.role_name }}
                                </v-card-title>
                                <v-chip color="primary">
                                    {{ roleToDisplay.role_listing.category }}
                                </v-chip>
                            </v-col>
                            <v-col cols="auto">
                                <v-btn class="bg-blue-accent-4 text-h6">Apply Now</v-btn>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Department: </span> &nbsp; <span>{{ roleToDisplay.role_listing.department }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6 pt-0">
                                    <span class="font-weight-bold">Deadline: </span>&nbsp;<span>{{ roleToDisplay.role_listing.deadline }}</span>
                                </v-card-text>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="text-h6">
                                    <!-- Lorem ipsum dolor sit amet consectetur adipisicing elit. Delect{{ roleToDisplay.role_listing.deadline }}us magnam aspernatur culpa consequatur corrupti modi quibusdam, vitae mollitia numquam ullam doloremque fuga beatae voluptate molestias itaque dolor soluta molestiae fugit! -->
                                    {{ roleToDisplay.role_listing.role_desc }}
                                </v-card-text>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col >
                                <v-card-text>
                                    <!-- loop thru requied skils -->
                                    <span class="font-weight-bold text-h6">Skills Required: </span>
                                    <v-chip class="me-2" v-for="skill in roleToDisplay.role_skill_match.dont" :key="skill" color="red">
                                        {{ skill }}
                                    </v-chip>
                                    <br>
                                    <span class="font-weight-bold text-h6">Your Skills: </span>
                                    <v-chip class="me-2" v-for="skill in roleToDisplay.role_skill_match.have" :key="skill" color="blue">
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
        role_listings_with_skill_match: [], // Receive role listings as props
    },
    data() {
        return {
            showModal: false, // Control the visibility of the full-screen modal
            roleToDisplay: null, // Store the role data for the modal
        };
    },
    methods: {
        openModal(role) {
            this.roleToDisplay = role;
            this.showModal = true;
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
