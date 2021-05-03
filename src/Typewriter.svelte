<script lang="ts">
  export let text: string | number | undefined;
  export let emoji: string | undefined;

  let value: string = '';
  let counterIndex = 0;

  /**
   * Create the typewriter effect with
   * the text and the speed passed in as
   * a props
   */
  function createTypewriterEffect() {
    let speed = 50;
    if (counterIndex < String(text).length) {
      value += String(text).charAt(counterIndex);
      counterIndex += 1;
      setTimeout(() => {
        createTypewriterEffect();
      }, 100);
    }
  }

  createTypewriterEffect();
</script>

<main>
  <div class="text">
    <div class="type">
      {#if text}
        <p class="data">
          {value}
          {#if emoji}
            {emoji}
          {/if}
        </p>
      {/if}
    </div>
  </div>
</main>

<style>
  .text {
    display: grid;
    align-items: center;
    text-align: center;
    /* margin-top : 10%; */
  }
  .data {
    color: #ebe7e7;
    font-family: 'Josefin Sans', arial, helvetica;
    display: inline-block;
    font-size: 5vw;
    font-weight: bolder;
  }

  .data::selection {
    background-color: #1d1e22;
  }
</style>
