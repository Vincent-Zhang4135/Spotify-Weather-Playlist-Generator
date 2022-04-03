import json
import os
import sys
import spotipy
import spotipy.util as util

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
    tracks = spotify_client.get_tracks('jsons/60637_tracks.json')

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
        client_id = 'b5c82c819eb94cbf9728d7be2d648760',
        client_secret='4445d38c80e54fd2a2a97a94b4df5ec0',
        redirect_uri='http://127.0.0.1:5501/index.html') 

    sp = spotipy.Spotify(auth=token)
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