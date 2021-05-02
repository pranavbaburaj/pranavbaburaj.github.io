<script lang="ts">
  import Image from './Image.svelte';

  export let data: any;

  const profile = data.profile_image;
</script>

<main>
  {#if profile}
    <!-- <img src={profile} alt={data.summary} class="src" title={data.name}> -->
    <Image
      source={profile}
      isProfile={true}
      text={data.name}
      viewportHeigth={15}
      margins={{top: 5}}
    />
  {/if}
</main>

<style>
  main {
    display: grid;
    place-items: center;
  }

  .contain {
    border-radius: 50%;
    height: 15vh;
    margin-top: 5vh;
  }

  img::selection {
    background: rgb(43, 42, 42);
  }
</style>
