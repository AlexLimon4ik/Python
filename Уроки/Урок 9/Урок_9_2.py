import requests 
import bs4

def get_weather(city="Kiev"):
    city = city.replace(" ", "+")

    url = f"https://wttr.in/{city}?format=j1" #JSON формат

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()

            current = data["current_condition"][0]
            temperature = current["temp_C"]
            weather_desc = current["weatherDesc"][0]["value"]
            feels_like = current["FeelsLikeC"]


            print(f"Погода у {city}:")
            print(f"Температура: {temperature}°C")
            print(f"Відчувається як: {feels_like}°C")
            print(f"Стан: {weather_desc}")
        else:
            print("Помилка при отриманні даних")
    except Exception as a: 
        print(a)

get_weather("Кременчук")

def get_weather_html(city="Kiev"):
    city = city.replace(" ", "+")
    url = f"https://wttr.in/{city}?m"

    response = requests.get(url)
    soup = bs4.BeautifulSoup(response.text, "html.parser")

    print(soup.text)

get_weather_html("Кременчук")