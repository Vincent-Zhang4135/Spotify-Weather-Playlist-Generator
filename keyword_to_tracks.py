import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import requests
import json
# from spotipy.oauth2 import SpotifyOAuth

# export SPOTIPY_CLIENT_ID='eaa884bf4e774482af2e0aaffeaec2fa'
# export SPOTIPY_CLIENT_SECRET='22cb937a4eba49d283cd9dec5241a13d'
# export SPOTIPY_REDIRECT_URI='http://127.0.0.1:5500/index.html'

SPOTIPY_CLIENT_ID = 'eaa884bf4e774482af2e0aaffeaec2fa'
SPOTIPY_CLIENT_SECRET = '22cb937a4eba49d283cd9dec5241a13d'
# scope = "user-library-read"

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

def create_track(artist_name, track_name):
    track = {}
    #track['track_id'] = track_id
    track['artist_name'] = artist_name
    track['track_name'] = track_name
    return track

def create_tracks_with_keywords(keyword, lim):
    tracks_dict = {}
    for i in range(0, lim, 50):
        tracks = sp.search(q=keyword, type='track', market='US', offset=i, limit=50)
        for i, t in enumerate(tracks['tracks']['items']):
            track = create_track(t['artists'][0]['name'], t['name'])
            tracks_dict[t['id']] = track
    return tracks_dict

def read_into_json(tracks, keyword):
    tracks_json = json.dumps(tracks)
    fp = open(f'{keyword}_tracks.json', 'w')
    fp.write(tracks_json)
    fp.close()

if __name__ == '__main__':
    snowy_tracks = create_tracks_with_keywords('snowy', 500)
    sunny_tracks = create_tracks_with_keywords('sunny', 500)
    
    read_into_json(snowy_tracks, 'snowy')
    read_into_json(snowy_tracks, 'sunny')
    
    