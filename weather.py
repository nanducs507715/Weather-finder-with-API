import requests

api_key = "bfd877a695803bcaf596da0aa09e42c9"
api_l = "http://api.openweathermap.org/data/2.5/weather"  # current weather endpoint

def get_weather(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric",
    }
    res = requests.get(api_l, params=params)
    data = res.json()

    if data.get("cod") != 200:
        print("Error:", data.get("message"))
        return

    print(f"""
City: {city}
Temperature: {data["main"]["temp"]}
Weather: {data["weather"][0]["description"]}
    """)

city = input("Enter your city: ")
get_weather(city)
