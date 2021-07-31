<template>
  <div>
    <h2 style="color: white" v-html="value"></h2>
    <Card style="width: 20rem; margin: 5px">
      <template #header>
        <img
          alt="user header"
          src="@/assets/img/4.jpg"
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
import InputText from "primevue/inputtext";
import Button from "primevue/button";
import Card from "primevue/card";

export default defineComponent({
  name: "Index",
  data() {
    return {
      value: "&darr;&darr;Always child replace innerHTML&darr;&darr;",
    };
  },
  components: {
    InputText,
    Button,
    Card,
  },
});
</script>
