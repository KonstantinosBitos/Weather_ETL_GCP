# Weather ETL Pipeline on Google Cloud

## Description
ETL pipeline that fetches hourly weather data from WeatherAPI, transforms it using Pandas, and stores it in BigQuery.

## Architecture

* Extract: A Python script sends HTTP requests to the OpenWeatherMap API to fetch real-time weather data for specific cities.
* Transform: The nested JSON response is flattened and cleaned using Pandas. Data types are enforced to ensure schema consistency.
* Load: The transformed DataFrame is appended to a BigQuery table using the google-cloud-bigquery client.
* Orchestration: Cloud Scheduler triggers the function hourly.

## Tech Stack
- Python (requests, pandas)
- Google Cloud Platform (Cloud Functions, Cloud Scheduler, BigQuery)

## How to Run Locally
1. Install dependencies:
   pip install -r requirements.txt
2. Set your API key in `main.py` or as an environment variable:
   export WEATHER_API_KEY="your_api_key"
3. Run the script:
   python main.py

---

## Connect

**Author:** Konstantinos Bitos  
Email: [bitoskostas1@gmail.com](mailto:bitoskostas1@gmail.com)  
Medium: [@bitoskostas1](https://medium.com/@bitoskostas1)
