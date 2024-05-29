#importing neccassary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#reading the data and correcting datatypes
data = pd.read_csv('SoftwareDevTools/vehicles_us.csv')
data['model_year'] = data['model_year'].astype(int, errors = 'ignore')
data['cylinders'] = data['cylinders'].astype(int, errors = 'ignore')
data['odometer'] = data['odometer'].astype(int, errors='ignore')
data['is_4wd'] =  data['is_4wd'].astype(int, errors = 'ignore')
data['date_posted'] = pd.to_datetime(data['date_posted'])

#First visual is a table of the dataframe
st.header('Data Viewer')
check = st.checkbox('Show Data With No Missing Variables') #using checkbox to toggle if the tables shows all rows or all rows with no missing values
if check:
    data_no_na = data.dropna()
    st.dataframe(data_no_na)
else:
    st.dataframe(data)

#creates a histogram of car prices
st.header('Histogram of Car Prices')
car_price_hist = px.histogram(data, x='price', title='Histogram of Car Prices', range_x=[0,50000], color='model')
st.write(car_price_hist)

#creates scatterplot of price vs Model Year
st.header('Scatterplot of Price vs Model Year')
price_vs_model_year = px.scatter(data, x='model_year', y='price', title='Scatterplot of Price vs. Model Year', range_x=[1960,2020], color = 'model_year')
st.write(price_vs_model_year)
