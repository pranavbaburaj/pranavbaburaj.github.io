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
  let f5ConfirmationModelDisplay = "none"

  function listenKeyboardEvent(event) {
    if(event.key == "F5"){
      event.preventDefault()
      f5ConfirmationModelDisplay = "block"
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
  <div id="id01" class="modal" style="display:{f5ConfirmationModelDisplay};">
    <span>&times;</span>
    <form class="modal-content">
      <div class="container">
        <h1>Are you sure?</h1>
        <!-- <p>Are you sure you want to delete your account?</p> -->

        <div class="clearfix">
          <button type="button" class="cancelbtn" on:click={() => {
            f5ConfirmationModelDisplay = "none"
          }}>Cancel</button>
          <button type="button" class="deletebtn" on:click={() => {window.open("https://www.youtube.com/watch?v=eBGIQ7ZuuiU")}}>Proceed</button>
        </div>
      </div>
    </form>
  </div>
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

  /* Set a style for all buttons */
button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

button:hover {
  opacity:1;
}

/* Float cancel and delete buttons and add an equal width */
.cancelbtn, .deletebtn {
  float: left;
  width: 50%;
}

/* Add a color to the cancel button */
.cancelbtn {
  background-color: #ccc;
  color: black;
}

/* Add a color to the delete button */
.deletebtn {
  background-color: #6B88EF;
}

/* Add padding and center-align text to the container */
.container {
  padding: 16px;
  text-align: center;
}

/* The Modal (background) */
.modal {
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  left: 0;
  top: 0;
  width: 100%; /* Full width */
  height: 100%; /* Full height */
  overflow: auto; /* Enable scroll if needed */
  background-color: #24252A;
  padding-top: 50px;
}

/* Modal Content/Box */
.modal-content {
  background-color: #fefefe;
  margin: 5% auto 15% auto; /* 5% from the top, 15% from the bottom and centered */
  border: 1px solid #888;
  width: 80%; /* Could be more or less, depending on screen size */
}

/* Style the horizontal ruler */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* The Modal Close Button (x) */
.close {
  position: absolute;
  right: 35px;
  top: 15px;
  font-size: 40px;
  font-weight: bold;
  color: #f1f1f1;
}

.close:hover,
.close:focus {
  color: #f44336;
  cursor: pointer;
}

/* Clear floats */
.clearfix::after {
  content: "";
  clear: both;
  display: table;
}

/* Change styles for cancel button and delete button on extra small screens */
@media screen and (max-width: 300px) {
  .cancelbtn, .deletebtn {
    width: 100%;
  }
}
</style>
