import requests
import csv
from datetime import date

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


    with open("Weather_history.csv","a",newline="") as f:
        w = csv.writer(f)
        w.writerow([city,data["main"]["temp"],data["weather"][0]["description"], date.today()])
        f.close()

def history():
    f = open("Weather_history.csv","r")
    r = csv.reader(f)
    for i in r:
        print(i)
    f.close()
    

print("""Choice: 
    1. View weather
    2. Check old Records
    3. Exit
    """)
while True:
    _choice = int(input("Choice: "))
    if _choice==1:
        city = input("Enter your city: ")
        get_weather(city)
    elif _choice==2:
        history()
    elif _choice==3:
        break
    else:
        print("Wrong Choice")
    print("----------------------------------------")
