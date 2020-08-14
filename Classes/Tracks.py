tracks = []

def add_track(track):
    tracks.append(track)

def find_track(sp_track):
    for t in tracks:
        if sp_track['track']['name'] == t.name and sp_track['track']['artists'][0]['name'] in t.artists[0].name:
            return t

    return None

def find_duplicates(count, tracks_to_search):
    duplicates = [track for track in tracks if track.count >= count]
    for track in duplicates:
        if not tracks_to_search or track.name in tracks_to_search:
            message = f"{track.name} is in {track.count} Playlists: "
            for playlist in track.playlists:
                message += f"\n  {playlist.name}"
            message += "\n"
            print(message)

