import streamlit as stl
import requests


stl.title("Bangalore House Price Predictor")

base_url = requests.get('http://localhost:8000/get_locations')

location_list = base_url.json()

stl.write(detail)
