<script lang="ts">
  import type { DiscordInvite } from './link'
  export let calloutHeader:string;
  export let discordInvite:DiscordInvite
  export let text:string

  function createDiscordLink(user:DiscordInvite):string {
    return  "https://discord.com/users/763820556491161650"
  }

  function createCalloutTextTitle(user:DiscordInvite):string {
    const discriminator = user.discriminator;
    const username = user.username;

    return `${username}#${discriminator}`
  }

</script>

<main>
    <div class="callout">
        <!-- <div class="callout-header">{calloutHeader}</div> -->
        <span class="closebtn">&nbsp;&nbsp;&times;</span>

        <div class="dummy"></div>
        <div class="callout-container">
          <button class="join-us-btn" 
          title={createCalloutTextTitle(discordInvite)}
          on:click={(event) => {
            window.open(
              createDiscordLink(discordInvite),
            )
          }}
          >
          Join me
        </button>
        </div>
    </div>
</main>

<style>

  .dummy {
    margin : 10px;
    margin-left : 5px;
  }

.join-us-btn {
    background-color: rgb(107, 136, 239);
    border: none;
    color: white;
    padding: 15px 32px;
    text-align: center;
    text-decoration: none;
    display: inline-block;
    font-size: 16px;
    border-radius: 5px;
    outline: none;
    margin : 20px ;
}

.join-us-btn:focus {
  background-color: rgb(107, 136, 239);
}
    .callout {
  position: fixed;
  bottom: 35px;
  right: 20px;
  margin-left: 20px;
  max-width: 300px;
  border-radius: 10px;
}

/* Callout header */
.callout-header {
  padding: 25px 25px;
  background: #7289da;
  font-size: 30px;
  color: rgb(250, 233, 233);
  /* font-family : sans-serif; */
  border-radius: 10px;

}

/* Callout container/body */
.callout-container {
  padding: 10px;
  background-color: #36393F;
  color: rgb(219, 209, 209);
  border-radius: 5px;
}

/* Close button */
.closebtn {
  position: absolute;
  top: 5px;
  bottom : 5px;
  right: 15px;
  color: rgb(252, 237, 237);
  font-size: 30px;
  cursor: pointer;
  transition: 0.3;
}

/* Change color on mouse-over */
.closebtn:hover {
  opacity : 0.7;
}
</style>