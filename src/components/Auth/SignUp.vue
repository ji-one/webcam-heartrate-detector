<template>
  <v-card>
    <v-card-title>Sign-Up</v-card-title>
    <v-card-text>
      <v-form v-model="isValid">
        <v-text-field
          label="ID"
          v-model="credentials.username"
          :rules="[rules.required]"
          required
        >
        </v-text-field>
        <v-text-field
          label="Password"
          v-model="credentials.password"
          :rules="[rules.required]"
          :type="isPasswordHide ? 'password' : 'text'"
          :append-icon="isPasswordHide ? 'mdi-eye-off' : 'mdi-eye'"
          @click:append="isPasswordHide = !isPasswordHide"
          required
        >
        </v-text-field>
        <v-text-field
          label="Password Confirmation"
          v-model="credentials.passwordConfirmation"
          type="password"
          :rules="[rules.required, rules.passwordMatch]"
          required
        >
        </v-text-field>
      </v-form>
    </v-card-text>
    <v-card-actions class="justify-space-between">
      <v-btn @click="toSignIn" rounded text>Already have an account?</v-btn>
      <v-btn :disabled="!isValid" @click="signup" rounded text color="primary"
        >Sign up</v-btn
      >
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  name: "SignUp",
  data: function() {
    return {
      credentials: {
        username: "",
        password: "",
        passwordConfirmation: "",
      },
      isPasswordHide: true,
      isValid: false,
      rules: {
        required: (v) => !!v || "This field is required.",
        passwordMatch: (v) =>
          v === this.credentials.password || "Password do not match.",
      },
    };
  },
  methods: {
    signup() {
      this.axios
        .post("auth/signup/", this.credentials)
        .then((res) => {
          console.log(res);
          this.$emit("close");
          //   this.$router.push({ name: "Home" });
        })
        .catch((err) => {
          alert(err.response.data.error);
        });
    },
    toSignIn() {
      this.$emit("toSignIn");
    },
  },
};
</script>
