class Playlist:
    def __init__(self, name, id):
        # name (str): playlist name
        # id (str): playlist id
        self.name = name
        self.id = id
    def __str__(self):
        return f"Playlist: {self.name}"