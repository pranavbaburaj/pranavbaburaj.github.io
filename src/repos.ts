export class GithubRepos {
  private localstorageKey: string;

  /**
   * @constructor
   * @param {string} key The localstorage key
   */
  constructor(key: string) {
    this.localstorageKey = key;
  }

  /**
   * @public
   * Fetch the results from the api and post
   * it in the localStorage using the key
   */
  public fetchRepoData = (): void => {
    fetch('https://pranavababuraj-top-github-proj.herokuapp.com/', {
      method: 'GET',
    })
      .then((response: Response) => {
        return response.json();
      })
      .then((data: any) => {
        window.localStorage.setItem(this.localstorageKey, JSON.stringify(data));
      })
      .catch((exception: any) => {
        console.error(exception);
      });
  };
}
