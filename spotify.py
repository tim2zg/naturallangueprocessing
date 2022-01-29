import os
from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-read-playback-state,user-modify-playback-state"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('client_id'),
                                               client_secret=os.environ.get('client_secret'),
                                               redirect_uri=os.environ.get('redirect_uri'),
                                               scope=os.environ.get('scope')))

# Shows playing devices
res = sp.devices()
print(res)


def play_song():
    sp.start_playback(device_id=os.environ.get('device_id'), uris=['spotify:track:4iV5W9uYEdYUVa79Axb7Rh'])

play_song()