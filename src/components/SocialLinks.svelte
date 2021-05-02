<script lang="ts">
    interface SocialLink {
        siteName : string;
        redirectUrl : string;
        currentTab? : boolean
        show : boolean
    }

    export let links:Map<string, SocialLink>;
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
</svelte:head>

<main>
  <a href="#" class="fa fa-github" />
</main>

<style>
  .fa {
    padding: 20px;
    font-size: 30px;
    width: 50px;
    text-align: center;
    text-decoration: none;
  }

  /* Add a hover effect if you want */
  .fa:hover {
    opacity: 0.7;
  }
</style>
