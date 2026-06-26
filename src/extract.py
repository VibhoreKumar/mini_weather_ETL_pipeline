import json
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError, HTTPError

def fetch_weather(lat, lon):
    params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,wind_speed_10m"
    }
    url = "https://api.open-meteo.com/v1/forecast?" + urlencode(params)
    try:
        with urlopen(url, timeout=10) as response:
            return json.load(response,)
    except HTTPError as e:
        raise RuntimeError(f"HTTP error {e.code} from API") from e
    except URLError as e:
        raise RuntimeError(f"Network error: {e.reason}") from e