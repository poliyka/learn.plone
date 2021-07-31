import { createApp } from "vue";
import Index from "@/components/Index.vue";
import store from "@/store";

import PrimeVue from "primevue/config";

import "primevue/resources/themes/saga-blue/theme.css";
import "primevue/resources/primevue.min.css";
import "primeicons/primeicons.css";
import "@/assets/scss/main.scss";
import $ from "jquery";

const app = createApp(Index);

app.use(PrimeVue);
app.use(store);
app.mount("#app");

$(function () {
  console.log("Jquery!");
});

