<template>
  <v-app>
    <v-app-bar app color="primary">
      <router-link to="/">
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
      </router-link>
      <v-spacer></v-spacer>
      <v-dialog v-model="signInDialog" max-width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn text color="white" v-bind="attrs" v-on="on">
            sign in
          </v-btn>
        </template>
        <sign-in
          @close="signInDialog = false"
          @toSignUp="
            signInDialog = false;
            signUpDialog = true;
          "
        />
      </v-dialog>
      <v-dialog v-model="signUpDialog" max-width="500">
        <template v-slot:activator="{ on, attrs }">
          <v-btn text color="white" v-bind="attrs" v-on="on">
            sign up
          </v-btn>
        </template>
        <sign-up
          @close="signUpDialog = false"
          @toSignIn="
            signUpDialog = false;
            signInDialog = true;
          "
        />
      </v-dialog>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>
<script>
import SignIn from "./components/Auth/SignIn.vue";
import SignUp from "./components/Auth/SignUp.vue";
export default {
  name: "App",
  components: {
    SignIn,
    SignUp,
  },
  data: () => ({ signInDialog: false, signUpDialog: false }),
};
</script>
