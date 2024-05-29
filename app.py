import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

data = pd.read_csv('C:/Users/tk_42/AppData/Local/Programs/Python/Python39/Scripts/SoftwareDevTools/vehicles_us.csv')
data['model_year'] = data['model_year'].astype(int, errors = 'ignore')
data['cylinders'] = data['cylinders'].astype(int, errors = 'ignore')
data['odometer'] = data['odometer'].astype(int, errors='ignore')
data['is_4wd'] =  data['is_4wd'].astype(int, errors = 'ignore')
data['date_posted'] = pd.to_datetime(data['date_posted'])

st.header('Data Viewer')
check = st.checkbox('Show Data With No Missing Variables')
if check:
    data_no_na = data.dropna()
    st.dataframe(data_no_na)
else:
    st.dataframe(data)

st.header('Histogram of Car Prices')
car_price_hist = px.histogram(data, x='price', title='Histogram of Car Prices', range_x=[0,50000], color='model')
st.write(car_price_hist)

st.header('Scatterplot of Price vs. Model Year')
price_vs_model_year = px.scatter(data, x='model_year', y='price', title='Scatterplot of Price vs. Model Year', range_x=[1960,2020], color = 'model_year')
st.write(price_vs_model_year)