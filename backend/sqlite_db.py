import logging
import sqlite3


logger = logging.getLogger(__name__)


class SQLiteBase:
    def __init__(self, db_path):
        logger.debug("Starting SQLite database")
        self.db_path = db_path

    def create_database(self):
        logger.debug("Starting to create an SQLite database")
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        sql = """CREATE TABLE IF NOT EXISTS weather_fetched
        (
            "ID" INTEGER PRIMARY KEY, 
            "City name" TEXT,
            "Temperature" REAL,
            "Description English" TEXT,
            "Description German" TEXT,
            "User text" TEXT,
            "Sentiment score" REAL,
            "Fetched at" TEXT
        )"""

        c.execute(sql)
        conn.commit()
        conn.close()

    def insert_weather_data(self, city, temp, descr_en, descr_de, user_text, sent_score, fetched_at):
        logger.debug("Starting to insert weather data into SQLite database")
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()

        params = (city, temp, descr_en, descr_de, user_text, sent_score, fetched_at)

        sql = """INSERT INTO weather_fetched
                 ("City name", "Temperature", "Description English", "Description German","User text", "Sentiment score", "Fetched at") 
              VALUES (?, ?, ?, ?, ?, ?, ?)"""

        c.execute(sql, params)
        conn.commit()
        conn.close()
        logger.info("Successfully inserted data into SQLite database")