import requests
import json

#Function that generates the current weather description by city
def find_descrip(city):
    url = "http://api.openweathermap.org/data/2.5/forecast?"
    key = "57e2e559f5026ec8939365df9e7b925c"
    use_url = url + "appid=" + key + "&q=" + city
    response = requests.get(use_url)

    #if response code was valid
    if response.status_code == 200:
        info = response.json()
        info = json.dumps(info)
        fp = open('test.json', 'w')
        fp.write(info)
        fp.close()
        # m = info['main']
        #curr_w = info['weather']
        #descrip = curr_w[0]['description']

        print("Current weather: " + str(descrip))
        return descrip
    #invalid response code, return error
    else:
        print("Error: Failed request, check input city again")
        
#Function that generates the current weather description by zip
def find_descrip_by_zip(zip):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    key = "57e2e559f5026ec8939365df9e7b925c"
    use_url = url + "appid=" + key + "&q=" + zip + ",us"
    response = requests.get(use_url)

    #if response code was valid
    if response.status_code == 200:
        info = response.json()
        
        #info = json.dumps(info)
        #fp = open('test.json', 'w')
        #fp.write(info)
        #fp.close()
        
        weather = info['weather']
        #curr_w = info['weather']
        descrip = weather[0]['description']

        # print("Current weather: " + str(descrip))
        return descrip
    #invalid response code, return error
    else:
        print("Error: Failed request, check input city again")

"""
# weather in chicago 60637
find_descrip_by_zip("60637")

# weather in dallas 75216
find_descrip_by_zip("77070")

# weather in los angelos 90002
find_descrip_by_zip("90002")
"""

