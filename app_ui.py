import streamlit as st
import requests


st.title("Bangalore House Price Predictor")

base_url = requests.get('http://localhost:8000/get_locations')
location_request = base_url.json()
location_list = location_request['location']

main_location = st.selectbox("Location" ,location_list,index=None)