artists = []

def add_artist(artist):
    artists.append(artist)

def find_artist(artist):
    for a in artists:
        if artist['name'] == a.name:
            return a

    return None

# def find_duplicates(count, tracks_to_search):
#     duplicates = [track for track in tracks if track.count >= count]
#     for track in duplicates:
#         if not tracks_to_search or track.name in tracks_to_search:
#             message = f"{track.name} is in {track.count} Playlists: "
#             for playlist in track.playlists:
#                 message += f"\n  {playlist.name}"
#             message += "\n"
#             print(message)
