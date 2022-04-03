from urllib.request import urlopen
import json

url = "https://api.datamuse.com/words?ml=sky"

response = urlopen(url)
data_json = json.loads(response.read())

print(data_json)

def weather_description_to_words(weather_description):
    

if __name__ == '__main__':
    print("hello")