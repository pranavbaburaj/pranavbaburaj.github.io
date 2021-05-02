import App from './App.svelte';
import { GithubRepos } from './repos';

const repos = new GithubRepos("repos").fetchRepoData()
const app = new App({
	target: document.body,
	props: {
		name: 'world'
	}
});

export default app;