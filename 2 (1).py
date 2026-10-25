import json
import os
from urllib.parse import urlencode
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

API_KEY = os.environ.get("OPENWEATHER_API_KEY")

if not API_KEY:
    raise SystemExit("Set OPENWEATHER_API_KEY before running this exercise.")

paikkakunta = input("Anna paikkakunnan nimi: ").strip()

if not paikkakunta:
    print("Et antanut paikkakuntaa.")
    raise SystemExit

try:
    geo_params = {
        "q": paikkakunta,
        "limit": 1,
        "appid": API_KEY
    }
    geo_url = "https://api.openweathermap.org/geo/1.0/direct?" + urlencode(geo_params)

    with urlopen(geo_url) as response:
        paikat = json.load(response)

    if not paikat:
        print("Paikkakuntaa ei löytynyt.")
        raise SystemExit

    lat = paikat[0]["lat"]
    lon = paikat[0]["lon"]

    weather_params = {
        "lat": lat,
        "lon": lon,
        "appid": API_KEY,
        "units": "metric",
        "lang": "fi"
    }
    weather_url = "https://api.openweathermap.org/data/2.5/weather?" + urlencode(weather_params)

    with urlopen(weather_url) as response:
        data = json.load(response)

    saateksti = data["weather"][0]["description"]
    lampotila = data["main"]["temp"]

    print(f"Säätila: {saateksti}")
    print(f"Lämpötila: {lampotila:.1f} °C")

except HTTPError as e:
    print(f"HTTP-virhe: {e.code}")
except URLError as e:
    print(f"Verkkovirhe: {e.reason}")