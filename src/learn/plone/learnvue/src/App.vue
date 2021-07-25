<template>
  <div class="main">
    <Button label="Submit" />
  </div>
</template>

<script lang="ts">
import { Options, Vue } from "vue-class-component";
import InputText from 'primevue/inputtext';
import Button from 'primevue/button';

@Options({
  components: {
    InputText,
    Button,
  },
})
export default class App extends Vue {}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
