<template>
  <v-dialog
    v-model="dialog"
    v-if="this.$store.state.alertDialogToggle"
    transition="dialog-bottom-transition"
    max-width="430"
  >
    <v-card>
      <v-card-title class="justify-center">
        <v-icon size="100" color="red">mdi-heart-pulse</v-icon>
      </v-card-title>
      <v-card-text class="text-center">
        <div class="text-h5 mb-5">
          {{ this.$store.state.alertDialogInfo.result }}
        </div>
        <div class="text-body-1">
          {{ this.$store.state.alertDialogInfo.detail }}
        </div>
      </v-card-text>
      <v-card-actions class="justify-end">
        <v-btn text @click="closeDialog">Close</v-btn>
      </v-card-actions>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  data: () => ({
    dialog: true,
    // result: this.$store.state.alertDialogInfo.result,
    // result: "심박수 높음"
  }),
  methods: {
    closeDialog() {
      this.$store.commit("closeAlertDialog");
    },
  },
};
</script>
