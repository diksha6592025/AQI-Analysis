import streamlit as st
import pandas as pd
import plotly.express as px
from prophet import Prophet

# Page config
st.set_page_config(page_title="AQI Dashboard", layout="wide")

# Title
st.title("🌫️ Air Quality Index (AQI) Interactive Dashboard – India")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("city_day.csv")
    df['Date'] = pd.to_datetime(df['Date'])
    df.ffill(inplace=True)
    return df

df = load_data()

# Sidebar
st.sidebar.header("Filter Options")

city = st.sidebar.selectbox(
    "Select City",
    sorted(df['City'].unique())
)

pollutant = st.sidebar.selectbox(
    "Select Parameter",
    ['AQI', 'PM2.5', 'PM10', 'NO2', 'SO2', 'CO']
)

# Filter data
city_df = df[df['City'] == city]

# KPI Metrics
st.subheader(f"📍 {city} – Key Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Average AQI", int(city_df['AQI'].mean()))
col2.metric("Maximum AQI", int(city_df['AQI'].max()))
col3.metric("Minimum AQI", int(city_df['AQI'].min()))

# Trend chart
st.subheader(f"📈 {pollutant} Trend Over Time")

fig = px.line(
    city_df,
    x='Date',
    y=pollutant,
    title=f"{pollutant} Levels in {city}",
)
st.plotly_chart(fig, use_container_width=True)

# AQI Category distribution
st.subheader("🚦 AQI Category Distribution")

bins = [0, 50, 100, 200, 300, 400, 500]
labels = ['Good', 'Satisfactory', 'Moderate', 'Poor', 'Very Poor', 'Severe']
city_df['AQI_Category'] = pd.cut(city_df['AQI'], bins=bins, labels=labels)

cat_fig = px.histogram(
    city_df,
    x='AQI_Category',
    title="AQI Categories",
)
st.plotly_chart(cat_fig, use_container_width=True)

# Forecasting
st.subheader("🔮 AQI Forecast (Next 6 Months)")

forecast_df = city_df[['Date', 'AQI']]
forecast_df.columns = ['ds', 'y']

model = Prophet()
model.fit(forecast_df)

future = model.make_future_dataframe(periods=180)
forecast = model.predict(future)

forecast_fig = px.line(
    forecast,
    x='ds',
    y='yhat',
    title=f"{city} AQI Forecast (Prophet Model)"
)
st.plotly_chart(forecast_fig, use_container_width=True)

st.success("✅ Interactive AQI Dashboard Loaded Successfully")
