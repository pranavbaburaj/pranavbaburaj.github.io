<script lang="ts">
  export let url: any;
  export let showPreview: boolean;
  export let text: string;
  export let image: string | undefined;

  let displayValue = `${text}`;
  let emoji = '';

  function createLinkOpen(event) {
    let windowObjectReference: Window;
    let windowFeatures: string =
      'menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes';

    windowObjectReference = window.open(url, 'Redirecting', windowFeatures);
  }
</script>

<svelte:head>
  <link
    rel="stylesheet"
    href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
  />
</svelte:head>

<main>
  <div class="container">
    <p
      class="link"
      on:click={(event) => createLinkOpen(event)}
      on:mouseover={(event) => {
        emoji = `🔗`;
      }}
      on:mouseout={(event) => {
        emoji = '';
      }}
    >
      {displayValue}
    </p>
  </div>
</main>

<style>
  .container {
    display: inline;
  }
  .link {
    color: white;
    opacity: 0.7;
    transition: 1s;
    font-family: JetBrains Mono;
  }

  .link:hover {
    opacity: 0.4;
  }
</style>
