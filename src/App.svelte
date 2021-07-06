<script lang="ts">
  import type {AxiosResponse} from 'axios';
  import Link from './components/Link.svelte';

  import {DevProfile} from './components/profile';
  import Profile from './components/Profile.svelte';
  import Typewriter from './Typewriter.svelte';
  import type {DiscordInvite, SocialLink} from './components/link';
  import SocialLinks from './components/SocialLinks.svelte';
  import GithubCards from './components/github/GithubCards.svelte';
  import Callout from './components/Callout.svelte';

  const discord: DiscordInvite = {
    username: 'pranavbaburaj',
    discriminator: 3361,
    userId: 763820556491161650,
  };

  interface DevUser {
    type: string;
    id: number;
    username: string;
    name: string;
    bio: string;
    links: Map<string, SocialLink>;
    image: string;
  }

  export async function fetchData(username: string): Promise<any> {
    const data = await fetch(DevProfile.api(username), {
      method: 'GET',
    });

    return await data.json();
  }

  fetchData('pranavbaburaj')
    .then((value: any) => {
      window.localStorage.setItem('user', JSON.stringify(value));
    })
    .catch((exception) => {
      window.location.href = '/';
    });

  let userData: string = window.localStorage.getItem('user');
  const socialLinkList: Map<string, SocialLink> = new Map<string, SocialLink>([
    [
      'github',
      {
        siteName: 'github',
        redirectUrl: 'https://github.com/pranavbaburaj',
        show: true,
      },
    ],
    [
      'twitter',
      {
        siteName: 'twitter',
        redirectUrl: 'https://twitter.com/_pranavbaburaj',
        show: true,
      },
    ],
    [
      'instagram',
      {
        siteName: 'instagram',
        redirectUrl: 'https://instagram.com/pranavbaburaj',
        show: true,
      },
    ],
    [
      'reddit',
      {
        siteName: 'reddit',
        redirectUrl: 'https://www.reddit.com/user/pranavbaburaj',
        show: true,
      },
    ],
    [
      'discord',
      {
        siteName: 'discord',
        redirectUrl: 'https://discord.com/users/763820556491161650',
        show: false,
      },
    ],
  ]);


  function listenKeyboardEvent(event) {
    if(event.key == "F5"){
      event.preventDefault()
    }
  }

  import Meta from './Meta.svelte'

    const metadata = {
        title: 'Svelte is Awesome',
        description: 'It really is!',
        image: 'https://svelte.dev/images/twitter-card.png',
        imageAlt: 'Svelte svelte.dev',
        url:'svelte.dev'
    }
</script>

<svelte:window on:keydown={(event)=>{listenKeyboardEvent(event)}} />

<Meta {metadata}/>
<main
  on:contextmenu={(event) => {
    event.preventDefault();
  }}
>
  <Profile data={JSON.parse(userData)} />
  <Typewriter text="Hey, I'm  Pranav" emoji="👋🏾" />
  <SocialLinks links={socialLinkList} />
  <GithubCards />
  <Callout
    calloutHeader="Hi Everyone"
    discordInvite={discord}
    text="Ping me on discord"
  />
</main>

<style>
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');
  @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:ital,wght@1,600&display=swap');

  :root {
    background-color: #24252a;
  }
</style>
