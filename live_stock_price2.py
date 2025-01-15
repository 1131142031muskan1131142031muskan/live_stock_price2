import streamlit as st
import requests

# Title of the app
st.title("Live Stock Price Tracker")

# Sidebar Inputs
ticker = st.sidebar.text_input("Enter Stock Ticker Symbol (e.g., INFY)", "INFY")
exchange = st.sidebar.text_input("Enter Exchange (e.g., NSE)", "NSE")

# API URL (use the deployed URL of your Flask API here)
api_url = f'http://https://flask-api-2-mgs8.onrender.com/get_stock_price?ticker=INFY&exchange=NSE/get_stock_price?ticker={ticker}&exchange={exchange}'

# Fetch Stock Price
try:
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if "price" in data:
            st.subheader("Current Stock Price")
            st.write(f"The stock price of {data['ticker']} on {data['exchange']} is: ₹{data['price']}")
        else:
            st.error(data.get("error", "Unknown error occurred"))
    else:
        st.error(f"API request failed with status code {response.status_code}")
except Exception as e:
    st.error(f"Error connecting to the API: {str(e)}")
