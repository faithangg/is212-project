<template>
    <v-app>
        <v-content>
            <v-card max-width="448" class="mx-auto mt-9 text-center">
                <!-- <v-layout>     -->
                <v-main>
                    <v-container fluid>
                        <v-row dense>
                            <v-card-title>Login</v-card-title>
                            <v-card-text>
                                <v-text-field 
                                label="Staff ID" 
                                required prepend-icon="mdi-account-circle" 
                                v-model="staffID"
                                id="staffId"
                                variant="outlined"
                                ></v-text-field>

                                <v-text-field 
                                label="Password" 
                                required :type="showPassword ? 'text' : 'password'"
                                prepend-icon="mdi-lock" 
                                :append-icon="showPassword ? 'mdi-eye-' : 'mdi-eye-off'"
                                @click:append="showPassword = !showPassword" 
                                v-model="password" 
                                id="password"
                                variant="outlined"
                                ></v-text-field>
                                <!-- <v-btn>Login</v-btn> -->
                            </v-card-text>
                        </v-row>
                        <v-dialog v-model="errorDialog" hide-overlay class="w-75">

                        <v-alert
                            v-if="errorMessage !== ''"
                            id="failure_alert"
                            color="error"
                            icon="$error"
                            title="Login Failed"
                            text="The password or staff id is incorrect"
                        >
                        </v-alert>
                        </v-dialog>

                        <v-divider></v-divider>
                        <v-card-actions>
                            <v-btn type="submit" class="mt-4" color="teal" @click="login()" id="login">Login</v-btn>
                        </v-card-actions>

                    </v-container>
                </v-main>
                <!-- </v-layout> -->
            </v-card>
        </v-content>
    </v-app>
</template>




<script>
import { mapActions } from 'vuex';

export default {
    name: "LoginPage",
    data() {
        return {
            showPassword: false,
            staffID: '',
            password: '',
            errorDialog: false,
            errorMessage: '',
            failure_model: false, // Control the visibility of the full-screen failure modal

        }
    },
    methods: {
        ...mapActions(['authenticate']), // Map the login action from the store to the login method
        showErrorDialog(message) {
            this.errorMessage = message;
            this.errorDialog = true;
            setTimeout(() => {
                this.errorDialog = false;
            }, 3000);
            },

        async login() {

            const userData = {
                staffID: this.staffID,
                password: this.password
            }

            const success = await this.authenticate(userData); // Call the login action from the store

            if (success) {
                this.$router.replace({ name: "ViewRolesPage" });
            } else {
                this.showErrorDialog('The password or staff id is incorrect');
            }

        },
    }
}
</script>

