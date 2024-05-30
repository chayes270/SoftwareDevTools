## Project_4-SoftwareDevTools
## This program will be used in conjuction with Render to create 3 visualizations of the car data in the vehicles_us.csv
## This program will create a table of the data, a histogram of the data, and a scatterplot.



#importing neccassary libraries
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

#reading the data and correcting datatypes
data = pd.read_csv('vehicles_us.csv') #allows Render to read the csv since it is in the same repository as app.py
#the line below is my unique file path where vehicles_us.csv is stored. To use this file on your local machine, you must use the file path where you will save
#vehicles.csv
#data = pd.read_csv('C:/Users/tk_42/AppData/Local/Programs/Python/Python39/Scripts/SoftwareDevTools/vehicles_us.csv')
 
data['model_year'] = data['model_year'].astype(int, errors = 'ignore')
data['is_4wd'] =  data['is_4wd'].astype(int, errors = 'ignore')
data['date_posted'] = pd.to_datetime(data['date_posted'])

#Next section is cleaning up the data

# Group by car model and calculate the mean number of cylinders for each model
model_cylinder_means = data.groupby(['model'])['cylinders'].mean()

# Define a function to fill missing values with the model's mean cylinders
def fill_missing_cylinders(row):
    if pd.isnull(row['cylinders']):
        return model_cylinder_means[row['model']]
    else:
        return row['cylinders']

# Apply the function to fill missing values in the 'cylinders' column
data['cylinders'] = data.apply(fill_missing_cylinders, axis=1)


# Group by car model and calculate the mean number of miles for each model
model_odometer_means = data.groupby(['model'])['odometer'].mean()

# Define a function to fill missing values with the model's mean miles
def fill_missing_odometer(row):
    if pd.isnull(row['odometer']):
        return model_odometer_means[row['model']]
    else:
        return row['odometer']

# Apply the function to fill missing values in the 'odometer' column
data['odometer'] = data.apply(fill_missing_odometer, axis=1)


# Filling missing values in 'paint_color' column with 'Unkown'
data['paint_color'] = data['paint_color'].fillna('Unkown')


#Since only a couple thousand rows still have some missing values (out of over 50,000 rows), I believe it is safe to drop these columns
data.dropna(subset=["model_year", 'odometer'], inplace=True)


#First visual is a table of the dataframe
st.title('SoftwareDevTools-Project_4')
st.header('Data Viewer')
st.dataframe(data)

#creates a histogram of car prices
st.header('Histogram of Car Prices')
unique_types_hist = data['type'].unique()

selected_types_hist = st.multiselect(
    'Select types to highlight histogram',
    unique_types_hist,
    default=unique_types_hist  # Default to all categories selected
)
filtered_data_hist = data[data['type'].isin(selected_types_hist)]



car_price_hist = px.histogram(filtered_data_hist, x='price', title='Histogram of Car Prices', range_x=[0,50000], color='type')
car_price_hist.update_layout(
    xaxis_title_text = 'Price', 
    yaxis_title_text = 'Number of Vehicles'
    )
st.write(car_price_hist)

#creates scatterplot of price vs Model Year
check = st.checkbox('Show Scatterplot of Price vs Model Year')
unique_types = data['type'].unique()

selected_types = st.multiselect(
    'Select types to highlight',
    unique_types,
    default=unique_types  # Default to all categories selected
)
filtered_data = data[data['type'].isin(selected_types)]

if(check):
    st.header('Scatterplot of Price vs Model Year')
    price_vs_model_year = px.scatter(filtered_data, x='model_year', y='price', title='Scatterplot of Price vs. Model Year', range_x=[1960,2020],range_y=[0,100000], color='type')
    st.write(price_vs_model_year)
else:
    st.header('Scatterplot of Price vs Odometer')
    price_vs_odometer = px.scatter(filtered_data, x='odometer', y='price', title='Scatterplot of Price vs. Odometer Reading', range_x=[0,400000], range_y=[0,200000], color='type')
    st.write(price_vs_odometer)