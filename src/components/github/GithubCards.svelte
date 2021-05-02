<script lang="ts">
  let data = window.localStorage.getItem('repos')
  if (!data){
    window.location.reload()
  }

  data = JSON.parse(data).data
  if(!Array.isArray(data)){
    window.location.reload()
  }

  let show = Array.isArray(data)

</script>

<main>

<div class="github-cards">
{#if show}
  {#each data as repo}
    <a class="github-card" data-github="Nexmo/nexmo-ruby" href="" on:click={(event) => {
      window.open(repo.html_url)
    }}>
      <h3>{repo.name}</h3>
      <p>{repo.description}</p>
      <span class="github-card__meta">
        <i class="fa fa-star" aria-hidden="true"></i>
        <span data-stars>
          {repo.stargazers_count}
        </span>
      </span>
    </a>
  {/each}
{/if}
</div>
</main>

<style lang="css">


.github-cards {
  display: flex;
  flex-flow: row;
  flex-wrap: wrap;
  width: 5vh;
  
}

.github-card {
  background : inherit;
  display: block;
  box-sizing: border-box;
  border: 1px solid rgb(65, 63, 63);
  margin: 10px;
  padding: 16px;
  color: rgb(139, 148, 158);
  text-decoration: none;
  font-size: 14px;
  flex: 1;
  min-width: 250px;
  border-radius : 10px;
}

h3 {
    margin-top: 0;
    color: #4078c0;
    font-size: 16px;
    font-weight : 600;
  }

.github-card__meta {
  margin-right: 20px;
}  
i {
    font-size: 16px;
  }
</style>