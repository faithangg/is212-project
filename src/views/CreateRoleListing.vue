<template>
<v-card max-width="948" class="mx-auto" color="grey-lighten-3">
    <v-layout>    
        <v-main>
            <div data-aos="fade-up" data-aos-duration="1000">
                <v-container fluid>
                    <form @submit.prevent="submit">
                        <v-card elevation="2" class="pa-14">
                            <v-row dense>
                                <v-col cols="3">
                                    <v-btn class="ml-12 mt-2" prepend-icon="mdi-arrow-left" variant="text" to="/ManageRolesPage">
                                        Back
                                    </v-btn>
                                </v-col>
                                <v-col cols="9">
                                    <h1 class="text-left ml-12 pb-8">Create A Role Listing</h1>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Role*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="role_name" label="Select a role to populate description and skills required" variant="outlined" required :items="this.role_name_list" @update:model-value="display_description"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Description*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-textarea type="text" v-model="description" variant="outlined" readonly required></v-textarea>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Skills Required*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-chip-group row class="mb-4">
                                        <v-chip
                                            v-for="(skill, index) in skills"
                                            :key="index"
                                            color="default"
                                            size="large"
                                            label
                                        >
                                            {{ skill }}
                                        </v-chip>
                                    </v-chip-group>                      
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Department*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="departments" label="Select department" variant="outlined" required :items="this.departments_list"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Category*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="categories" label="Select category" variant="outlined" required :items="this.categories_list"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Application Deadline*
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field
                                        type="date"    
                                        v-model="selectedDateFormatted"
                                        label="Select a Date"
                                        variant="outlined" 
                                        required
                                        :min="minDate"
                                    ></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row dense class="mx-16">
                                <!-- Error Message -->
                                <v-alert
                                    v-if="errorMessage"
                                    color="error"
                                    icon="mdi-alert"
                                    >
                                    {{ errorMessage }}
                                </v-alert>
                            </v-row>
                            <v-row dense class="mx-16">
                                <v-col>
                                    <v-btn
                                        block
                                        class="mt-8 mr-6"
                                        color="default"
                                        size="large"
                                        variant="tonal"
                                        :disabled="!isFormFilledAtAll"
                                        @click="reset_form()"
                                    >
                                        <b>Reset</b>
                                    </v-btn>
                                </v-col>
                                <v-col>
                                    <v-btn
                                        block
                                        class="mt-8 ml-6"
                                        color="teal-lighten-1"
                                        size="large"
                                        variant="tonal"
                                        :disabled="!isFieldsNotEmpty"
                                        @click="create_role()"
                                    >
                                        <b>Create</b>
                                    </v-btn>
                                </v-col>
                            </v-row>
                            <!-- show success message -->
                            <v-dialog v-model="success_model" hide-overlay class="w-50">
                                <!-- Modal content goes here -->
                                <v-alert
                                    id="success_alert"
                                    color="success"
                                    icon="$success"
                                    title="New role created successfully."
                                ></v-alert>
                            </v-dialog>
                        </v-card>
                    </form>
                </v-container>
            </div>            
        </v-main>    
    </v-layout>
</v-card>
</template>

<script>
import axios from 'axios';

export default {
    name: "CreateRoleListing",
    data() {
        return {
            role_name: "",
            role_name_list: [],
            description: "",
            departments: "",
            departments_list: [],
            categories: "",
            categories_list: [],
            skills: [],
            selectedDate: new Date(), // Initialize with the current date
            selectedDateFormatted: '', // Displayed date in the text field
            minDate: this.showDateinSGT(), // Minimum date allowed to select
            errorMessage: '',          // Error message to display to the user
            success_model: false, // Control the visibility of the full-screen success modal
        };
    },
    async created() {
        // Fetch roles from the API
        await this.get_roles();
        await this.get_departments();
        await this.get_categories();
        await this.showDateinSGT();
    },
    methods: {
        showDateinSGT() {
            // Get today's date in Singapore Time Zone
            // Specify the desired time zone (Singapore Time Zone)
            const timeZone = "Asia/Singapore";

            // Create a DateTimeFormat object with the specified time zone
            const dateFormatter = new Intl.DateTimeFormat("en-US", {
            timeZone,
            year: "numeric",
            month: "numeric",
            day: "numeric",
            });

            // Get today's date in the specified time zone
            const singaporeDate = dateFormatter.format(new Date());

            // Split the input string by '/'
            const parts = singaporeDate.split('/');

            // Rearrange the parts to the desired format (yyyy-mm-dd)
            const singaporeDateFormatted = `${parts[2]}-${parts[0].padStart(2, '0')}-${parts[1].padStart(2, '0')}`;

            return singaporeDateFormatted;
            // console.log(singaporeDateFormatted);
        },
        //get roles
        async get_roles() {
            try{
                console.log("trying get_roles()");

                const response = await axios.get('http://127.0.0.1:5000/hr/get_role_names');
                console.log("response", response);

                // Save role names to role_name
                this.role_name_list=response.data;
                //console.log("this.role_name", this.role_name);

            } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error fetching roles:', error);
            }

        },
        async display_description(){
            try{
                console.log("trying display_description()");

                const response = await axios.get('http://127.0.0.1:5000/hr//role/'+this.role_name+'/description');
                console.log("response", response);

                // Save description to a variable
                this.description=response.data.description;
                // console.log("this.description", this.description);

                // Get skills
                this.display_skills();
                } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error fetching description:', error);
                }
        },
        async display_skills(){
            try{
                console.log("trying display_skills()");

                const response = await axios.get('http://127.0.0.1:5000/hr/get_role_skills/'+this.role_name);
                console.log("response", response);

                // Save skills to a variable
                this.skills=response.data.skills_required;
                // console.log("this.skills", this.skills);

                } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error fetching skills:', error);
                }
        },
        async get_departments() {
            try{
                console.log("trying get_departments()");

                const response = await axios.get('http://127.0.0.1:5000/hr/departments');
                console.log("response", response.data);

                // Save departments to departments
                this.departments_list=response.data;
                // console.log("this.departments_list", this.departments_list);

            } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error fetching departments:', error);
            }

        },
        
        async get_categories() {
            try{
                console.log("trying get_categories()");

                const response = await axios.get('http://127.0.0.1:5000/hr/categories');
                console.log("response", response);

                this.categories_list=response.data;
                // console.log("this.categories_list", this.categories_list);

            } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error fetching categories:', error);
            }

        },
        async create_role() {
            try{
                console.log("trying create_role()");
                // console.log("to send:", this.role_name, this.departments, this.categories, this.selectedDateFormatted);

                const response = await axios.post(`http://127.0.0.1:5000/hr/create_role_listing`, {role_name:this.role_name, department:this.departments, category:this.categories, deadline:this.selectedDateFormatted});
                console.log("response", response);
                if (response.status === 201) {
                    // Role created successfully
                    this.errorMessage = "";

                    // Reset the form and set timeout to hide the success message
                    this.success_model = true;
                    this.role_name = "";
                    this.departments = "";
                    this.categories = "";
                    this.selectedDateFormatted = "";
                    this.description = "";
                    this.skills = [];
                    this.get_roles();
                    this.get_departments();
                    this.get_categories();
                    setTimeout(() => {
                        this.success_model = false;
                    }, 10000);
                }
            } catch (error) {
                if (error.response && error.response.status === 400) {
                    // duplicate roles detected
                    // Display an error message to the user
                    console.error("Error creating roles:", error); // Log the error response
                    this.errorMessage = "This role already exists. Please check your input and try again.";
                    console.log("errorMessage", this.errorMessage);
                } else {
                    // Errors when calling the service; such as network error, service offline, etc
                    console.log('Network error or service offline:', error);
                    // Display a generic error message
                    this.errorMessage = "An error occurred while communicating with the server. Please try again later.";
                    console.log("errorMessage", this.errorMessage);
                }
            }

        },
        reset_form() {
            // Reset the form
            this.role_name = "";
            this.departments = "";
            this.categories = "";
            this.selectedDateFormatted = "";
            this.description = "";
            this.skills = [];
            this.errorMessage = "";
        },
    },
    computed: {
        isFieldsNotEmpty() {
            // Check if all required fields are valid before enabling the create button
            return !!this.role_name && !!this.departments && !!this.categories && !!this.selectedDateFormatted;
        },
        isFormFilledAtAll() {
            // Check if any of the fields are not empty before enabling the reset button
            return this.role_name || this.departments || this.categories || this.selectedDateFormatted;
        },
    },
}
</script>

