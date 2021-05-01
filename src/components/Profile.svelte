<script lang="ts">
  export let data: any;

  const profile = data.profile_image;
</script>

<main>
  {#if profile}
    <img src={profile} alt={data.summary} class="src" title={data.name}>
  {/if}
</main>

<style>
  main {
      display : grid;
      place-items: center;
  } 

  img {
      border-radius: 50%;
      height : 15vh;
      margin-top : 5vh;

  }

  img::selection {
      background : rgb(43, 42, 42);
  }
</style>
