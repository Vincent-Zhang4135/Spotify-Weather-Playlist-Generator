import requests
import json


#Function that generates the current weather description
def find_descrip(city):
    url = "http://api.openweathermap.org/data/2.5/forecast?"
    key = "57e2e559f5026ec8939365df9e7b925c"
    use_url = url + "appid=" + key + "&q=" + city
    response = requests.get(use_url)

    #if response code was valid
    if response.status_code == 200:
        info = response.json()
        m = info['main']
        curr_w = info['weather']
        descrip = curr_w[0]['description']

        print("Current weather: " + str(descrip))
        return descrip
    #invalid response code, return error
    else:
        print("Error: Failed request, check input city again")





