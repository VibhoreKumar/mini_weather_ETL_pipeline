# mini_weather_ETL_pipeline
A mini ETL pipeline built with pure Python — no pandas,no SQL—that pulls live weather data for 15 cities from the free Open-Meteo API,classifies each reading,and stores results as JSON Lines in a flat file.Includes proper error handling for network failures and malformed data,with append-mode logging that builds a real historical dataset over time.
