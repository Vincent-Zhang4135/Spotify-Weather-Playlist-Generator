import json
import requests
import os

from track import Track
from playlist import Playlist

class spotifyClient:
    def __init__(self, authorization_token, user_id):
        self.authorization_token = authorization_token
        self.user_id = user_id

    def get_tracks(self, tracks):
        # tracks (json file) = the songs being put into the playlists
        f = open(tracks)
        data = json.load(f)
        songs = [Track(track["track_name"], track["id"], track["artist_name"]) for track in data.values()]
        return songs
    
    def create_playlist(self, name): # maybe pass a parameter for date created
        data = json.dumps({
            "name": name,
            "description": "playlist based on the forecast"
        })
        user_id = self.user_id
        url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
        response = self._place_post_api_request(url, data)
        response_json = response.json()

        playlist_id = response_json["id"]
        playlist = Playlist(name, playlist_id)
        return playlist

    def add_songs(self, playlist, tracks):
        # playlist (string): the name of the playlist to add songs into
        # tracks (string): all the songs to add into the playlist
        tracks_uri = [track.create_spotify_uri() for track in tracks]
        data = json.dumps(tracks_uri)
        url = f"https://api.spotify.com/v1/users/{playlist.id}/tracks"
        response = self._place_post_api_request(url, data)
        response_json = response.json()
        return response_json

    def _place_post_api_request(self, url, data):
        response = requests.post(
            url,
            data = data,
            headers = {
                "Content-Type": "application/json",
                "Authorization": "Bearer {self.authorization_token}"
            }
        )
        return response

def main():
    spotify_client = spotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                    os.getenv("SPOTIFY_USER_ID"))
    tracks = spotify_client.get_tracks('60637_tracks.json')
    
    playlist_name = "Weather Based Playlist"
    playlist = spotify_client.create_playlist(playlist_name)
    
    spotify_client.add_songs(playlist, tracks)

if __name__ == '__main__':
    main()