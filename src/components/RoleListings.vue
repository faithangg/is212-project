<!-- RoleListings.vue -->


<template>
    <div>
        <div class="text-h3 my-6">
            Role Listings
        </div>
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
                            <span class="font-weight-bold">Department: </span> &nbsp <span>{{ role.department }}</span>
                        </v-card-text>
                        <v-card-text class="d-flex justify-start text-h6 pt-0">
                            <span class="font-weight-bold">Deadline: </span>&nbsp<span>{{ role.deadline }}</span>
                        </v-card-text>
                    </v-col>
                    <v-col class="d-flex justify-end me-4 mb-4 align-end">
                        <!-- open role description page -->
                        <v-btn class="me-3" density="default" icon="mdi-open-in-new" @click="openModal(role)"></v-btn>
                        <!-- edit role -->
                        <v-btn icon v-if="userIsHr"><v-icon>mdi-pencil</v-icon></v-btn>
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
                            <v-col cols="auto">
                                <v-btn class="bg-blue-accent-4 text-h6">Apply Now</v-btn>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="d-flex justify-start text-h6">
                                    <span class="font-weight-bold">Department: </span> &nbsp <span>{{ roleToDisplay.department }}</span>
                                </v-card-text>
                                <v-card-text class="d-flex justify-start text-h6 pt-0">
                                    <span class="font-weight-bold">Deadline: </span>&nbsp<span>{{ roleToDisplay.deadline }}</span>
                                </v-card-text>
                            </v-col>
                        </v-row>
                        <v-row>
                            <v-col>
                                <v-card-text class="text-h6">
                                    Lorem ipsum dolor sit amet consectetur adipisicing elit. Delectus magnam aspernatur culpa consequatur corrupti modi quibusdam, vitae mollitia numquam ullam doloremque fuga beatae voluptate molestias itaque dolor soluta molestiae fugit!
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

                    <!-- <v-card-title>
                        Full-Screen Modal Content
                    </v-card-title>
                    <v-card-text>
                        
                    </v-card-text> -->

                </v-card>
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
        };
    },
    methods: {
        openModal(role) {
            // Store the role data and open the modal
            // axios.get(`http://127.0.0.1:5000/hr/role_listings/${roleId}`)
            //     .then((response) => {
            //         console.log(response.data.data);
            //         
            //         console.log(this.roleToDisplay);
            //     })
            //     .catch((error) => {
            //         console.error('Error fetching role listings:', error);
            //     });
            this.roleToDisplay = role;

            this.showModal = true;
        },
    },

    computed: {
        userIsHr() {
            // Access the user's role from your Vuex store getter
            return this.$store.getters.getUserRole === 'hr';
        },
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
