# Define a function 'app()' which accepts 'car_df' as an input.
import streamlit as st
import numpy as np 
import pandas as pd
# S6.2: Design the View Data page of the multipage app.
# Import necessary modules
import numpy as np  
import pandas as pd
import streamlit as st

# Define a function 'app()' which accepts 'car_df' as an input.
def app(cars_df):
    st.header("View Data")
    # Add an expander and display the dataset as a static table within the expander.
    with st.expander("View Dataset"):
        st.table(cars_df)
    
    # ADD NEW CODE HERE.
    st.subheader("Column's Description")
    col1 , col2 = st.columns(2)
    with col1 :
      if st.checkbox("Show all column names"):
        st.table(list(cars_df.columns))

    with col2:
      if st.checkbox("View column data"):
        columns_data = st.selectbox("Select_columns" , ("enginesize" , "horsepower" , "carwidth" , "drivewheel_fwd" , "price"))
        if columns_data == "drivewheel_fwd":
          st.write(cars_df["drivewheel_fwd"]) 

        elif columns_data == "enginesize":
          st.write(cars_df["enginesize"])

        elif columns_data == "horsepower":
          st.write(cars_df["horsepower"])

        elif columns_data == "carwidth":
          st.write(cars_df["carwidth"])

        else:
          st.write(cars_df['price'])

    if st.checkbox("Show Summary"):
      st.table(cars_df.describe())          