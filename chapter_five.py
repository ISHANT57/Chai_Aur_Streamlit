import streamlit as st
import pandas as pd
import requests

# Title
st.title("💱 Live Currency Converter")

# Input: Amount in INR
amount = st.number_input("Enter the amount in INR:", min_value=1)

# Input: Target currency
target_currency = st.selectbox("Convert to:", ["USD", "EUR", "GBP", "JPY", "CNY", "AUD"])

# Convert button
if st.button("Convert"):
    # Fetch exchange rates from API
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        
        # Get rate for selected currency
        if target_currency in data["rates"]:
            rate = data["rates"][target_currency]
            converted = round(rate * amount, 2)

            st.success(f"{amount} INR is equal to {converted} {target_currency}")
        else:
            st.error("Selected currency not available in API data")
    else:
        st.error("❌ Failed to retrieve exchange rates. Try again later.")
