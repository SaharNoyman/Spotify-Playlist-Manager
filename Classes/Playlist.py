from Classes.Track import Track

class Playlist:
    playlists = {}

    def __init__(self, sp, sp_playlist):
        self.sp_playlist = sp_playlist
        self.name = sp_playlist['name']
        self.sp = sp
        self.tracks = {}
        self.playlists[self.name] = self
        self.duplicates = {}

    def get_playlist_sp_tracks(self):
        results = self.sp.user_playlist_tracks(playlist_id=self.sp_playlist['uri'], limit=100)
        sp_tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            sp_tracks.extend(results['items'])

        return sp_tracks

    def set_playlist_tracks(self):
        sp_tracks = self.get_playlist_sp_tracks()
        
        for sp_track in sp_tracks:
            track = self.convert_to_track(sp_track)
            track.add_playlist(self)
            for artist in track.artists:
                if not artist.find_playlist(self):
                    artist.add_playlist(self)
                if not artist.find_track(track):
                    artist.add_track(track)

            self.tracks[(track.name, track.artists[0].name)] = track


    def convert_to_track(self, sp_track):
        name = sp_track['track']['name']
        artist_name = sp_track['track']['artists'][0]['name']
        
        for playlist in self.playlists:    
            track = self.playlists[playlist].get_track((name, artist_name))
            if track:
                break

        if track:
            if (track.name, track.artists[0].name) in self.tracks:
                key = (track.name, track.artists[0].name)
                self.duplicates[key] = self.duplicates[key] + 1 if key in self.duplicates else 2
            return track

        return Track(self.sp, sp_track)

    def get_track(self, track):
        return self.tracks[track] if track in self.tracks else None

    def find_duplicates(self):
        for duplicate in self.duplicates:
            track = self.get_track(duplicate)
            print(f"{track.name} - {self.duplicates[duplicate]} times in {self.name}")

    def shuffle(self):
        pass