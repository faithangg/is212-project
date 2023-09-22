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
                                        Role Name* 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field type="text" v-model="role_name" label="Enter role name" variant="outlined" required></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Description 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-textarea type="text" v-model="description" label="Enter job scope" variant="outlined" required></v-textarea>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Department 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="department" label="Select department" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Category 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="category" label="Select category(s)" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']" chips multiple></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Employment Type 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="employment_type" label="Select employment type" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Country 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="country" label="Select country" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Skills 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="skills" label="Select skill(s)" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']" chips multiple></v-select>
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
                                        :min="minDate"
                                        :max="maxDate"
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
    export default {
        name: "CreateRoleListing",
        data() {
            return {
                role_name: "",
                description: "",
                department: "",
                category: null,
                employment_type: "",
                country: "",
                skills: null,
                selectedDate: new Date(), // Initialize with the current date
                minDate: new Date(),      // Minimum date (e.g., today)
                maxDate: null,            // Maximum date (optional)
                selectedDateFormatted: '', // Displayed date in the text field
                showDatePicker: false,    // Flag to show/hide the date picker
                
            };
        },
        methods: {
            updateDate() {
                // Format the selected date and update the text field
                const options = { year: 'numeric', month: 'short', day: 'numeric' };
                this.selectedDateFormatted = this.selectedDate.toLocaleDateString('en-US', options);
                this.showDatePicker = false; // Hide the date picker after selection
            },
        },
    }
</script>

