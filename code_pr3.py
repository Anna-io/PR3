import requests

api_key = "YOUR_API_KEY"
city = "Kharkiv"

url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    temperature = data["main"] ["temp"]
    description = data["weather"] [0] ["description"]
    print(f"The weather in {city} is {description} with temperature of {temperature} K.")
else:
    print("Error:", response.status_code)
