<template>
  <v-app>
    <v-app-bar app color="primary">
      <router-link to="/">
        <v-btn icon>
          <v-icon>mdi-heart</v-icon>
        </v-btn>
      </router-link>
      <v-spacer></v-spacer>
      <v-dialog
        v-if="!this.$store.state.login"
        v-model="signInDialog"
        max-width="500"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" text color="white">
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
      <v-dialog
        v-if="!this.$store.state.login"
        v-model="signUpDialog"
        max-width="500"
      >
        <template v-slot:activator="{ on, attrs }">
          <v-btn v-bind="attrs" v-on="on" text color="white">
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

      <v-btn v-if="this.$store.state.login" text color="white" to="/analysis"
        >analysis</v-btn
      >
      <v-btn v-if="this.$store.state.login" @click="signout" text color="white"
        >sign out</v-btn
      >
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
  data: () => ({
    signInDialog: false,
    signUpDialog: false,
  }),
  methods: {
    signout() {
      this.axios
        .delete("auth/signout/")
        .then(() => {
          this.$store.commit("del_token");
          this.$store.state.avgBPM = [];
          if (this.$route.path !== "/") this.$router.push({ name: "Home" });
        })
        .catch((e) => console.log(e));
    },
  },
};
</script>
