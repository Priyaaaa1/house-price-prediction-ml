import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load your best model (e.g., CatBoost or Random Forest)
model = joblib.load('models/random_forest_model.pkl')

st.set_page_config(page_title="Real Estate Investment Analyzer", page_icon="🏠")

st.title("🏠 Real Estate Valuation & Deal Analyzer")
st.markdown("Enter property details to find out the market value and investment potential.")

with st.sidebar:
    st.header("Property Details")
    sqft = st.number_input("Total Square Footage", min_value=500, max_value=10000, value=1500)
    beds = st.slider("Bedrooms", 1, 6, 3)
    baths = st.slider("Bathrooms", 1, 5, 2)
    age = st.number_input("Property Age (Years)", 0, 100, 10)
    
    # User's current offer price
    asking_price = st.number_input("Asking Price ($)", value=250000)

if st.button("Analyze Deal"):
    # 1. Transform inputs into the format your model expects
    # (Note: You must match the exact feature order from your training)
    features = np.array([[sqft, beds, baths, age]]) 
    prediction = model.predict(features)[0]
    
    # 2. Deal Analyzer Logic
    diff = prediction - asking_price
    percent_diff = (diff / asking_price) * 100

    st.subheader(f"Estimated Market Value: ${prediction:,.2f}")

    if diff > (0.1 * asking_price):
        st.success(f"🔥 GREAT DEAL: This property is undervalued by {percent_diff:.1f}%!")
    elif diff < (-0.1 * asking_price):
        st.error(f"🚩 OVERPRICED: This property is valued at {abs(percent_diff):.1f}% above market.")
    else:
        st.info("⚖️ FAIR VALUE: The asking price matches the market valuation.")