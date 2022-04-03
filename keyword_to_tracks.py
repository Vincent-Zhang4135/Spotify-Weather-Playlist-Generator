import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from weather_description_similar_words import weather_description_to_words 
import json
# from spotipy.oauth2 import SpotifyOAuth

# export SPOTIPY_CLIENT_ID='eaa884bf4e774482af2e0aaffeaec2fa'
# export SPOTIPY_CLIENT_SECRET='22cb937a4eba49d283cd9dec5241a13d'
# export SPOTIPY_REDIRECT_URI='http://127.0.0.1:5500/index.html'

'''SPOTIFY CLIENT and CLIENT SECRET!'''
SPOTIPY_CLIENT_ID = 'eaa884bf4e774482af2e0aaffeaec2fa'
SPOTIPY_CLIENT_SECRET = '22cb937a4eba49d283cd9dec5241a13d'
# scope = "user-library-read"

client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

# creates a track dict object given the id, artist name, and track name
def create_track(track_id, artist_name, track_name):
    track = {}
    track['id'] = track_id
    track['artist_name'] = artist_name
    track['track_name'] = track_name
    return track

# randomize a dictionary list of the tracks
def randomize_tracks(track_dict):
    l = list(track_dict.items())
    random.shuffle(l)
    track_dict = dict(l[:50])
    return track_dict
    
# create tracks using the search api of spotify based off of the keywords 
# we feed into it.
def create_tracks_with_keywords(keywords, lim):
    tracks_dict = {}
    for keyword in keywords:
        for i in range(0, lim, 50):
            tracks = sp.search(q=keyword, type='track', market='US', offset=i, limit=10)
            for i, t in enumerate(tracks['tracks']['items']):
                track = create_track(t['id'] ,t['artists'][0]['name'], t['name'])
                tracks_dict[t['id']] = track
    return randomize_tracks(tracks_dict)

# write our tracks into a json file
def read_into_json(tracks, weather_description):
    tracks_json = json.dumps(tracks)
    fp = open(f'jsons/{weather_description}_tracks.json', 'w')
    fp.write(tracks_json)
    fp.close()


if __name__ == '__main__':
    clear_sky = weather_description_to_words("sky")
    dark_clouds = weather_description_to_words("dark clouds")
    snowy_tracks = create_tracks_with_keywords(clear_sky, 10)
    dark_tracks = create_tracks_with_keywords(dark_clouds, 10)
    
    read_into_json(snowy_tracks, 'clear_sky')
    read_into_json(dark_tracks, 'dark_clouds')
