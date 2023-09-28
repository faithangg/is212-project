<template>
<v-card max-width="948" class="mx-auto" color="grey-lighten-3">
    <v-layout>    
        <v-main>
            <div data-aos="fade-up" data-aos-duration="1000">
                <v-container fluid>
                    <form @submit.prevent="submit">
                        <v-card elevation="2" class="pa-14">
                            <h1 class="ps-0 pb-8">Create A Role Listing</h1>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Role
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="role_name" label="Select role" variant="outlined" required :items="this.role_name_list" @update:model-value="display_description"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Description 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-textarea type="text" v-model="description" variant="outlined" readonly required></v-textarea>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Skills Required
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
                                        Department 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="departments" label="Select department" variant="outlined" required :items="this.departments_list"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Category 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="menu" v-model="categories" label="Select category(s)" variant="outlined" required :items="this.categories_list"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Application Deadline 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field
                                        type="date"    
                                        v-model="selectedDateFormatted"
                                        label="Select a Date"
                                        variant="outlined" 
                                        required
                                    ></v-text-field>
                                    
                                    <!-- <v-date-picker
                                        v-model="selectedDate"
                                        v-if="showDatePicker"
                                        scrollable
                                        locale="en-us"
                                        show-current
                                        @input="updateDate"
                                    ></v-date-picker>          -->
                                </v-col>
                            </v-row>
                            <v-row dense class="mx-16">
                                <v-btn
                                    block
                                    class="mt-8"
                                    color="teal-lighten-1"
                                    size="large"
                                    variant="tonal"
                                    @click="create_role()"
                                >
                                    <b>Publish</b>
                                </v-btn>
                            </v-row>
                            
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
            // minDate: new Date(),      // Minimum date (e.g., today)
            // maxDate: null,            // Maximum date (optional)
            selectedDateFormatted: '', // Displayed date in the text field
            // showDatePicker: false,    // Flag to show/hide the date picker
        };
    },
    async created() {
        // Fetch roles from the API
        await this.get_roles();
        await this.get_departments();
        await this.get_categories();
    },
    methods: {
        updateDate() {
            // Format the selected date and update the text field
            const options = { year: 'numeric', month: 'short', day: 'numeric' };
            this.selectedDateFormatted = this.selectedDate.toLocaleDateString('en-US', options);
            this.showDatePicker = false; // Hide the date picker after selection
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

                const response = await axios.get('http://127.0.0.1:5000/staff/departments');
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

                const response = await axios.get('http://127.0.0.1:5000/hr/get_category_names');
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
            } catch (error) {
                // Errors when calling the service; such as network error, 
                // service offline, etc
                console.log('Error creating roles:', error);
            }

        },
    }
}
</script>

