import json
import requests
import os
import sys
import spotipy
import spotipy.util as util

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
    
    # def create_playlist(self, name): # maybe pass a parameter for date created
    #     data = json.dumps({
    #         "name": name,
    #         "description": "playlist based on the forecast"
    #     })
    #     user_id = self.user_id
    #     url = f"https://api.spotify.com/v1/users/{user_id}/playlists"
    #     response = self._place_post_api_request(url, data)
    #     response_json = response.json()
    #     playlist_id = response_json["id"]
    #     playlist = Playlist(name, playlist_id)
    #     return playlist

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

    
    def GetPlaylistID(username, playlist_name):
        playlist_id = ''
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:  # iterate through playlists I follow
            if playlist['name'] == playlist_name:  # filter for newly created playlist
                playlist_id = playlist['id']
        return playlist_id

def main():
    spotify_client = spotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                    os.getenv("SPOTIFY_USER_ID"))
    tracks = spotify_client.get_tracks('60637_tracks.json')
    scope = 'user-library-read'
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    token = util.prompt_for_user_token(username, scope, client_id = 'b5c82c819eb94cbf9728d7be2d648760',client_secret='4445d38c80e54fd2a2a97a94b4df5ec0',redirect_uri='http://localhost/') 
    sp = spotipy.Spotify(auth=token)
    playlist_name = "Weather Based Playlist"
    sp.user_playlist_create(username, playlist_name)
    playlist_id = spotifyClient.GetPlaylistID(username, playlist_name)
    playlist = Playlist(playlist_name, playlist_id)
    spotify_client.add_songs(playlist, tracks)

if __name__ == '__main__':
    main()