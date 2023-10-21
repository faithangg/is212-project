<template>
  <v-container class="background_image" fluid>
    <v-card max-width="948" class="mx-auto" flat dark>
      <v-layout>
        <v-main>
          <div data-aos="fade-up" data-aos-duration="1000">
            <v-container fluid>
              <form @submit.prevent="submit">
                <v-card elevation="2" class="px-14 pb-14 pt-8">
                  <v-row dense>
                    <v-col>
                      <h1
                        class="pb-8 mt-4 text-center text--white"
                        color="white"
                      >
                        Update Role Listing
                      </h1>
                    </v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="4">
                      <p class="text-h6 font-weight-bold pt-4">Role*</p>
                    </v-col>
                    <v-col cols="8">
                      <v-select
                        type="menu"
                        id="role"
                        v-model="role_name"
                        label="Select a role"
                        variant="outlined"
                        required
                        :items="this.role_name_list"
                        @update:model-value="display_description"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="4">
                      <p class="text-h6 font-weight-bold pt-4">Description*</p>
                    </v-col>
                    <v-col cols="8">
                      <p class="text-left scrollable-descript my-4" >
                          <p v-for="paragraph in this.description" :key="paragraph">
                            {{paragraph}}
                          </p>   
                        </p>
                    </v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="4">
                      <p class="text-h6 font-weight-bold pb-8">
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
                      <p class="text-h6 font-weight-bold pt-4">Department*</p>
                    </v-col>
                    <v-col cols="8">
                      <v-select
                        type="menu"
                        id="department"
                        v-model="departments"
                        label="Select department"
                        variant="outlined"
                        required
                        :items="this.departments_list"
                      ></v-select>
                    </v-col>
                  </v-row>
                  <v-row dense>
                    <v-col cols="4">
                      <p class="text-h6 font-weight-bold pt-4">Category*</p>
                    </v-col>
                    <v-col cols="8">
                      <v-select
                        type="menu"
                        v-model="categories"
                        label="Select category"
                        variant="outlined"
                        required
                        :items="this.categories_list"
                      ></v-select>
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
                        :rules="[rules.dateBeforeToday]"
                        id="application_deadline"
                      ></v-text-field>
                    </v-col>
                  </v-row>
                  <v-row dense class="mx-16">
                    <!-- Error Message -->
                    <v-alert v-if="errorMessage" color="error" icon="mdi-alert">
                      {{ errorMessage }}
                    </v-alert>
                  </v-row>
                  <v-row dense>
                    <p class="text-caption ml-6 mt-4">* indicates a required field</p>
                  </v-row>
                  <v-row dense>
                    <v-col cols="12" md="6">
                      <v-dialog
                        v-model="cancel_dialog"
                        persistent
                        width="auto"
                      >
                        <template v-slot:activator="{ props }">
                          <v-btn
                            block
                            class="mt-8 mr-6"
                            color="default"
                            size="large"
                            variant="tonal"
                            v-bind="props"
                          >
                            <b>Cancel</b>
                          </v-btn>
                        </template>
                        <v-card>
                          <v-toolbar flat color="amber">
                            <v-toolbar-title class="font-weight-bold">Cancel Edits to Role Listing</v-toolbar-title>
                          </v-toolbar>
                          <v-card-text>
                            <p>If you cancel, you will lose all the changes you have made.</p>
                            <br>
                            <p><b>Are you sure you wish to cancel?</b></p>
                          </v-card-text>
                          <v-card-actions>
                            <v-spacer></v-spacer>
                              <v-btn
                                color="grey-darken-1 font-weight-bold"
                                prepend-icon="mdi-close" 
                                variant="outlined"
                                to="/ManageRolesPage"
                                rounded
                                class="px-4"
                              >
                                Cancel Edits
                              </v-btn>
                              <v-btn
                                color="black font-weight-bold"
                                prepend-icon="mdi-pencil" 
                                variant="tonal"
                                @click="cancel_dialog = false"
                                rounded
                                class="px-4"
                              >
                                Continue Editing
                              </v-btn>
                          </v-card-actions>
                        </v-card>
                      </v-dialog>  
                    </v-col>
                    <v-col cols="12" md="6">
                      <v-btn
                        block
                        class="mt-8"
                        color="teal-lighten-1"
                        size="large"
                        variant="tonal"
                        :disabled="!isFieldsNotEmpty || date_before_today()"
                        @click="update_role()"
                        id="update_btn"
                      >
                        <b>Update</b>
                      </v-btn>
                    </v-col>
                  </v-row>
                  <!-- show success message -->
                  <v-dialog
                    v-model="success_model"
                    hide-overlay
                    class="w-50"
                    id="updated_success_alert"
                  >
                    <!-- Modal content goes here -->
                    <v-alert
                      id="success_alert"
                      color="success"
                      icon="$success"
                      title="Role updated successfully."
                    ></v-alert>
                  </v-dialog>
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
  name: "UpdateRoleListing",
  data() {
    return {
      role_name: "",
      role_name_list: [],
      description: "hi",
      departments: "",
      departments_list: [],
      categories: "",
      categories_list: [],
      skills: [],
      selectedDateFormatted: "", // Displayed date in the text field
      minDate: this.showDateinSGT(), // Minimum date allowed to select
      errorMessage: "", // Error message to display to the user
      success_model: false, // Control the visibility of the full-screen success modal
      cancel_dialog: false, // Control the visibility of the full-screen cancel modal
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
  mounted() {
    // Fetch role listing from the API
    this.listing_id = this.$route.query.listing_id;
    axios
      .get("http://127.0.0.1:5000/hr/role_listings/" + this.listing_id)
      .then((response) => {
        console.log("EXISTING ROLE LISTING DATA", response.data.data);
        (this.selectedDateFormatted = response.data.data.role_listing.deadline),
          (this.categories = response.data.data.role_listing.category);
        this.departments = response.data.data.role_listing.department;
        this.role_name = response.data.data.role_listing.role_name;
        this.description = response.data.data.role_listing.role_desc;
        this.skills = response.data.data.role_listing.skills_required;
      })
      .catch((error) => {
        console.error("Error fetching role listings:", error);
      });
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
    async update_role() {
      try {
        console.log("trying update_role()");
        // console.log(
        //   "to send:",
        //   this.role_name,
        //   this.departments,
        //   this.categories,
        //   this.selectedDateFormatted
        // );
        const response = await axios.put(
          `http://127.0.0.1:5000/hr/update_role_listing/` + this.listing_id,
          {
            role_name: this.role_name,
            department: this.departments,
            category: this.categories,
            deadline: this.selectedDateFormatted,
          }
        );
        // console.log("update outcome", response);
        if (response.status === 200) {
          // Role created successfully
          this.errorMessage = "";

          // Reset the form and set timeout to hide the success message
          this.success_model = true;
          // console.log("success message", this.success_model);

          setTimeout(() => {
            this.success_model = false;
            this.$router.replace({ name: "ManageRolesPage" });
          }, 2000);
        }
      } catch (error) {
        if (error.response && error.response.status === 400) {
          // duplicate roles detected
          // Display an error message to the user
          console.error("Error updating roles:", error); // Log the error response
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
</style>

