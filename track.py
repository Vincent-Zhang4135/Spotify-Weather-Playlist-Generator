class Track:
    def __init__(self, name, id, artist):
        # name (str): trackname
        # id (str): song id from spotify
        # artist (str): artist of the track
        self.name = name
        self.id = id
        self.artist = artist
    
    def create_spotify_uri(self):
        return "spotify:track:{self:id}"

    def __str__(self):
        return "{self.name}"