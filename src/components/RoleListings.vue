<!-- RoleListings.vue -->


<template>
    <div>
        <div class="text-h3 my-6">
            Role Listings
        </div>
        <v-row class="d-flex justify-center">
            <!-- <v-col  cols="12" md="6" lg="4"> -->
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
                    <v-col >
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Department: </span> &nbsp <span>{{ role.department }}</span> 
                        </v-card-text>
                        <v-card-text class="d-flex justify-start text-h6 pt-0">
                            <span class="font-weight-bold">Deadline: </span>&nbsp<span>{{ role.deadline }}</span> 
                        </v-card-text>
                    </v-col>
                    <v-col class="d-flex justify-end me-4 mb-4 align-end">
                        <!-- open role description page -->
                        <v-btn class="me-3" density="default" icon="mdi-open-in-new"></v-btn>
                        <!-- edit role -->
                        <v-btn icon v-if="userIsHr"><v-icon>mdi-pencil</v-icon></v-btn>
                    </v-col>
                </v-row>
                <!-- You can add more card content here -->
            </v-card>
            <!-- </v-col> -->
        </v-row>
    </div>
</template>

<script>

export default {
    props: {
        roleListings: Array, // Receive role listings as props
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
