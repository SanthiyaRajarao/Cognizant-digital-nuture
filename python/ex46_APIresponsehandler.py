import requests

def get_weather(city):
    try:
        if city.strip() == "":
            return "Invalid city name"

        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(url)

        if response.status_code != 200:
            return "Error fetching data"

        data = response.json()

        current = data["current_condition"][0]

        temp = current["temp_C"]
        weather = current["weatherDesc"][0]["value"]

        return f"Temperature: {temp}°C, Condition: {weather}"

    except requests.exceptions.RequestException:
        return "Network error"


print(get_weather("Chennai"))