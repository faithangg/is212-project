<template>
<v-card max-width="948" class="mx-auto" color="grey-lighten-3">
    <v-layout>    
        <v-main>
            <div data-aos="fade-up" data-aos-duration="1000">
                <v-container fluid>
                    <form @submit.prevent="submit">
                        <v-card elevation="2" class="pa-14">
                            <h1 class="ps-0 pb-8">Create New Role Listing</h1>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Job title* 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-text-field type="text" v-model="email" label="Enter job title" variant="outlined" required></v-text-field>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Description 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-textarea type="text" v-model="email" label="Enter job scope" variant="outlined" required></v-textarea>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Department 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="email" label="Select department" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Category 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="email" label="Select category(s)" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']" chips multiple></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Job Level 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="email" label="Select job level" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Country 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="email" label="Select country" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"></v-select>
                                </v-col>
                            </v-row>
                            <v-row dense>
                                <v-col cols="4">
                                    <p class="text-h6 font-weight-bold pt-4">
                                        Skills 
                                    </p>
                                </v-col>
                                <v-col cols="8">
                                    <v-select type="text" v-model="email" label="Select skill(s)" variant="outlined" required :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']" chips multiple></v-select>
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
    }
</script>

