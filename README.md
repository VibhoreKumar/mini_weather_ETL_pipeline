Mini Weather ETL Pipeline

A small ETL pipeline that pulls live weather data for multiple cities from the
Open-Meteo API (free, no API key required), cleans
and classifies each reading, and stores it in a flat file using JSON Lines
format — no database or SQL involved. Built using only Python's built-in
urllib and json modules, no external dependencies.

What it does


Extract — calls the Open-Meteo API for each city in cities.py and
returns the raw JSON response
Transform — pulls the relevant fields out of the nested API response
and classifies each reading into Hot / Cold / Normal based on
temperature thresholds
Load — appends each cleaned record as one JSON object per line to
Data/weather_log.txt. Running the pipeline repeatedly builds a growing
historical log instead of overwriting previous runs
Analyze — a separate read-only script that loads the log file back
and computes basic stats (category breakdown, average temperature per
city) — this is the no-SQL stand-in for what a GROUP BY query would do.


How to run it

No installs needed — everything uses Python's standard library.

bashpython3 main.py      # fetch fresh data for all cities, append to the log
python3 analyze.py   # read the log back and print stats
