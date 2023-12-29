from utils import *
import streamlit as st

brand = st.selectbox('Car brand:', BRAND)
status = st.selectbox('Status:', STATUS)
origin = st.selectbox('Origin:', ORIGIN)
style = st.selectbox('Style:', STYLE)
transmission = st.selectbox('Transmission:', TRANSMISSION)
gear = st.selectbox('Gear:', GEAR)
drive = st.selectbox('Wheel drive:', DRIVE)
fuel = st.selectbox('Fuel:', FUEL)
seats = st.selectbox('Number of seats:', SEATS)
doors = st.selectbox('Number of doors:', DOORS)
age = st.slider('Age:', 0, 50, 0)
km = st.slider('Traveled Km:', 0, 150000, 0)

submit_button = st.button('Predict')
if submit_button:
    st.write('Button was clicked!')
