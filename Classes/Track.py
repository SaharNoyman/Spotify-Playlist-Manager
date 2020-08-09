class Track:
    def __init__(self, sp, sp_track):
        self.sp_track = sp_track
        self.name = sp_track['track']['name']
        self.artist = sp_track['track']['artists'][0]['name']
        self.count = 0
        self.playlists = []
        self.sp = sp

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        self.count += 1