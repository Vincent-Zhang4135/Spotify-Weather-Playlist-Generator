from flask import Flask, render_template, request, jsonify
from weather import find_descrip_by_zip
from weather_description_similar_words import weather_description_to_words 
from keyword_to_tracks import create_tracks_with_keywords, read_into_json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


@app.route('/songs', methods['POST', 'GET'])
def songs(zip):
    # first, we generate the description based off the zip
    descrip = find_descrip_by_zip(zip)
    
    # next, we want to find semantically similar keywords based off the description
    keywords = weather_description_to_words(descrip)
    print(keywords)
    
    # then, we want to use these keywords and generate songs using the search api from spotify
    tracks = create_tracks_with_keywords(keywords, 10)
    
    res = jsonify(tracks)
    return res

if __name__ == "__main__":
    app.run(debug=True)