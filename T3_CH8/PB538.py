class Artist:
    def __init__(self, name):
        self.name = name
        self.albums = []  # Albums created by the artist
        self.songs = []   # Songs by the artist
    def add_album(self, album):
        self.albums.append(album)
    def add_song(self, song):
        self.songs.append(song)
    def __str__(self):
        return self.name
class Song:
    def __init__(self, title, artist, album=None):
        self.title = title
        self.artist = artist
        self.album = album
        artist.add_song(self)  # Add this song to the artist's collection
    def __str__(self):
        return f"{self.title} by {self.artist}"
class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.tracks = []  # List of Song objects
        artist.add_album(self)  # Add this album to the artist's albums
    def add_track(self, song):
        self.tracks.append(song)
        song.album = self  # Link song to this album
    def __str__(self):
        return f"Album: {self.title} by {self.artist}"
class Playlist:
    def __init__(self, name):
        self.name = name
        self.songs = []  # List of Song objects
    def add_song(self, song):
        self.songs.append(song)
    def show_songs(self):
        print(f"Playlist: {self.name}")
        for idx, song in enumerate(self.songs, 1):
            print(f"{idx}. {song}")
artist1 = Artist("Coldplay")
album1 = Album("Parachutes", artist1)
song1 = Song("Yellow", artist1)
song2 = Song("Shiver", artist1)
album1.add_track(song1)
album1.add_track(song2)
playlist1 = Playlist("My Favorites")
for track in album1.tracks:
    playlist1.add_song(track)
playlist1.show_songs()