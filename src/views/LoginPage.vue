<template>
  <v-card max-width="448" class="mx-auto" color="grey-lighten-3">
    <v-layout>    
        <v-main>
            <v-container fluid>
                <v-row dense>
                  <v-card-title>Login</v-card-title>
                  <v-card-text>
                    <v-text-field
                      label="Staff ID"
                      required prepend-icon="mdi-account-circle"
                    ></v-text-field>
                    <v-text-field
                      label="Password"
                      required 
                      :type="showPassword ? 'text':'password'" prepend-icon="mdi-lock" 
                      :append-icon="showPassword ? 'mdi-eye-':'mdi-eye-off'" @click:append="showPassword =!showPassword">
                    </v-text-field>
                    <v-btn>Login</v-btn>
                  </v-card-text>
                </v-row>

                <v-divider></v-divider>
                <v-card-actions>
                  <v-btn color="Info">Login</v-btn>
                </v-card-actions>
            </v-container>
        </v-main>    
    </v-layout>
  </v-card>
</template>

<script>
    export default {
        name: "LoginPage",
        data(){
          showPassword: false
        }
    }
</script>

