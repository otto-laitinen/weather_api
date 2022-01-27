import requests

API_KEY = "ccb0d6c22ebf6c83fcba70775076b264"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

# This is the format we want the request url to be in.
# We have the base url and the query parameters (everything after the question mark).
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"

# Use the request module to send an HTTP request.
response = requests.get(request_url)

# HTTP status code '200' means that the request was successful
if response.status_code == 200:
    data = response.json()  # Contains JSON data of a given city as Python dictionary.
    weather = data["weather"][0]["description"]
    print(weather)
    temperature = data["main"]["temp"]
    print(f"{round(temperature - 273.15, 2)} Celsius")  # Celsius = Kelvin - 273.15
else:
    print("An error occurred")
