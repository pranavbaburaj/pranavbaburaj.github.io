<script lang="ts">
    export let url:any;
    export let showPreview:boolean;
    export let text:string;

    let displayValue = `${text}`
    let emoji = ""

    function createLinkOpen(event){
        let windowObjectReference:Window;
        let windowFeatures:string = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

        windowObjectReference = window.open(url, "Redirecting", windowFeatures);
    }  

</script>

<main>
   <div class="container">
    <p class="link" 
    on:click={(event) => createLinkOpen(event)}
    on:mouseover={(event) => {
        emoji = `🔗`
    }}
    on:mouseout={(event) => {
        emoji = ""
    }}
    >
        {displayValue}
    </p>
   </div>
</main>

<style>

    .container {
        display : inline;
    }
    .link {
        color : white;
        opacity : 0.5;
        transition: 1s;
    }
</style>