<template>
  <v-app>
  <v-content>
  <v-card max-width="448" class="mx-auto mt-9" >
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
                    ></v-text-field>
                    <v-text-field
                      label="Password"
                      required 
                      :type="showPassword ? 'text':'password'" prepend-icon="mdi-lock" 
                      :append-icon="showPassword ? 'mdi-eye-':'mdi-eye-off'" @click:append="showPassword =!showPassword"
                      v-model="password">
                    </v-text-field>
                    <!-- <v-btn>Login</v-btn> -->
                  </v-card-text>
                </v-row>

                <v-divider></v-divider>
                <v-card-actions>
                  <v-btn type="submit" class="mt-4" color="primary"  @click="login()">Login</v-btn>
                </v-card-actions>
            </v-container>
        </v-main>    
    <!-- </v-layout> -->
  </v-card>
  </v-content>
</v-app>
</template>




<script>
    export default {
        name: "LoginPage",
        data(){
          return{
            showPassword: false,
            staffID: '',
            password: ''
          }
        },
        methods: {
          async login(){
            var login_url = "http://127.0.0.1:5000/staff/login_details/" + String(this.staffID) + "/" + this.password;
            const data_fetch = await fetch(login_url)

            var data = await data_fetch.json();

            if (data['code'] == 500){
                alert('The password or staff id is incorrect')
            } 
            else{
                var access_right = data["access_rights"]
                console.log(access_right)
               
                if(access_right==1){ //staff
                  this.$router.replace({ name: "HomePage", params: { access_right: access_right } });
                  console.log("staff")
                }else if(access_right==2){ //HR
                  console.log("HR") 
                }
            }
          },
        }
    }
</script>

