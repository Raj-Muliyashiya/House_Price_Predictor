import streamlit as st
import requests

st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏡",               
)

st.title("Bangalore House Price Predictor")

st.divider()    

@st.cache_data
def get_location_list():
    base_url = requests.get('https://house-price-predictor-2ws5.onrender.com/get_locations')
    return base_url.json()['location']

try:
    location_list = get_location_list()

except:
    st.error("Server is asleep. Please wait a moment and reload.")
    location_list = []

main_location = st.selectbox("Location" ,get_location_list(),index=None, placeholder="Search for a location...")

col1, col2 = st.columns(2)

with col1:
    bhk = st.number_input("BHK", min_value=1 , max_value=8)

with col2:
    bath = st.number_input("Bath", min_value=1 , max_value=8)

sqrft = st.slider("Total Area (sqft)", min_value=700 , max_value=5000)


if st.button("Predict Price"):
    if main_location is None:
        st.error("please select the location")
    else:
        input_data ={
            'location' : main_location,
            'bhk' : bhk,
            'total_sqft' : sqrft,
            'bath' : bath
        }
        with st.spinner():
            json_response = requests.post('https://house-price-predictor-2ws5.onrender.com/predict_home_price', json=input_data)
            response = json_response.json()["the prediction is "]

            final_price = max(10.0, response)
        
        st.metric(label="Estimated Property Price" ,value=f"₹ {final_price:.2f} Lakhs")

        chart_data = {"Your House": final_price, "Average": 90}
        st.bar_chart(chart_data, horizontal=True)