const card = Vue.createApp({
  data(){
    return{
      value: "&darr;&darr;Work on Vue3 CDN&darr;&darr;"
    }
  },
  methods: {
    fruit: function (name){
      alert(name)
    }
  }
});

card.mount("#card");
