<script lang="ts">
    export let text:string | number | undefined;
    
    let value:string = "";
    let counterIndex = 0;

    function createTypewriterEffect() {    
        let speed = 50;
        if(counterIndex < String(text).length){
            value += String(text).charAt(counterIndex)
            counterIndex += 1
            setTimeout(() => {
                console.log(value)
                createTypewriterEffect()
            }, 100)
        }
    }

    createTypewriterEffect()
</script>

<main>
    <div class="text">
        <div class="type">
            {#if text}
                <p class="data">
                    {value}
                </p>
            {/if}
        </div>
    </div>
</main>

<style>

</style>