<script lang="ts">
  import type {SocialLink} from './link';

  function redirect(links: Map<string, SocialLink>, key: string) {
    const link: SocialLink | undefined = links.get(key);
    if (link) {
      if (link.currentTab) {
        window.location.href = link.redirectUrl;
      } else {
        let windowObjectReference: Window;
        let windowFeatures: string =
          'menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes';

        windowObjectReference = window.open(
          link.redirectUrl,
          'Redirecting',
          windowFeatures
        );
      }
    }
  }

  function showLinkIcon(links: Map<string, SocialLink>, key: string): boolean {
    const link: SocialLink | undefined = links.get(key);
    if (!link) {
      return false;
    }

    return link.show;
  }

  export let links: Map<string, SocialLink>;
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
</svelte:head>

<main>
  {#each Array.from(links.keys()) as key}
    {#if showLinkIcon(links, key)}
      <i
        class="fa fa-{key}"
        on:click={(event) => {
          redirect(links, key);
        }}
      />
    {/if}
  {/each}
</main>

<style>
  main {
    display: flex;
    justify-content: center;
  }
  .fa,
  .iconify {
    padding: 10px;
    font-size: 30px;
    /* width: 50px; */
    text-align: center;
    text-decoration: none;
  }

  /* Add a hover effect if you want */
  .fa:hover,
  .iconify:hover {
    opacity: 0.7;
  }

  .iconify {
    color: #7289da;
  }

  .fa-twitter {
    color: #1ea1f2;
  }

  .fa-instagram {
    color: #c55582;
  }

  .fa-github {
    color: rgb(218, 218, 218);
  }

  .fa-reddit {
    color: #e66638;
  }
</style>
