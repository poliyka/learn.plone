<template>
  <div class="main">
    <Button label="Submit" />
  </div>
</template>


<script lang="ts">
import { defineComponent } from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

export default defineComponent({
  name: "App",
  components: {
    HelloWorld,
    InputText,
    Button,
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
