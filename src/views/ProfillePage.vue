<template>
    <v-card max-width="448" class="mx-auto" color="grey-lighten-3">
      <v-layout>    
          <v-main>
              <div class="hello">main page</div> <!-- used for test files can change-->
              <v-container fluid>
                  <v-row dense>
                  <v-col
                      v-for="n in 4"
                      :key="n"
                      cols="12"
                  >
                      <v-card
                      :title="`Content ${n}`"
                      :subtitle="`Subtitle for Content ${n}`"
                      text="Lorem ipsum dolor sit amet consectetur, adipisicing elit.?"
                      ></v-card>
                  </v-col>
                  </v-row>
              </v-container>
          </v-main>    
      </v-layout>
    </v-card>
  </template>
  
  <script>
      export default {
          name: "HomePage",
      }
  </script>
  
  