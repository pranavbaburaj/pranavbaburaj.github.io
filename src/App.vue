<template>
<meta name="viewport" content="width=device-width,initial-scale=1.0">
  <div id="app">
    <NavBar />
    <!-- <footer>
      <p>
        &copy; Pranav Baburaj . Design inspired by <strong><a href="https://iolanguage.org/">iolanguage.org</a></strong>
      </p>
    </footer> -->
  </div>
</template>

<script>
import NavBar from './components/NavBar.vue'

export default {
  name: 'App',
  components: {
    NavBar
  }
}
</script>

<style>

* {
  background: #191919;
}

footer {
  word-spacing: 2px;
  font-family: cursive;
  color : rgb(255, 255, 255);
  bottom: 0px;
  display: block;
  font-size: 13px;
  /* height: 11.2px; */
  left: 0px;
  position: absolute;
  right: 0px;
  text-align: center;
  text-size-adjust : 100%;
}


footer a {
  color: #ffffff;
  text-decoration: none;
  font-weight: 400;
}

footer a:hover {
  text-decoration: underline;;
}

</style>
