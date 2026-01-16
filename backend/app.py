"""
> pip install "fastapi[standard]"
> fastapi dev backend/app.py
"""

from weather_sentiment_fetcher import WeatherSentimentFetcher
from sqlite_db import SQLiteBase
from supabase_db import SupaBaseDB
from fastapi import FastAPI

import logging
from setup_logging import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


# 1. Create the app
app = FastAPI()


# 2. Load class from .py files in backend folder
weather = WeatherSentimentFetcher()
sqlite_db = SQLiteBase("backend/weather_fetcher.db")
supabase_db = SupaBaseDB()


# 3. Create root
@app.get("/")
def root():
    return {"msg": "Wheather & Sentiment Analysis App"}


# 4. Get weather data
@app.get("/get_weather")
def get_weather(city):
    weather_data = weather.get_weather(city)
    return weather_data


# 5. Get polarity score
@app.get("/get_polarity")
def get_polarity(text):
    polarity = weather.get_sentiment_polarity(text)
    return polarity


# 6. Save data in SQLite database
@app.post("/save_sqlite")
def save_to_sqlite(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
    sqlite_db.create_database()
    sqlite_db.insert_weather_data(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at)


# 7. Save data in Supabase
@app.post("/save_supabase")
def save_to_supabase(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
    supabase_db.insert_weather_data(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at)


# 8. Send to Discord channel
@app.post("/send_to_discord")
def send_to_discord(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
    weather.send_to_discord(city, temp, descr_en, descr_de, user_text, sent_score, fetched_at)