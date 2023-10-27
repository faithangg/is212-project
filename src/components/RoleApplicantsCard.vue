
<template>
    <div>
        <v-row class="d-flex justify-center">
            <!-- display role listings -->
            <v-card v-for="applicant in role_applicants" :key="applicant.staff_id" class="role-card role-card w-100 w-lg-50 h-20">

                <v-row class="mt-3">
                    <v-col class="d-flex justify-start">
                        <v-card-title class="text-h5 font-weight-bold" id="role_name"
                        >
                            {{ applicant.name }}
                            
                        </v-card-title>
                    </v-col>
                    <v-col class="d-flex justify-end me-2">
                        <v-chip color="primary" id="dept">
                            {{ applicant.department }}
                        </v-chip>
                    </v-col>
                </v-row>                
                <v-row>
                    <v-col cols="12" md="8">
                        <v-card-text class="d-flex justify-start text-h6 ">
                            <span class="font-weight-bold" id="email">Email: </span>&nbsp;<span class="wrap-text">{{ applicant.email }}</span>
                        </v-card-text>
                        <v-card-text class="d-flex justify-start text-h6">
                            <span class="font-weight-bold">Application Date: </span> &nbsp; <span class="wrap-text">{{ applicant.application_date }}</span>
                        </v-card-text>
                    </v-col>
                    <v-col cols="12"  md="4" style="padding-top: 0px;" class="match_percentage_style">
                        <v-card-text>
                            <span class="font-weight-bold text-h6 mb-0">Your Match: </span>
                            <v-row class="px-0 py-4 my-1 mx-1 d-flex justify-center">
                                <v-progress-circular
                                    :rotate="180"
                                    :size="100"
                                    :width="15"
                                    :model-value="applicant.match_percentage"
                                    :color="calculateColor(applicant.match_percentage)"
                                >
                                    {{ applicant.match_percentage }}%
                                </v-progress-circular>
                            </v-row>
                        </v-card-text>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6 chip-container">
                        <span class="font-weight-bold text-h6 text-decoration-underline text-left">Skills Required</span>
                  <!-- loop thru requied skils -->
                        </v-card-text>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6 text-sm-h7 chip-container">
                            <span class="font-weight-bold">Skills Matched: </span>&nbsp;
                                <v-chip
                                class="me-2 mb-2"
                            v-for="skill in applicant.skills_have"
                            :key="skill"
                            color="blue">
                            {{ skill }}
                                </v-chip>
                        </v-card-text>
                    </v-col>
                </v-row>
                <v-row>
                    <v-col>
                        <v-card-text class="d-flex justify-start text-h6 chip-container">
                            <span class="font-weight-bold">Skills Missing: </span>&nbsp;
                            <v-chip
                                class="me-2 mb-2"
                                v-for="skill in applicant.skills_dont"
                                :key="skill"
                                color="red">
                                {{ skill }}
                            </v-chip>
                        </v-card-text>
                    </v-col>
                </v-row>
            </v-card>
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
            
            
        };
    },
    methods: {
        calculateColor(percentage) {
      // Define your color logic based on percentage here
      if (percentage <= 20) {
        return 'red-darken-1';
      } else if (percentage <= 40) {
        return 'orange-darken-1';
      } else if (percentage <= 60) {
        return 'yellow-darken-1';
      } else if (percentage <= 80) {
        return 'light-green-darken-1';
      } else {
        return 'teal-darken-1';
      }
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
.chip-container {
    display: flex;
    flex-wrap: wrap;
}
.wrap-text {
    white-space: nowrap;
}

.match_percentage_style{
    height: 0px;
}
@media (max-width: 600px) {
    .wrap-text {
        white-space: normal; /* Allows the text to wrap to the next line */
        overflow-wrap: break-word; /* Breaks long words to prevent overflow */
        word-wrap: break-word; /* Older browsers might require this property */
        word-break: break-word; /* Breaks the word at the end of the line */
    }
    .match_percentage_style{
        height: 100% !important;
    }
}
</style>