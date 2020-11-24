<template>
    <div id="search">
        <!--The main search bar-->
        <input placeholder="Search .." type="text" onfocus="this.value=''" onblur="this.value=''" autocomplete="off" spellcheck="false" name="search" id="search"><span class="close" v-on:click="close_search">&times;</span>
    </div>
</template>


<script>
export default {
    name : "Search", 
    methods: {
        close_search : () => {
            // to close the search bar on the click of the span button
            // hoverwer this is not gonna happen because the input automatically 
            // shrinks when it loses the focus
            document.getElementById("search").style.width = "30%";
        }
    }
}
</script>


<style scoped>
@import url("../static/css/search.css");
</style>