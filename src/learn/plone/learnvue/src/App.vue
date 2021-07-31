<template>
  <div style="display: inline-flex">
    <Card style="width: 20rem; margin: 5px">
      <template #header>
        <img
          alt="user header"
          src="#"
        >
      </template>
      <template #title>
        Advanced Card
      </template>
      <template #content>
        Lorem ipsum dolor sit amet, consectetur adipisicing elit. Inventore sed consequuntur error repudiandae numquam deserunt
        quisquam repellat libero asperiores earum nam nobis, culpa ratione quam perferendis esse, cupiditate neque quas!
      </template>
      <template #footer>
        <Button
          icon="pi pi-check"
          label="Save"
        />
        <Button
          icon="pi pi-times"
          label="Cancel"
          class="p-button-secondary"
          style="margin-left: .5em"
        />
      </template>
    </Card>
  </div>

</template>


<script lang="ts">
import { defineComponent } from "vue";
import HelloWorld from "./components/HelloWorld.vue";
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import Card from "primevue/card";

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
    Card,
  },
});
</script>
