import os
from dotenv import load_dotenv
import logging
from supabase import create_client

load_dotenv()

logger = logging.getLogger(__name__)


class SupaBaseDB:
    def __init__(self):
        logger.debug("Starting Supabase database")
        self.URL = os.getenv("SUPABASE_URL")
        self.KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
        self.client = create_client(self.URL, self.KEY)

    def insert_weather_data(self, city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
        logger.debug("Starting to insert weather data into Supabase database")
        sb = self.client.table("weatherfetcher").insert({
            "city": city,
            "temperature": temp,
            "descr_en": descr_en,
            "descr_de":descr_de,
            "user_text": user_text,
            "sent_score": sent_score,
            "fetched_at": fetched_at
        }).execute()
        logger.info("Successfully inserted data into Supabase database")

        return sb.data[0]