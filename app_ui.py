import streamlit as st
import requests


st.title("Bangalore House Price Predictor")

base_url = requests.get('http://localhost:8000/get_locations')
location_request = base_url.json()
location_list = (location_request['location'])

main_location = st.selectbox("Location" ,location_list,index=None, placeholder="Search for a location...")

col1, col2 = st.columns(2)

with col1:
    bhk = st.number_input("BHK", min_value=1 , max_value=10)

with col2:
    bath = st.number_input("Bath", min_value=1 , max_value=10)

sqrft = st.slider("Total Area (sqft)", min_value=300 , max_value=10000)


if st.button("Predict Price"):
    if main_location is None:
        st.error("please select the location")
    else:
        inpud_data ={
            'location' : main_location,
            'bhk' : bhk,
            'total_sqft' : sqrft,
            'bath' : bath
        }

        response = requests.post('http://localhost:8000/predict_home_price', json=inpud_data)
        response = response.json()
        
        st.metric(label="Estimated Property Price" ,value=f"₹ {response["the prediction is "]:.2f} Lakhs")
        st.balloons()
