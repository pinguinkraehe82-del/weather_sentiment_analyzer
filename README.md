# Weather Sentiment Analyzer

## Introduction
A Python application that retrieves weather data from 
[https://openweathermap.org/](https://openweathermap.org/), analyzes the sentiment of user 
comments, stores the data in an SQLite and a Supabase database and sents motes to Discord.

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

## Author
Simone Gerle

