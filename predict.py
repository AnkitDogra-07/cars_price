# S2.1: Import the necessary Python modules and create the 'prediction()' function as directed above.
# Importing the necessary Python modules.
import streamlit as st
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression as lr
from sklearn.metrics import r2_score , mean_absolute_error , mean_squared_error , mean_squared_log_error 
# Define the 'prediction()' function.
@st.cache_data()
def prediction(cars_df , cw , es , hp , dfwd , cc):
  X = cars_df.iloc[: , :-1]
  y = cars_df['price']
  X_train , X_test , y_train , y_test = train_test_split(X , y , random_state = 42 , test_size = 0.33)
  obj_lr = lr()
  obj_lr.fit(X_train , y_train)
  score = obj_lr.score(X_train , y_train)

  price = obj_lr.predict([[cw , es , hp , dfwd , cc]])
  price = price[0]
  
  y_test_pred = obj_lr.predict(X_test)
  test_r2_score = r2_score(y_test , y_test_pred)
  test_mae = mean_absolute_error(y_test , y_test_pred)
  test_msle = mean_squared_log_error(y_test , y_test_pred)
  test_rmse = np.sqrt(mean_squared_error(y_test , y_test_pred))

  return price , score , test_r2_score , test_mae , test_msle , test_rmse

  # S2.2: Define the 'app()' function as directed above.
def app(cars_df):
  st.markdown("<p style='color:blue;font-size:25px'> This app uses <b>Linear Regression</b> to predict the price of a car based on your inputs. </p>" , unsafe_allow_html = True)
  st.subheader("Select Values")
  cw = st.slider("Car Width" , float(cars_df['carwidth'].min()) , float(cars_df['carwidth'].max()))
  es = st.slider("Engine Size" , float(cars_df['enginesize'].min()) , float(cars_df['enginesize'].max()))
  hp = st.slider("Horse Power" , float(cars_df['horsepower'].min()) , float(cars_df['horsepower'].max()))
  dfwd = st.radio("Is it a forward drive wheel car ?" , ("Yes" , "No"))
  if dfwd == "No":
    dfwd = 0
  else:
    dfwd = 1
  cc = st.radio("Is car manufactured by Buick ?" , ("Yes" , "No"))   
  if cc == "No":
    cc = 0
  else:
    cc = 1 
  if st.button("Predict"):
    st.subheader("Prediction Results")
    price , score , test_r2_score , test_mae , test_msle , test_rmse = prediction(cars_df , cw , es , hp , dfwd , cc)
    st.success(f"The predicted price of the car: {price}")
    st.info(f"Acuracy Score of the model: {score}")
    st.info(f"R2_Score of the model: {test_r2_score}")
    st.info(f"Mean Absolute Error: {test_mae}")
    st.info(f"Mean Squared Log Error: {test_msle}")
    st.info(f"Mean Squared Log Error: {test_msle}")