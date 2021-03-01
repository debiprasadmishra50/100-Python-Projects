from bs4 import BeautifulSoup
import lxml
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

SPOTIFY_CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
SPOTIFY_CLIENT_SECRET = "YOUR_SPOTIFY_CLIENT_SECRET"

# -------------------- GET SONGS ------------------- #
print("Which year do you want to travel to?")
year = input("Enter Year: ")
month = input("Enter Month(1-12): ")
date = input("Enter Date: ")
if "0" not in month and int(month) < 10:
    month = f"0{month}"
if "0" not in date and int(date) < 10:
    date = f"0{date}"

time = f"{year}-{month}-{date}"
URL = f"https://www.billboard.com/charts/hot-100/{time}"

response = requests.get(url=URL).text
soup = BeautifulSoup(response, 'lxml')
song_tag = soup.find_all(name="span", class_="chart-element__information__song")

song_list = [song.getText() for song in song_tag]

# -------------------- Spotify Playlist ------------------- #

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        show_dialog=True,
        cache_path="token.txt"
    ))
user_id = sp.current_user()['id']
# print(user_id)

song_uris = []
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")

    try:
        song_uris.append(result["tracks"]['items'][0]['uri'])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)

with open("playlist_link.txt", mode="a") as link:
    link.write(f"{playlist['name']}:\t{playlist['external_urls']['spotify']}\n")

print(f"\n\nyou can access the playlist at:\n\n\t{playlist['external_urls']['spotify']}\n\n"
      f"URL or from playlist_link.txt file")
