from bs4 import BeautifulSoup
import requests
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q=%7B{city}%7D&oq=%7B{city}%7D&aqs=chrome..69i57j35i39j46i512j0i512j46i512l2j46i175i199i512j0i512j46i175i199i512j0i512.3246j0j9&sourceid=chrome&ie=UTF-8', headers=headers)
    print("Searching...\n")
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()
    print(location)
    print(time)
    print(info)
    print(weather + "C")
    
city = input("Enter the city you would like to know the weather in here: ")
city = city +" weather"
weather(city)
print("Have a nice day.")