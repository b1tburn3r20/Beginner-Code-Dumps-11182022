import requests, json
#enter the API key
api_key = "359ca6bdf556af82bbda780cff9a616a"
#URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"
#give city name
city_name = input("Enter city name you would like to find the weather in here: ")
#complete_url variables to store
#complete_url address
complete_url = base_url + "appid=" + api_key + "&q=" + city_name
#get method of requests module
#return response object
response = requests.get(complete_url)
#json method of response object
#convert json format data into python format data
x = response.json()
#now x contains list of nested dictionaries
#check the value of "cod" key is equal to 404, means city is found otherwise,
#city is found
if x["cod"] != "404":
    #store the value of "main"
    #to the "temp" key of y
    y = x["main"]
    
    #store the value corresponding
    #to the "temperature" of key y
    current_temperature = y["temp"]
    #store the value corresponding
    #to the "pressure" key of y
    current_pressure = y["pressure"]
    #store the value corresponding
    #to the "humidity" key of y
    current_humidity = y["humidity"]
    #store the value of "weather"
    #key in variable z
    z = x["weather"]
    #store the value of "weather"
    #key in variable z
    z = x["weather"]
    
    #store the value corresponding
    #to the "description" key at
    #the 0th index z
    weather_description = z[0]["description"]
    #printing some more rules
    print(" Temperature (in kelvin unit) = " + 
                    str(current_temperature) +
            "\n atmospheric pressure(in hPa unit) = " +
                    str(current_pressure) +
            "\n humidity (in percentage) = " +
                    str(current_humidity) +
            "\n description = " +
                    str(weather_description))

else:
    print(" City Not Found ")
    