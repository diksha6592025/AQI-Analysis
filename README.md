# Air Quality Index (AQI) Interactive Dashboard – Indian Cities

## 📌 Project Overview
This project analyzes historical Air Quality Index (AQI) data of major Indian cities and provides future AQI forecasting using time-series models.

An interactive dashboard is built using Streamlit to visualize AQI trends, pollutant levels, and forecasts.

## 🎯 Objectives
- Analyze AQI trends across Indian cities
- Identify high-risk pollution zones
- Forecast AQI levels for the next 6 months
- Provide interactive visual insights for decision-making

## 📊 Dataset
Source: Central Pollution Control Board (CPCB), Government of India  
Accessed via a compiled CPCB dataset available on Kaggle.

File used:
- `city_day.csv`

## 🛠 Technologies Used
- Python
- Google Colab
- Pandas, NumPy
- Plotly
- Streamlit
- Facebook Prophet
- Statsmodels (ARIMA)

## 🚀 How to Run the Project
```bash
pip install -r requirements.txt
streamlit run app.py

This directory includes a few sample datasets to get you started.

*   `california_housing_data*.csv` is California housing data from the 1990 US
    Census; more information is available at:
    https://docs.google.com/document/d/e/2PACX-1vRhYtsvc5eOR2FWNCwaBiKL6suIOrxJig8LcSBbmCbyYsayia_DvPOOBlXZ4CAlQ5nlDD8kTaIDRwrN/pub

*   `mnist_*.csv` is a small sample of the
    [MNIST database](https://en.wikipedia.org/wiki/MNIST_database), which is
    described at: http://yann.lecun.com/exdb/mnist/

*   `anscombe.json` contains a copy of
    [Anscombe's quartet](https://en.wikipedia.org/wiki/Anscombe%27s_quartet); it
    was originally described in

    Anscombe, F. J. (1973). 'Graphs in Statistical Analysis'. American
    Statistician. 27 (1): 17-21. JSTOR 2682899.

    and our copy was prepared by the
    [vega_datasets library](https://github.com/altair-viz/vega_datasets/blob/4f67bdaad10f45e3549984e17e1b3088c731503d/vega_datasets/_data/anscombe.json).
