<script lang="ts">
    export let url:any;
    export let showPreview:boolean;
    export let text:string;

    let displayValue = ` ${text}`

    function createLinkOpen(event){
        let windowObjectReference:Window;
        let windowFeatures:string = "menubar=yes,location=yes,resizable=yes,scrollbars=yes,status=yes";

        windowObjectReference = window.open(window.location.origin, "Redirecting", windowFeatures);
    }  

</script>

<main>
    <p class="link" 
    on:click={(event) => createLinkOpen(event)}
    on:mouseover={(event) => {
        displayValue = `🔗${text}`
    }}
    on:mouseout={(event) => {
        displayValue = ` ${text}`
    }}
    >
        {displayValue}
    </p>
</main>

<style>
    .link {
        color : red;
    }
</style>