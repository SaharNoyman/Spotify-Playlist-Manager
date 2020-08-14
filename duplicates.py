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
        for sp_playlist in sp_playlists['items']:
            if target_playlists is None or sp_playlist['name'] in target_playlists:
                playlist = Playlist(sp, sp_playlist)
                playlist.set_playlist_tracks()
                playlists.append(playlist)

        if sp_playlists['next']:
            sp_playlists = sp.next(sp_playlists)
        else:
            sp_playlists = None

    return playlists

def argument_parser():
    parser = argparse.ArgumentParser(description='Find duplicates in playlists')

    target_playlists = parser.add_mutually_exclusive_group()
    action = parser.add_mutually_exclusive_group()

    target_playlists.add_argument('-a', '--all', action='store_true', default=False, dest='all', help='List all playlists')         #done
    target_playlists.add_argument('-g', '--genres', action='store_true', default=True, dest='genres', help='List genres playlists') #done
    target_playlists.add_argument('-p', action='append', default=[], dest='playlists', help='List specific playlists')              #done
    action.add_argument('-ta', '--top-artists', action='store_true', default=False, dest='top_artists', help='List the top artists by appearance')
    action.add_argument('-da', '--duplicate-artists', action='store_true', default=False, dest='duplicate_artists', help='Find artists in more than 1 playlist')
    action.add_argument('-pc', '--playlists', action='store_true', default=False, dest='playlists_count', help='Print the songs count of playlists')
    action.add_argument('-fs', '--find-single-duplicates', action='store_true', default=True, dest='single_duplicates', help='Find duplicates in the same playlist')
    action.add_argument('-fm', '--find-multi-duplicates', action='store_true', default=False, dest='single_duplicates', help='Find duplicates across multiple playlists')
    parser.add_argument('-n', '--num', action='store', default=2, dest='count', type=int, help='Number of duplicates to find')      #done
    parser.add_argument('-s', '--song', action='append', default=[], dest='songs', help='Songs to search')                          #done

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

    # Action
    

    # Filter genres playlists
    for playlist in playlists:
        playlist.find_duplicates()

    Tracks.find_duplicates(results.count, results.songs)


if __name__ == "__main__":
    main()