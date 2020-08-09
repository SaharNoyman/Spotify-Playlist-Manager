from Private import Initialize
from Classes.Playlist import Playlist
from Classes.Tracks import Tracks

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

    genre_playlist = {}

    # Filter genres playlists
    for playlist in playlists:
        if playlist.name in genres:
            genre_playlist[playlist.name] = playlist.tracks
            playlist.find_duplicates()

    Tracks.find_duplicates()
    pass

if __name__ == "__main__":
    main()



