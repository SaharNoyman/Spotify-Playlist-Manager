from Classes.Track import Track
import Classes.Tracks as Tracks

class Playlist:
    def __init__(self, sp, sp_playlist):
        self.sp_playlist = sp_playlist
        self.name = sp_playlist['name']
        self.sp = sp
        self.tracks = []

    def set_playlist_tracks(self):
        results = self.sp.user_playlist_tracks(playlist_id=self.sp_playlist['uri'], limit=100)
        sp_tracks = results['items']
        while results['next']:
            results = self.sp.next(results)
            sp_tracks.extend(results['items'])

        for sp_track in sp_tracks:
            track, duplicate = self.convert_to_track(sp_track)
            track.add_playlist(self)
            self.tracks.append(track)
            if not duplicate:
                Tracks.add_track(track)

    def convert_to_track(self, sp_track):
        track = Tracks.find_track(sp_track)
        return (track, True) if track else (Track(self.sp, sp_track), False)

    # Deprecated
    def list_track(self, track):
        t = Tracks.find_track(track)
        if t is None:
            Tracks.tracks.append(track)
        track.add_playlist(self)
        return t


    def find_duplicates(self):
        seen = {}
        duplicates = []

        for track in self.tracks:
            if (track.name, track.artist) not in seen:
                seen[(track.name, track.artist)] = 1
            else:
                if seen[(track.name, track.artist)] == 1:
                    duplicates.append(track)
                seen[(track.name, track.artist)] += 1

        for track in duplicates:
            print(f"{track.name} - {seen[(track.name, track.artist)]} times in {self.name}")

    def shuffle(self):
        pass