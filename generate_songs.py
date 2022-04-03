from weather import find_descrip_by_zip
from weather_description_similar_words import weather_description_to_words 
from keyword_to_tracks import create_tracks_with_keywords, read_into_json

def generate_songs(zip):
    # first, we generate the description based off the zip
    descrip = find_descrip_by_zip(zip)
    
    # next, we want to find semantically similar keywords based off the description
    keywords = weather_description_to_words(descrip)
    print(keywords)
    
    # then, we want to use these keywords and generate songs using the search api from spotify
    tracks = create_tracks_with_keywords(keywords, 10)
    read_into_json(tracks, zip)
    
generate_songs('60637')
generate_songs('85043')