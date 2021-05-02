
export class GithubRepos {
    private localstorageKey:string;

    constructor(key:string) {
        this.localstorageKey = key
    }

    public fetchRepoData = ():void => {
        fetch("https://hehe.pranavbaburaj.repl.co/", {
            method : "GET"
        }).then((response:Response) => {
            return response.json()
        }).then((data:any) => {
            window.localStorage.setItem(this.localstorageKey, JSON.stringify(data))
        }).catch((exception:any) => {
            console.error(exception)
        })
    }
}