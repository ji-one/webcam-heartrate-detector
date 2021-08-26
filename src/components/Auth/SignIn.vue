<template>
  <v-card>
    <v-card-title> Sign-In </v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="ID"
          v-model="credentials.username"
          :rules="[rules.required]"
        >
        </v-text-field>
        <v-text-field
          label="Password"
          v-model="credentials.password"
          :rules="[rules.required]"
          :type="isPasswordHide ? 'password' : 'text'"
          :append-icon="isPasswordHide ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append="isPasswordHide = !isPasswordHide"
        ></v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-space-between">
      <v-btn @click="toSignUp" rounded text>Don’t have an account?</v-btn>
      <v-btn :disabled="!isValid" @click="signin" rounded text color="primary"
        >Sign in</v-btn
      >
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  name: "SignIn",
  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
      },
      token: "",
      decoded: "",
      isPasswordHide: true,
      isValid: false,
      rules: {
        required: (v) => !!v || "This field is required.",
      },
    };
  },
  methods: {
    signin() {
      const jwt = require("jsonwebtoken");
      this.axios
        .post("auth/signin/", this.credentials)
        .then((res) => {
          this.token = res.data.token;
          sessionStorage.token = this.token;
          this.decoded = jwt.decode(sessionStorage.token);
          this.$store.commit("get_token", this.decoded);
          // this.$router.push({ name: "Home" });
          this.$emit("close");
        })
        .catch((err) => {
          alert(err.response.data.error);
        });
    },
    toSignUp() {
      this.$emit("toSignUp");
    },
  },
};
</script>
