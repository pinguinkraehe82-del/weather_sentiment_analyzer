"""
> streamlit run frontend/app.py
"""

import requests
import streamlit as st
import logging

logger = logging.getLogger(__name__)


def main():
    if "weather_data" not in st.session_state:
        st.session_state.weather_data = None

    if "polarity" not in st.session_state:
        st.session_state.polarity = None

    # 1- Add page title
    st.title("Weather App (OpenWeatherMap)")

    # 2. Add input field
    city = st.text_input("Enter a city", "")

    # 3. Add a button to fetch weather data
    if st.button("Get weather"):
        try:
            # Send get request to FastAPI
            logger.debug("Starting to get weather data from backend")
            weather_response = requests.get("http://127.0.0.1:8000/get_weather", params={"city": city})
            weather_response.raise_for_status()
            logger.info("Successfully retrieved weather data from backend")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get weather data from backend: {e}")

        else:
            weather_data = weather_response.json()
            city = weather_data["city"]
            temp = weather_data["temp"]
            descr_en = weather_data["descr_en"]
            descr_de = weather_data["descr_de"]
            fetched_at = weather_data["fetched_at"]
            st.session_state.weather_data = city, temp, descr_en, descr_de, fetched_at

    # 4. Show weather data
    if st.session_state.weather_data is not None:
        city, temp, descr_en, descr_de, fetched_at = st.session_state.weather_data

        # Show feedback
        st.markdown(f"# {city}")
        # st.markdown(f"### Temperature")
        # st.write(f"{temp}°C.")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### Temperature")
            st.write(f"{temp}°C")

        with col2:
            st.markdown("### Description (EN)")
            st.write(f"{descr_en}")

        with col3:
            st.markdown("### Description (DE)")
            st.write(f"{descr_de}")

    # 5. Add text area for user comment
    comment = st.text_area("Comment", value="")

    # 6. Get polarity for user comment
    if st.button("Get comment polarity"):
        try:
            # Send get request to FastAPI
            logger.debug("Starting to get polarity score from backend")
            polarity_response = requests.get("http://127.0.0.1:8000/get_polarity", params={"text": comment})
            polarity_response.raise_for_status()
            logger.info("Successfully retrieved polarity score from backend")

        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to get polarity score from backend: {e}")

        else:
            polarity_json = polarity_response.json()
            polarity = polarity_json["mean_polarity"]
            st.session_state.polarity = polarity

    # 7. Show polarity
    if st.session_state.polarity is not None:
        st.success(f"The polarity of your comment is {st.session_state.polarity}")

    # 8. Save data in databases and discord channel
    if st.button("Save"):
        if st.session_state.weather_data is not None:
            city, temp, descr_en, descr_de, fetched_at = st.session_state.weather_data
            polarity = st.session_state.polarity
            params = {
                "city": city,
                "temp": temp,
                "descr_en": descr_en,
                "descr_de": descr_de,
                "user_text": comment,
                "sent_score": polarity,
                "fetched_at": fetched_at
            }

            # Save in SQLite database
            try:
                logger.debug("Starting to save data in SQLite database")
                sqlite_response = requests.post("http://127.0.0.1:8000/save_sqlite", params=params)
                sqlite_response.raise_for_status()
                logger.info("Successfully saved data in SQLite database")

            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to save data in SQLite database: {e}")

            # Save in Supabase database
            try:
                logger.debug("Starting to save data in Supabase database")
                supabase_response = requests.post("http://127.0.0.1:8000/save_supabase", params=params)
                supabase_response.raise_for_status()
                logger.info("Successfully saved data in Supabase database")

            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to save data in Supabase database: {e}")

            # Send data to Discord
            try:
                logger.debug("Starting to send data to Discord webhook")
                discord_response = requests.post("http://127.0.0.1:8000/send_to_discord", params=params)
                discord_response.raise_for_status()
                logger.info("Successfully send data to discord")

            except requests.exceptions.RequestException as e:
                logger.error(f"Failed to send data to Discord: {e}")

            else:
                st.success("Data successfully saved")





if __name__ == "__main__":
    main()