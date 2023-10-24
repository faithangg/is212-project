<template>
  <v-container class="background_image" fluid>
    <!-- <img
          v-bind:src="require('../assets/background1.jpeg')"
          style="width: 100%; height: 300px; margin-top: 5px;" 
      /> -->
    <v-card max-width="948" class="mx-auto" flat dark>
      <v-layout>
        <v-main>
          <div data-aos="fade-up" data-aos-duration="1000">
            <v-container fluid>
              <form @submit.prevent="submit">
                <v-card elevation="2" class="pa-6 pa-sm-16 py-sm-12">
                  <v-row dense>
                    <v-col
                      cols="3"
                      class="d-none d-sm-block"
                    >
                      <v-btn
                        prepend-icon="mdi-arrow-left"
                        variant="text"
                        to="/ManageRolesPage"
                      >
                        Back
                      </v-btn>
                    </v-col>
                  </v-row>
                  <v-row dense>
                    <v-col>
                      <v-card-title class="justify-center ps-0 pb-sm-8 mt-2 text-h6 text-sm-h4 text-center font-weight-bold">
                        Create A Role Listing
                      </v-card-title>
                    </v-col>
                  </v-row>
                  <v-card-text class="mx-sm-16 px-md-12">
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Role*
                        </p>
                      </v-col>
                      <v-col cols="12">
                        <v-select
                          type="menu"
                          id="role"
                          v-model="role_name"
                          variant="outlined"
                          required
                          :items="this.role_name_list"
                          @update:model-value="display_description"
                        ></v-select>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Description*
                        </p>
                      </v-col>
                      <v-col cols="12">
                          <p class="text-left text-body-2 text-sm-body-1 scrollable-descript my-4">
                            <p v-for="paragraph in this.description" :key="paragraph">
                              {{paragraph}}
                            </p>  
                          </p>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Skills Required*
                        </p>
                      </v-col>
                      <v-col cols="12">
                        <div class="scrollable-skills">
                          <v-chip-group row class="mb-4 ">
                              <v-chip
                                v-for="(skill, index) in skills"
                                :key="index"
                                color="default"
                                label
                                :ripple="false"
                              >
                                {{ skill }}
                              </v-chip>
                          </v-chip-group>
                        </div>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Department*
                        </p>
                      </v-col>
                      <v-col cols="12">
                        <v-select
                          type="menu"
                          id="department"
                          v-model="departments"
                          variant="outlined"
                          required
                          :items="this.departments_list"
                        ></v-select>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Category*
                        </p>
                      </v-col>
                      <v-col cols="12">
                        <v-select
                          type="menu"
                          id="category"
                          v-model="categories"
                          variant="outlined"
                          required
                          :items="this.categories_list"
                        ></v-select>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <v-col cols="12">
                        <p class="text-body-1 text-sm-h6 text-left font-weight-bold pt-2 pb-1 pb-sm-0">
                          Application Deadline*
                        </p>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          type="date"
                          v-model="selectedDateFormatted"
                          variant="outlined"
                          required
                          :min="minDate"
                          :rules="[rules.dateBeforeToday]"
                          id="application_deadline"
                        ></v-text-field>
                      </v-col>
                    </v-row>
                    <v-row dense>
                      <p class="text-caption mt-2 mt-sm-4">*indicates a required field</p>
                    </v-row>
                    <v-row dense class="mx-md-16">
                      <!-- Error Message -->
                      <v-alert
                        id="error_alert"
                        v-if="errorMessage"
                        color="error"
                        icon="mdi-alert"
                        class="text-body-2 text-sm-body-1 mt-6"
                      >
                        {{ errorMessage }}
                      </v-alert>
                    </v-row>

                    <!--BUTTONS-->
                    <v-row dense>
                      <v-col cols="6">
                        <v-btn
                          block
                          class="text-button mt-4 mt-sm-8"
                          color="default"
                          size="large"
                          variant="tonal"
                          :disabled="!isFormFilledAtAll"
                          @click="reset_form()"
                        >
                          <b>Reset</b>
                        </v-btn>
                      </v-col>
                      <v-col cols="6">
                        <v-btn
                          block
                          class="text-button mt-4 mt-sm-8"
                          color="teal-lighten-1"
                          size="large"
                          variant="tonal"
                          :disabled="!isFieldsNotEmpty || date_before_today()"
                          @click="create_role()"
                          id="create_role_btn"
                        >
                          <b>Create</b>
                        </v-btn>
                      </v-col>
                    </v-row>
                    <!-- show success message -->
                    <v-dialog v-model="success_model" hide-overlay style="max-width: 700px;">
                      <!-- Modal content goes here -->
                      <v-alert
                        id="success_alert"
                        color="success"
                        icon="$success"
                        title="New role created successfully."
                        class="text-body-2 text-sm-body-1 mt-6"
                      ></v-alert>
                    </v-dialog>
                  </v-card-text>
                </v-card>
              </form>
            </v-container>
          </div>
        </v-main>
      </v-layout>
    </v-card>
  </v-container>
</template>

<script>
import axios from "axios";

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
      selectedDateFormatted: "", // Displayed date in the text field
      minDate: this.showDateinSGT(), // Minimum date allowed to select
      errorMessage: "", // Error message to display to the user
      success_model: false, // Control the visibility of the full-screen success modal
      rules: {
        // Checks if the input date is before or today's date
        // If rule returns true -> valid
        dateBeforeToday: (v) =>
          new Date(v).setHours(0, 0, 0, 0) >=
            new Date(this.minDate).setHours(0, 0, 0, 0) ||
          "Deadline cannot be today's date or before.",
      },
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
      // GOAL: Get tomorrow's date in Singapore Time Zone
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
      const currentDate = new Date();

      // Calculate tomorrow's date
      const tomorrowDate = new Date(currentDate);
      tomorrowDate.setDate(currentDate.getDate() + 1);
      // console.log("tomorrowDate", tomorrowDate);
      // console.log("tomorrowDate", dateFormatter.format(tomorrowDate));

      // Split the input string by '/'
      const parts = dateFormatter.format(tomorrowDate).split("/");

      // Rearrange the parts to the desired format (yyyy-mm-dd)
      const singaporeDateFormatted = `${parts[2]}-${parts[0].padStart(
        2,
        "0"
      )}-${parts[1].padStart(2, "0")}`;
      // console.log(singaporeDateFormatted);

      return singaporeDateFormatted;
    },
    //get roles
    async get_roles() {
      try {
        console.log("trying get_roles()");

        const response = await axios.get(
          "http://127.0.0.1:5000/hr/get_role_names"
        );
        console.log("response", response);

        // Save role names to role_name
        this.role_name_list = response.data;
        //console.log("this.role_name", this.role_name);
      } catch (error) {
        // Errors when calling the service; such as network error,
        // service offline, etc
        console.log("Error fetching roles:", error);
      }
    },
    async display_description() {
      try {
        console.log("trying display_description()");

        const response = await axios.get(
          "http://127.0.0.1:5000/hr//role/" + this.role_name + "/description"
        );
        console.log("response", response);

        // Save description to a variable
        this.description = response.data.description;
        // console.log("this.description", this.description);

        // Get skills
        this.display_skills();
      } catch (error) {
        // Errors when calling the service; such as network error,
        // service offline, etc
        console.log("Error fetching description:", error);
      }
    },
    async display_skills() {
      try {
        console.log("trying display_skills()");

        const response = await axios.get(
          "http://127.0.0.1:5000/hr/get_role_skills/" + this.role_name
        );
        console.log("response", response);

        // Save skills to a variable
        this.skills = response.data.skills_required;
        // console.log("this.skills", this.skills);
      } catch (error) {
        // Errors when calling the service; such as network error,
        // service offline, etc
        console.log("Error fetching skills:", error);
      }
    },
    async get_departments() {
      try {
        console.log("trying get_departments()");

        const response = await axios.get(
          "http://127.0.0.1:5000/hr/departments"
        );
        console.log("response", response.data);

        // Save departments to departments
        this.departments_list = response.data;
        // console.log("this.departments_list", this.departments_list);
      } catch (error) {
        // Errors when calling the service; such as network error,
        // service offline, etc
        console.log("Error fetching departments:", error);
      }
    },

    async get_categories() {
      try {
        console.log("trying get_categories()");

        const response = await axios.get("http://127.0.0.1:5000/hr/categories");
        console.log("response", response);

        this.categories_list = response.data;
        // console.log("this.categories_list", this.categories_list);
      } catch (error) {
        // Errors when calling the service; such as network error,
        // service offline, etc
        console.log("Error fetching categories:", error);
      }
    },
    async create_role() {
      try {
        console.log("trying create_role()");
        // console.log("to send:", this.role_name, this.departments, this.categories, this.selectedDateFormatted);
        console.log(this.selectedDateFormatted);
        const response = await axios.post(
          `http://127.0.0.1:5000/hr/create_role_listing`,
          {
            role_name: this.role_name,
            department: this.departments,
            category: this.categories,
            deadline: this.selectedDateFormatted,
          }
        );
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
          }, 3000);
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          // duplicate roles detected
          // Display an error message to the user
          console.error("Error creating roles:", error); // Log the error response
          this.errorMessage =
            "This role already exists. Please check your input and try again.";
          console.log("errorMessage", this.errorMessage);
        } else {
          // Errors when calling the service; such as network error, service offline, etc
          console.log("Network error or service offline:", error);
          // Display a generic error message
          this.errorMessage =
            "An error occurred while communicating with the server. Please try again later.";
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
    date_before_today() {
      // Parse the input date string into a Date object
      const inputDate = new Date(this.selectedDateFormatted);

      // Get tmr's date
      const tmrDate = new Date(this.minDate);

      // Remove the time component from both dates to compare only the dates
      inputDate.setHours(0, 0, 0, 0);
      tmrDate.setHours(0, 0, 0, 0);

      // Compare the two dates
      if (inputDate < tmrDate) {
        return true;
      } else {
        return false;
      }
    },
  },
  computed: {
    isFieldsNotEmpty() {
      // Check if all required fields are valid before enabling the create button
      return (
        !!this.role_name &&
        !!this.departments &&
        !!this.categories &&
        !!this.selectedDateFormatted
      );
    },
    isFormFilledAtAll() {
      // Check if any of the fields are not empty before enabling the reset button
      return (
        this.role_name ||
        this.departments ||
        this.categories ||
        this.selectedDateFormatted
      );
    },
  },
};
</script>

<style>
.background_image{
  background-image: url('../assets/background1.jpeg');
  background-size: cover; /* This ensures the image covers the entire background */
  background-position: center center; /* Center the image horizontally and vertically */
  background-repeat: no-repeat; /* Prevent the image from repeating */
  width: 100%;
}
.scrollable-descript {
  max-height: 400px; /* Set the desired maximum height for scrolling */
  overflow-y: auto; /* Enable vertical scrolling if content exceeds max height */
}
</style>
