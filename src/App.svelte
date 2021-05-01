<script lang="ts">
	import type { AxiosResponse } from 'axios';

	import { DevProfile } from './components/profile';
	import Profile from './components/Profile.svelte';
	import Typewriter from './Typewriter.svelte'

	interface SocialLink {
		url : string,
		media : string,
		show? : boolean
	}

	
	interface DevUser {
		type : string,
		id : number,
		username : string,
		name : string,
		bio : string;
		links : Map<string, SocialLink>,
		image : string
	}

	async function fetchData(username:string):Promise<any> {
		const data = await fetch(DevProfile.api(username), {
			method : "GET"
		})

		return await data.json()
	}

	let userData:string = window.localStorage.getItem('user')
	if(!userData){
		fetchData("pranavbaburaj").then((value:any) => {
			window.localStorage.setItem('user', JSON.stringify(value))
		}).catch((exception) => {
			window.location.href = "/"
		})

		userData = window.localStorage.getItem('users')
	} 

</script>

<main>
	<Profile></Profile>
	<Typewriter text="Hey, I'm  Pranav" emoji="👋🏾"></Typewriter>
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');

	:root {
		background-color: #24252A;
	}
</style>