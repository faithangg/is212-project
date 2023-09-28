<template>
    <v-layout>
      <v-app-bar
        color="teal-darken-4"
        image="https://imageio.forbes.com/specials-images/imageserve/60ee028005bb1a95e8118143/0x0.jpg?format=jpg&crop=2915,1640,x0,y124,safe&width=1200"
      >
        <template v-slot:image>
          <v-img
            gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
          ></v-img>
        </template>

        <v-app-bar-title style="text-align: left;"> <img v-bind:src="require('../assets/sbrp.png')" style="width: 200px; margin-top: 20px;"/></v-app-bar-title>
        
        <v-spacer></v-spacer>

        <v-btn to="/">View Role Listings</v-btn>

        <v-btn to="/">Manage Role Listings</v-btn>
        
        <v-btn to="/login">Profile</v-btn>

      </v-app-bar>
    </v-layout>
</template>

<script>

export default {
  name: 'NavBar',
  mounted() {


  },

    data() {
      return {

      }
  },
  methods: {

    }


}
</script>

<style >
.navbar {
  position: absolute;
  top: 0;
  width: 100vw;
}

.link-style {
  text-decoration: none;
  color: white;
}
</style>
