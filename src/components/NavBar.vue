<template>
  <v-layout>
    <v-app-bar
      app
      color="teal-darken-4"
      image="https://imageio.forbes.com/specials-images/imageserve/60ee028005bb1a95e8118143/0x0.jpg?format=jpg&crop=2915,1640,x0,y124,safe&width=1200"
    >
      <template v-slot:image>
        <v-img
          gradient="to top right, rgba(19,84,122,.8), rgba(128,208,199,.8)"
        ></v-img>
      </template>

      <v-btn id="nav_bar_icon">
        <v-app-bar-nav-icon
          @click="toggleDrawer"
          class="d-lg-none d-flex"
          v-if="isLoggedIn"
        >
        </v-app-bar-nav-icon>
      </v-btn>
      <v-app-bar-title style="text-align: left">
        <router-link to="/viewRolesPage">
          <img
            v-bind:src="require('../assets/sbrp3.png')"
            style="width: 140px; margin-top: 12px; margin-bottom: 10px"
        /></router-link>
      </v-app-bar-title>

      <v-spacer></v-spacer>

      <v-btn
        v-if="isLoggedIn"
        to="/viewRolesPage"
        id="role_listings"
        class="d-none d-lg-block pt-2"
        >View Role Listings</v-btn
      >

      <v-btn
        v-if="userIsHr"
        to="/manageRolesPage"
        id="managed"
        class="d-none d-lg-block pt-2"
        >Manage Role Listings</v-btn
      >

      <v-btn
        v-if="isLoggedIn"
        to="/profilepage"
        id="profilepage"
        class="d-none d-lg-block pt-2"
        >Profile</v-btn
      >

      <!-- <v-btn v-if="!isLoggedIn" to="/login" id="login">Login</v-btn> -->
    </v-app-bar>

    <v-navigation-drawer v-model="drawer" fixed temporary >
      <v-list nav dense>
        <v-list-item-group
          v-model="group"
          active-class="deep-purple--text text--accent-4"
        >
        <!-- <v-btn id="role_listings_nav" to="/viewRolesPage"> -->
          <v-list-item>
            <v-btn to="/viewRolesPage" id="role_listings_nav" flat>
              View Role Listings
            </v-btn>
          </v-list-item>
        <!-- </v-btn> -->
          
          <v-list-item>
            <v-btn to="/manageRolesPage" v-if="userIsHr" id="managed_nav" flat
              >Manage Role Listings</v-btn
            >
          </v-list-item>
          <v-list-item>
            <v-btn to="/profilepage" id="profilepage_nav" flat>Profile</v-btn>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>
  </v-layout>
</template>

<script>
export default {
  name: "NavBar",
  mounted() {},

  data() {
    return {
      drawer: false,
    };
  },
  computed: {
    isLoggedIn() {
      // Access the user's login status from your Vuex store getter
      return this.$store.getters.getIsLoggedIn;
    },
    userIsHr() {
      // Access the user's role from your Vuex store getter
      const userRole = this.$store.getters.getUserRole;
      console.log("Current user role from store:", userRole); // Add this line
      return userRole === "hr";
    },
    getUserId() {
      // Access the user's role from your Vuex store getter
      return this.$store.getters.getUserId;
    },
  },

  methods: {
    toggleDrawer() {
      this.drawer = !this.drawer;
    },
  },
};
</script>

<style>
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
