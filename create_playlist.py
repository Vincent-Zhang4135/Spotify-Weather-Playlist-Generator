import json
import os
import sys
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials

from track import Track

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

def main():
    spotify_client = spotifyClient(os.getenv("SPOTIFY_AUTHORIZATION_TOKEN"),
                                    os.getenv("SPOTIFY_USER_ID"))
    tracks = spotify_client.get_tracks('jsons/02108_tracks.json')

    '''name of playlist being made'''
    playlist_name = "Weather Based Playlist"

    '''authentification for spotify'''
    if len(sys.argv) > 1:
        username = sys.argv[1]
    else:
        print("Usage: %s username" % (sys.argv[0],))
        sys.exit()

    scope = 'playlist-modify-public playlist-read-private playlist-read-collaborative playlist-modify-private'

    token = util.prompt_for_user_token(
        username, 
        scope, 
        client_id = '0ed034a78f744265a8b997557ebd7d36',
        client_secret='2dc8b0b2064b493fb96720557c44afd1',
        redirect_uri='http://127.0.0.1:5501/templates/index.html')
         
    auth_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(auth_manager=auth_manager)
    sp.user_playlist_create(username, playlist_name)

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

if __name__ == '__main__':
    main()