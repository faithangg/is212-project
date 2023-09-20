<template>
  <v-app>
  <v-content>
  <v-card max-width="448" class="mx-auto mt-9" color="grey-lighten-3">
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
                  <v-btn color="Info" @click="login()">Login</v-btn>
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
            }
          }
        }
    }
</script>

