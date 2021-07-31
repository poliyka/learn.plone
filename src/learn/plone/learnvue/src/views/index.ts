import { createApp } from "vue";
import App from "@/App.vue";
import store from "@/store";

import PrimeVue from "primevue/config";

import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import "@/assets/scss/main.scss";
import $ from "jquery";

const app = createApp(App);

app.use(PrimeVue);
app.use(store);
app.mount("#app");

$(function () {
  console.log("Jquery!");
});

