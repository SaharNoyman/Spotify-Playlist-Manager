tracks = []

def add_track(track):
    tracks.append(track)

def find_track(sp_track):
    for t in tracks:
        if t.name == sp_track['track']['name'] and t.artist == sp_track['track']['artists'][0]['name']:
            return t

    return None

def find_duplicates(count):
    duplicates = [track for track in tracks if track.count >= count]
    for track in duplicates:
        message = f"{track.name} is in {track.count} Playlists: "
        for playlist in track.playlists:
            message += f"\n  {playlist.name}"
        message += "\n"
        print(message)

