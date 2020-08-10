from Private import Initialize
from Classes.Playlist import Playlist
import Classes.Tracks as Tracks
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

def list_playlists(sp, target_playlists):

    sp_playlists = sp.current_user_playlists()
    playlists = []

    while sp_playlists:
        for playlist in sp_playlists['items']:
            if target_playlists is None or playlist['name'] in target_playlists:
                p = Playlist(sp, playlist)
                p.set_playlist_tracks()
                playlists.append(p)

        if sp_playlists['next']:
            sp_playlists = sp.next(sp_playlists)
        else:
            sp_playlists = None

    return playlists

def argument_parser():
    parser = argparse.ArgumentParser(description='Find duplicates in playlists')

    target_playlists = parser.add_mutually_exclusive_group()
    target_playlists.add_argument('-a', '--all', action='store_true', default=False, dest='all', help='Find duplicates all playlists')
    target_playlists.add_argument('-g', '--genres', action='store_true', default=True, dest='genres', help='Find duplicates only in genres playlists')
    target_playlists.add_argument('-p', '--playlists', action='append', default=[], dest='playlists', help='Find duplicates in specific playlists')
    parser.add_argument('-n', '--num', action='store', default=2, dest='count', type=int, help='Number of duplicates to find')

    return parser.parse_args()

def main():
    results = argument_parser()
    
    # Connect to API
    sp = Initialize.initialize()

    # Get all user's playlists
    if results.playlists:
        playlists = list_playlists(sp, results.playlists)
    elif results.all:
        playlists = list_playlists(sp, None)
    else:
        playlists = list_playlists(sp, genres)

    genre_playlist = {}

    # Filter genres playlists
    for playlist in playlists:
        if playlist.name in genres:
            genre_playlist[playlist.name] = playlist.tracks
            playlist.find_duplicates()

    Tracks.find_duplicates(results.count)

if __name__ == "__main__":
    main()