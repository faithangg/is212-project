import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import CreateRoleListing from "../views/CreateRoleListing.vue";


const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
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