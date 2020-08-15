class Artist:
    artists = {}

    def __init__(self, sp, sp_artist):
        self.sp_artist = sp_artist
        self.name = sp_artist['name']
        self.tracks = []
        self.playlist_count = 0
        self.track_count = 0
        self.playlists = []
        self.sp = sp
        self.artists[self.name] = self

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        self.playlist_count += 1

    def find_playlist(self, playlist):
        return True if playlist in self.playlists else False

    def find_track(self, track):
        return True if track in self.tracks else False

    def add_track(self, track):
        self.tracks.append(track)
        self.track_count += 1
