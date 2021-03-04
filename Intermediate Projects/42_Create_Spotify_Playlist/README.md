## 
<h2 style="font-family: Times New Roman, sans-serif; font-size: 40">Automated Spotify Playlist Creation</h2>

***

> This application asks you to enter a time era for which you want to listen songs to, all you need to enter the year, month and date and it will create a Spotify Playlist with top 100 songs and it will give you a link to access the playlist, in case you lose the link/URL, it will generate a file that contains the playlist name and the URL to access it.

### Enjoy your Music

#### Please follow these steps to get your application working

#### Requirements
> Install requests, bs4, lxml, spotipy modules

```
>> pip install requests bs4 lxml spotipy
```

#### Configure Spotify (Only need to do it ONCE)

> 1. In order to create a playlist in Spotify you must have an account with Spotify. If you don't already have an account, you can sign up for a free one here: [Spotify SignUp](https://www.spotify.com/in-en/signup/)

> 2. Once you've signed up/signed in, go to the developer dashboard and create a new Spotify App: [Spotify Dashboard](https://developer.spotify.com/dashboard/), Click on Log in and it will automatically log you in <br><br>
> > 2.1 After that click on *CREATE AN APP* and give it a name(your Choice) and *CREATE*

> 3. Once you've created a Spotify app, copy the **Client ID and Client Secret** into the musical_playlist.py. **(Line 7, 8)**

> 4. Click on *EDIT SETTINGS* and in *Redirect URLs* section write "**http://example.com**"

> 5. Now Run the application as 
```
	python musical_playlist.py
```

> 6. It will give you a pop-up to agree to give access from outside source to create playlists, click on *AGREE*

> 7. It will take you to page ***example.com***, you need to copy the whole URL from address bar and paste it in the Console

> 8. Now it will give you an URL to access that playlist and it is also stored in the *playlist_link.txt* file

#### And that's it, from now on, it you will not need to do all these steps, all you have to do is run the file as
#### python musical_playlist.py