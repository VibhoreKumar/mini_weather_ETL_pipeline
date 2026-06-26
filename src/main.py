from extract import fetch_weather
from transform import build_record
from load import append_record
from cities import CITIES

LOG_PATH  = "../Data/weather_log.txt"

def main():
    success, failed = 0, 0
    for city in CITIES:
        try:
            data = fetch_weather(city["lat"], city["lon"])
        except RuntimeError as e:
            print(f"FAIL  {city['name']}: {e}")
            failed += 1
            continue
        record = build_record(city["name"], data)
        append_record(record, LOG_PATH)
        print(f"OK    {record}")
        success += 1
    print(f"\nDone: {success} succeeded, {failed} failed")

if __name__ == "__main__":
    main()