import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

# Load pre-trained model
model = pk.load(open('rf.pkl', 'rb'))

# Streamlit header
st.header('Medical Insurance Premium Predictor')

gender =st.selectbox('Choose Gender', ['Female','Male'])
smoker =st.selectbox('Are you a smoker? ', ['Yes','No'])
region =st.selectbox('Choose Region', ['SouthEast','SouthWest','NorthEast','NorthWest'])
age =st.slider('Enter Age', 5, 80)
bmi =st.slider('Enter BMI', 5, 100)
children =st.slider('Choose No. Of Childrens',0,5)

if gender == 'Female':
    gender=0
else:
    gender=1


if smoker == 'No':
    smoker=0
else:
    smoker=1

if region == 'SouthEast':
    region=0
if region == 'SouthWast':
    region=1
if region == 'NorthEast':
    region=2
else:
    region=3

input_data = (age, gender, bmi, children, smoker, region)
input_data = np.asarray(input_data)
input_data = input_data.reshape(1,-1)
if st.button('Predict'):
    predicted_prem= model.predict(input_data)

    display_string = 'Insurance Premium will be ' + str(predicted_prem[0]) + ' Rupees'

    st.markdown(display_string)
