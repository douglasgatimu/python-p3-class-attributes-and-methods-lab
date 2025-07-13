from collections import Counter
class Song:
    count = 0
    genres = []
    artists = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artist_count(artist)
        

    
    def add_song_to_count():
        Song.count += 1

    def add_to_genres(genre):
        if genre not in Song.genres:
            Song.genres.append(genre)

    def add_to_artists(artist):
        if artist not in Song.artists:
            Song.artists.append(artist)

    def add_to_genre_count(genre):

        if Song.genre_count.get(genre) and Song.genre_count.get(genre) > 0:
            Song.genre_count[genre] +=1
        else:
            Song.genre_count[genre] = 1

    def add_to_artist_count(artist):

        if Song.artist_count.get(artist) and Song.artist_count.get(artist) > 0:
            Song.artist_count[artist] +=1
        else:
            Song.artist_count[artist] = 1            

oneman = Song('Kairetu Gakwa', 'Samido', 'Mugithi')
onelady = Song('Kairetu Gakwa', 'Loise Kim', 'Kigoco')
twoman = Song('Kairetu Gakwa', 'Samido', 'Mugithi')
print(Song.count)
print(Song.artist_count)
print(twoman.artist_count)