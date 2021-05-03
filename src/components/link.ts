export interface SocialLink {
  siteName: string;
  redirectUrl: string;
  currentTab?: boolean;
  show: boolean;
}

export interface DiscordInvite {
  username : string;
  discriminator : number;
  userId : number
}