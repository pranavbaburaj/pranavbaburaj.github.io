<script lang="ts">
	import { DevProfile } from './components/profile';
	import Profile from './components/Profile.svelte';
	import Typewriter from './Typewriter.svelte'

	const data = new DevProfile("pranavbaburaj").findUserProfile()
</script>

<main>
	<Profile props={data}></Profile>
	<Typewriter text="Hey, I'm  Pranav" emoji="👋🏾"></Typewriter>
</main>

<style>
	@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');

	:root {
		background-color: #24252A;
	}
</style>