from Classes.Artist import Artist

class Track:
    def __init__(self, sp, sp_track):
        self.sp_track = sp_track
        self.name = sp_track['track']['name']
        self.artists = []
        self.sp = sp
        self.set_artists(sp_track['track']['artists'])
        self.count = 0
        self.playlists = []
        

    def add_playlist(self, playlist):
        self.playlists.append(playlist)
        self.count += 1

    def set_artists(self, sp_artists):
        for sp_artist in sp_artists:
            artist = self.convert_to_artist(sp_artist)
            self.artists.append(artist)

    def convert_to_artist(self, sp_artist):
        if sp_artist['name'] in Artist.artists:
            return Artist.artists[sp_artist['name']]
        
        artist = Artist(self.sp, sp_artist)
        Artist.artists[artist.name] = artist
        return artist