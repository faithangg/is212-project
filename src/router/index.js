import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import CreateRoleListing from "../views/CreateRoleListing.vue";

import LoginPage from "../views/LoginPage.vue";

const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/login",
    name: "LoginPage",
    component: LoginPage,
  },
  {
    path: "/CreateRoleListing",
    name: "CreateRoleListing",
    component: CreateRoleListing,
  },

];


const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;