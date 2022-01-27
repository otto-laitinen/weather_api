import requests

API_KEY = "ccb0d6c22ebf6c83fcba70775076b264"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")

# This is the format we want our request url to be in.
# We have our base url and our query parameters (everything after the question mark).
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
