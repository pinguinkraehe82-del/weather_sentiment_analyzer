# Weather Sentiment Analyzer

## Introduction
End-to-end data science application that combines real-time weather data with sentiment analysis of user input.

This project demonstrates the development of a complete data-driven system – from data acquisition and processing to model integration and deployment via an API-based architecture.


## Key Features

- Real-time weather data via the OpenWeatherMap API  
- Sentiment analysis of user input  
- REST API for data processing and serving (FastAPI)  
- Interactive user interface (Streamlit)  
- Data storage using SQLite and Supabase  
- Integration with external services (Discord webhook)  


## Architecture

```
Streamlit (Frontend)
        ↓
FastAPI (Backend)
        ↓
External APIs (OpenWeather)
        ↓
Database (SQLite / Supabase)
        ↓
External Services (Discord Webhook)
```

## 🛠️ Tech Stack

- **Python**
- **FastAPI** (backend / REST API)
- **Streamlit** (frontend)
- **Pandas, NumPy** (data processing)
- **Machine Learning / Sentiment Analysis**
- **SQLite / Supabase** (data storage)


## Functionality

1. User inputs a city and a text message  
2. The application fetches real-time weather data via an external API  
3. Sentiment analysis is performed on the user input  
4. Results are stored in a database  
5. Optionally, results are sent to a Discord webhook  
6. Results are displayed in the frontend  


## Installation
1. Clone repository
~~~bash
> git clone https://github.com/pinguinkraehe82-del/weather_sentiment_analyzer.git
~~~

2. Set virtual environment

~~~bash
> python -m venv venv
# Windows
> venv\Scripts\activate
# Linux/Mac:
> source venv/bin/activate
~~~

3. Install dependencies
~~~bash
> pip install -r requirements.txt
~~~

4. Create `.env` file (see `sample.env`)
~~~bash
API_KEY=yourkey
WEBHOOK=yourkey
SUPABASE_URL=yourkey
SUPABASE_SERVICE_ROLE_KEY=yourkey
~~~


## Usage
Start backend:
~~~bash
> pip install "fastapi[standard]"
> fastapi dev backend/app.py
~~~

Start frontend:
~~~bash
> pip install streamlit
> > streamlit run frontend/app.py
~~~


## Structure
~~~bash
weather_sentiment_analyzer/
├── backend/
│   ├── app.py
│   ├── weather_sentiment_fetcher.py
│   ├── sqlite_db.py
│   ├── supabase_db.py
│   └── setup_logging.py
├── frontend/
│   └── app.py
├── logging/
│   ├── logging.ini
│   └── app.log
├── .env
├── requirements.txt
└── README.md
~~~


## Project Goals

This project demonstrates:

- Development of end-to-end data science applications  
- Integration of external APIs into data workflows  
- Application of machine learning in real-world scenarios  
- Combining data analysis, backend development, and frontend visualization  


## Author
Simone Gerle

