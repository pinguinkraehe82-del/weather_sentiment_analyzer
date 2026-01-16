import os
from dotenv import load_dotenv
import logging
import requests
from datetime import datetime, timezone
from textblob import TextBlob


load_dotenv()

logger = logging.getLogger(__name__)

class WeatherSentimentFetcher:
    """
    A Python application that retrieves current weather data for chosen cities using the OpenWeatherMap API
    and stores the information in a local SQLite database.
    """

    def __init__(self):
        logger.debug("Starting Weather Fetcher...")
        self.API_KEY = os.getenv("API_KEY")
        self.WEBHOOK = os.getenv("WEBHOOK")
        logger.info("Successfully started weather fetcher")


    def get_weather(self, city):
        logger.debug("Starting weather fetching by city...")
        URL = "https://api.openweathermap.org/data/2.5/weather"

        # Parameters for fetching data from English website.
        params_en = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric",
            "lang": "en"
        }

        # Parameters for fetching data from German website.
        params_de = {
            "q": city,
            "appid": self.API_KEY,
            "units": "metric",
            "lang": "de"
        }

        # Sent GET request
        try:
            # EN
            logger.debug("Starting to send GET request for response_en")
            response_en = requests.get(URL, params_en)
            response_en.raise_for_status()
            data_en = response_en.json()

            # DE
            logger.debug("Starting to send GET request for response_de")
            response_de = requests.get(URL, params_de)
            response_de.raise_for_status()
            data_de = response_de.json()

            logger.info("GET requests successful")

        except requests.exceptions.RequestException as e:
            logger.error(f"API requests failed by user input: {city} {e}")

        else:
            logger.debug("Starting to fetch temperature, description and time")
            temp = data_en["main"]["temp"]
            descr_en = data_en["weather"][0]["description"]
            descr_de = data_de["weather"][0]["description"]
            fetched_at_unix = data_en['dt']
            fetched_at = datetime.fromtimestamp(fetched_at_unix, tz=timezone.utc).astimezone().strftime(
                "%Y-%m-%d %H:%M:%S")
            logger.info("Successfully fetched temperature, description and time")

            return {
                "city": city,
                "temp": temp,
                "descr_en": descr_en,
                "descr_de": descr_de,
                "fetched_at": fetched_at
            }


    def get_sentiment_polarity(self, text):
        logger.debug("Starting to analyze polarity of user input")
        try:
            list_of_scores = []

            blob = TextBlob(text)

            for sentence in blob.sentences:
                list_of_scores.append(sentence.sentiment.polarity)

            # Check if sentences were found
            if len(list_of_scores) == 0:
                logger.warning("No sentences found in text")
                return 0

        except Exception as e:
            logger.error(f"Error during polarity analysis: {e}")

        else:
            mean_polarity = sum(list_of_scores) / len(list_of_scores)

            logger.info("Successfully analyzed polarity of user input")

            return {"mean_polarity": mean_polarity}


    def send_to_discord(self, city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
        # Message for Discord
        data = {"content": f"City: {city}, \nTemperature: {temp}, \nDescription (EN): {descr_en}, \nDescription (DE): {descr_de}, \nUser message: {user_text}, \nPolarity: {sent_score}, \nFetched at: {fetched_at}"}

        # Send message to URL
        try:
            logger.debug("Starting to send user message und text polarity to discord")
            response = requests.post(self.WEBHOOK, json=data)
            response.raise_for_status()

            logger.info("Successfully sent user message and text polarity to discord")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to send user message and text polarity to discord: {e}")
