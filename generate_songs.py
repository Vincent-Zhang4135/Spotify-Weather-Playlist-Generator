#!/usr/bin/python
import sys, getopt
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
    
#generate_songs('60637')

def main(argv):
    #zip_start = argv[1]
    #zip_end = argv[2]
    for zip in zips:
        generate_songs(zip)
    
zips = ['36101', '99801', '85001', '72201', '94203', '80201', '06101', '19901', '32301', '30301', '96801', '83701', '62701', '46201', '50301', '50301', '40601', '70801', '04330', '21401', '02108', '48901', '55101', '39201', '65101', '59601', '68501', '89701', '03301', '08601', '87501', '12201', '27601', '58501', '43201', '73101', '97301', '17101', '02901', '57501', '37201', '73301', '84101', '05601', '23218', '98501', '25301', '53701', '82001']
if __name__ == "__main__":
    main(sys.argv)
