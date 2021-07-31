<template>
  <div>
    <div class="main">
      <Button
        label="Submit"
        v-on:click="value = 'onclick'"
      />
      <Calendar
        v-model="value"
        :inline="true"
      />
    </div>
    <div>
      <p v-text="value"></p>
    </div>
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import Calendar from "primevue/calendar";

export default defineComponent({
  name: "App",
  data() {
    return {
      value: "value",
    };
  },
  components: {
    HelloWorld,
    InputText,
    Button,
    Calendar,
  },
});
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 65px;
}
</style>
