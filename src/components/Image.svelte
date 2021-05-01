<script lang="ts">
    interface Margins {
        top? : number,
        bottom? : number,
        rigth? : number,
        left? : number
    }

    function createStyleString(data:Array<string>){
        let css = ""
        for(let index=0; index<data.length; index++){
            css += data[index];
        }

        return css;
    }

    export let source:string;
    export let isProfile:boolean;
    export let text:string;
    export let viewportHeigth:number | null;
    export let margins:Margins;

    function createImageMargins(data:Margins):string{
        let array = [data.top, data.bottom, data.rigth, data.left]
        let keys = ["margin-top", "margin-bottom", "margin-right", "margin-left"]
        let marginString = ""
        for(let index=0; index<array.length; index++){
            const currentMargin = array[index]
            if(currentMargin){
                marginString += `${keys[index]}:${currentMargin}vh;`
            }
        }

        return marginString
    }

    let borderRadius:string = isProfile ? "border-radius:50%;" : "" 
    let height:string = viewportHeigth ? `height:${viewportHeigth}vh;` : ""
    let imageMargins:string = createImageMargins(margins) 

    const css = createStyleString([
        borderRadius, height, imageMargins
    ])

</script>


<main>
    <img src={source} alt={text} title={text} style={css}>
</main>

<style>

</style>