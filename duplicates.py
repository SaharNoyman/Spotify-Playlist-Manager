from Private import Initialize
from Classes.Playlist import Playlist
from Classes.Tracks import Tracks
import argparse

genres = ['Alternative / Pop Rock',
          'Metal',
          'Rock',
          'Pop',
          'Rap',
          'ישראלי',
          'היפ הופ ישראלי',
          'ים תיכוני',
          'רוק ישראלי']

def list_playlists(sp):

    sp_playlists = sp.current_user_playlists()
    playlists = []

    while sp_playlists:
        for playlist in sp_playlists['items']:
            p = Playlist(sp, playlist, playlist['name'] in genres)
            p.set_playlist_tracks()
            playlists.append(p)

        if sp_playlists['next']:
            sp_playlists = sp.next(sp_playlists)
        else:
            sp_playlists = None

    return playlists

def main():
    # Connect to API
    sp = Initialize.initialize()

    # Get all user's playlists
    playlists = list_playlists(sp)

    parser = argparse.ArgumentParser(description='Find duplicates in playlists')

    target_playlists = parser.add_mutually_exclusive_group()
    target_playlists.add_argument('-a', '--all', action='store_true', default=False, dest='all', help='Find duplicates all playlists')
    target_playlists.add_argument('-g', '--genres', action='store_true', default=False, dest='genres', help='Find duplicates only in genres playlists')
    target_playlists.add_argument('-p', '--playlists', action='append', default=[], dest='playlists', help='Find duplicates in specific playlists')

    try:
        results = parser.parse_args()
    except:
        pass

    genre_playlist = {}

    # Filter genres playlists
    for playlist in playlists:
        if playlist.name in genres:
            genre_playlist[playlist.name] = playlist.tracks
            playlist.find_duplicates()

    Tracks.find_duplicates()

if __name__ == "__main__":
    main()