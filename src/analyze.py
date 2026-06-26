import json
from collections import Counter

PATH = "../Data/weather_log.txt"
records = []
skipped = 0

with open(PATH) as f:
    for line in f:
        line = line.strip()
        if not line:
            skipped += 1
            continue
        records.append(json.loads(line))

print(f"Total readings: {len(records)} (skipped {skipped} blank line(s))")

by_category = Counter(r["temp_category"] for r in records)
print("Category breakdown:", dict(by_category))

by_city = {}
for r in records:
    by_city.setdefault(r["city"], []).append(r["temperature_c"])

print("\nAverage temp per city:")
for city, temps in by_city.items():
    print(f"  {city}: {sum(temps)/len(temps):.1f}°C across {len(temps)} reading(s)")