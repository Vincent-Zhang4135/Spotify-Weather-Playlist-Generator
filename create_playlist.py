import os
import json
import sys

from track import Track

#spotipy Libraries
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyOAuth

SPOTIPY_CLIENT_ID="0ed034a78f744265a8b997557ebd7d36"
SPOTIPY_CLIENT_SECRET="2dc8b0b2064b493fb96720557c44afd1"
SPOTIPY_REDIRECT_URI="http://127.0.0.1:5501/templates/index.html/callback"
SCOPE = "playlist-modify-public playlist-read-collaborative"

class CreatePlaylist:
    def __init__(self, AUTHORIZATION_TOKEN, USER_ID):
        self.AUTHORIZATION = AUTHORIZATION_TOKEN
        self.USER_ID = USER_ID

    def authenticate(self, username):
        scope = 'playlist-modify-public playlist-read-collaborative'
        token = util.prompt_for_user_token(
            username=username,
            scope=scope,
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            redirect_uri=SPOTIPY_REDIRECT_URI
        )
        return token
    
    def createPlaylist(self, authToken, username, playlist_name):
        sp = spotipy.Spotify(authToken)
        if authToken:
            spotifyObject = spotipy.Spotify(authToken)
            spotifyObject.user_playlist_create(
                username, 
                playlist_name, 
                description="Weather Based Playlist")
        else:
            print("Can't get token for", username)
    
    def get_tracks(self, tracks):
        # tracks (json file) = the songs being put into the playlists
        f = open(tracks)
        data = json.load(f)
        songs = [Track(track["track_name"], track["id"], track["artist_name"]) for track in data.values()]
        return songs
    
    def addSongs(self, authToken, username, playlist_name, tracks):
        sp = spotipy.Spotify(authToken)
        ''' Get playlist ID given playlist name'''
        playlist_id = ''
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:  # iterate through playlists I follow
            if playlist['name'] == playlist_name:  # filter for newly created playlist
                playlist_id = playlist['id']

        '''Add playlist in based on id'''
        track_ids = []
        for track in tracks:
            track_ids.append(track.id)
        sp.user_playlist_add_tracks(username, playlist_id, track_ids)


def main():
    spotify_client= CreatePlaylist(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                            os.getenv("SPOTIFY_USER_ID"))

    # Variables for requesting username and zip
    if len(sys.argv) > 2:
        username = sys.argv[1]
        zip = sys.argv[2]
    else:
        print("not enough parameters")
        sys.exit()

    # To authentify spotify
    authToken = spotify_client.authenticate(username)

    #creating playlist
    playlist_name = f'Weather for {zip}'
    spotify_client.createPlaylist(authToken, username, f'{playlist_name}')

    # add the songs in the json file to the playlist
    tracks = spotify_client.get_tracks(f'jsons/{zip}_tracks.json')
    spotify_client.addSongs(authToken, username, playlist_name, tracks)


if __name__=='__main__':
    main()