```headlines.py
from xmd import Message
import requests
def headlines_plugin(msg: Message):
    api_key = "YOUR_NEWS_API_KEY"
    response = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}")
    headlines_data = response.json()["articles"]
    headlines_text = "Top News Headlines:
"
    for headline in headlines_data[:5]:
        headlines_text += f"{headline['title']}
"
    msg.reply(headlines_text)


weather.py
from xmd import Message
import requests
def weather_plugin(msg: Message):
    api_key = "YOUR_WEATHER_API_KEY"
    location = msg.text.split("/weather ")[1]
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}")
    weather_data = response.json()
    weather_text = f"Weather in {location}:
Temperature: {weather_data['main']['temp']}°C
Conditions: {weather_data['weather'][0]['description']}"
    msg.reply(weather_text)
sports.py
from xmd import Message
import requests
def sports_plugin(msg: Message):
    api_key = "YOUR_SPORTS_API_KEY"
    response = requests.get(f"https://newsapi.org/v2/top-headlines?category=sports&apiKey={api_key}")
    sports_data = response.json()["articles"]
    sports_text = "Top Sports Headlines:
"
    for article in sports_data[:5]:
        sports_text += f"{article['title']}
"
    msg.reply(sports_text) ```
