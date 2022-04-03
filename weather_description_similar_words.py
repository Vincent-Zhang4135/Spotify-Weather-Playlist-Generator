from urllib.request import urlopen
import json

# parses our json words into just the word part of the json word
def parse_json(json_words):
    words = []
    for word in json_words:
        words.append(word['word'].split(' ')[0])
    return words

# this function takes a weather description, and uses datamuse api
# to generate 5 semantically similar words per word in the description,
# and returns a list of all these words
def weather_description_to_words(weather_description):
    weather_phrase = []
    if weather_description:
        weather_phrase.append(weather_description.replace(' ', '+'))
    else:
        return []
    weather_words = weather_description.split(' ')
    words = [] + weather_words
    for word in weather_phrase:
        url = f'https://api.datamuse.com/words?ml={word}'
        response = urlopen(url)
        json_words = json.loads(response.read())
        words += parse_json(json_words)[:5]
    return words

if __name__ == '__main__':
    # print(weather_description_to_words("clear sky"))
    print(weather_description_to_words("wonder"))