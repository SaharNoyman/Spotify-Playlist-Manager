class Tracks:
    tracks = []

    def __init__(self):
        pass

    @classmethod
    def add_track(cls, track):
        cls.tracks.append(track)

    @classmethod
    def find_track(cls, sp_track):
        for t in cls.tracks:
            if t.name == sp_track['track']['name'] and t.artist == sp_track['track']['artists'][0]['name']:
                return t

        return None

    @classmethod
    def find_duplicates(cls):
        duplicates = [track for track in cls.tracks if track.count > 1]
        for track in duplicates:
            message = f"The track {track.name} is in "
            for playlist in track.playlists:
                message += f"{playlist.name}, "
            message = message[:-2]
            print(message)

