# Spotify Playlist using Musical Time Machine
CLIENT_ID = "54df7b3d8e654090bb092049ae6b7abd"
CLIENT_SECRET = "b55b401e966548fabb8a77bd286d6d00"
from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth


date = input("Which year do you want to travel to? Type the date in this format: YYYY-MM-DD\n :")
year = date.split("-")[0]
month = date.split("-")[1]
day = date.split("-")[2]

# Step 1 : Scraping the Billboard Hot 100
URL = f"https://www.billboard.com/charts/hot-100/{year}-{month}-{day}/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(URL, headers=header)
webpage = response.text


soup = BeautifulSoup(webpage, "html.parser")

song_titles = []
for title_tag in soup.find_all(name="h3", class_="a-no-trucate"):
    song_titles.append(title_tag.get_text(strip=True))

# print(song_titles)

# Step 2 : Authentication with Spotify
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://127.0.0.1:8000/callback",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="31gyuyyuzdlaarhvbk7ehgns77sa",
)
)

user_id = sp.current_user()["id"]

# Step 3 : Search Spotify for the Songs from Step 1
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}",type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Step 4 : Creating and Adding to Spotify Playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)








