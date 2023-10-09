import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import CreateRoleListing from "../views/CreateRoleListing.vue";
import ViewRolesPage from "../views/ViewRolesPage.vue";
import ManageRolesPage from "../views/ManageRolesPage.vue";
import RoleApplicantsPage from "../views/RoleApplicantsPage.vue";
import UpdateRoleListing from "../views/UpdateRoleListing.vue";
import LoginPage from "../views/LoginPage.vue";

const routes = [
  {
    path: "/",
    name: "LoginPage",
    component: LoginPage,
  },
  // {
  //   path: "/login",
  //   name: "LoginPage",
  //   component: LoginPage,
  // },
  {
    path: "/CreateRoleListing",
    name: "CreateRoleListing",
    component: CreateRoleListing,
  },

  {
    path: "/viewRolesPage",
    name: "ViewRolesPage",
    component: ViewRolesPage, 
  },

  {
    path: "/manageRolesPage",
    name: "ManageRolesPage",
    component: ManageRolesPage, 
  },

  {
    path: "/RoleApplicantsPage",
    name: "RoleApplicantsPage",
    component: RoleApplicantsPage, 
  },

  {
    path: "/UpdateRoleListing",
    name: "UpdateRoleListing",
    component: UpdateRoleListing, 
  },

];


const router = createRouter({
  history: createWebHistory(),
  routes
});


export default router;