<template>
  <div class="nav">
    <div class="header">
      <header><h1>Pranav</h1></header>
      <header><h3>I am {{ age }} and I love programming.</h3></header>
    </div>
    <!-- <Search /> -->
    <Links />
  </div>
</template>

<script>
// import Search from "./Search.vue";
import Links from "./Links.vue";


export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  components : {
    Links
  },
  data : () => {
    return {
      age : new Date().getFullYear() - 2007
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import url("../static/css/main.css");


</style>
