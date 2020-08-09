import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

def initialize():
    os.environ["SPOTIPY_CLIENT_ID"] = "80f21ffe584d47fba3f20aa84f2badaf"
    os.environ["SPOTIPY_CLIENT_SECRET"] = "9dd4bef0d9fd44ecb82a18e6e3bb15c9"
    os.environ["SPOTIPY_REDIRECT_URI"] = "http://localhost:80"

    scope = "user-library-read playlist-modify-private playlist-read-private"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, show_dialog=True, cache_path='C:\\users\\SaharN'))

    return sp