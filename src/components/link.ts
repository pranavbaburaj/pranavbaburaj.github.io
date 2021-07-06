export interface SocialLink {
  // the name of the social site
  siteName: string;

  // the url to redirect
  redirectUrl: string;

  // whether to open in the current tab
  // or a new tab
  currentTab?: boolean;

  // whether to show the link or not
  show: boolean;
}

export interface DiscordInvite {
  // the username
  username: string;

  // the discriminator
  discriminator: number;

  // the user id
  userId: number;
}
