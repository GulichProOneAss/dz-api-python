import requests


API_KEY = "1e6d1b880c148e0ef1e5e36f759a4cab"          # ←←← замените на свой настоящий ключ!
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",          # Цельсий
        "lang": "ru"                # описание погоды на русском
    }
    
    try:
        response = requests.get(BASE_URL, params=params, timeout=12)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("cod") != 200:
            print(f"Ошибка API: {data.get('message', 'Неизвестная ошибка')}")
            return
        
        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        city_name = data["name"]
        
        print(f"\nПогода в городе {city_name}:")
        print(f"Температура: {temp} °C")
        print(f"Описание:    {description.capitalize()}")
        
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            print(f"Город '{city}' не найден.")
        else:
            print(f"HTTP ошибка: {http_err}")
    except requests.exceptions.RequestException as e:
        print(f"Ошибка соединения: {e}")


if __name__ == "__main__":
    print("Получение текущей погоды (OpenWeatherMap)")
    print("Введите название города (на английском или русском), например:")
    print("  Moscow    Paris    Санкт-Петербург    London\n")
    
    while True:
        city = input("Город (или 'выход' для завершения): ").strip()
        if city.lower() in ("выход", "exit", "q"):
            print("До свидания!")
            break
        if not city:
            print("Введите название города.")
            continue
        
        get_weather(city)
        print()