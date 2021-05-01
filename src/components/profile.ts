import * as axios from 'axios'

export interface SocialLink {
    url : string,
    media : string,
    show? : boolean
}


export interface DevUser {
    type : string,
    id : number,
    username : string,
    name : string,
    bio : string;
    links : Map<string, SocialLink>,
    image : string
}

export class DevProfile {
    private static api = (username:string):string => {
        return `https://dev.to/api/users/by_username?url=${username}`
    }
    private username:string;

    constructor(username:string){
        this.username = username;
    }

    public findUserProfile = async ():Promise<axios.AxiosResponse<any>> => {
        const url = DevProfile.api(this.username)
        const response:axios.AxiosResponse<any> = await axios.default.get(url)
        
        return response
    }

}