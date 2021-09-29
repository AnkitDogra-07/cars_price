# S1.1: Design the "Visualise Data" page of the multipage app.
# Import necessary modules 
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
# Define a function 'app()' which accepts 'car_df' as an input.
def app(cars_df):
  st.header("Visualize Data")
  st.set_option("deprecation.showPyplotGlobalUse" , False)
  st.subheader("Scatter Plot")
  feat_lst = st.multiselect("Select Values for X-Axis" , ("carwidth" , "enginesize" , "horsepower" , "drivewheel_fwd" , "car_company_buick"))
  for i in feat_lst:
    st.subheader(f"Scatter Plot between {i} and price")
    plt.figure(figsize = (15 , 10))
    sns.scatterplot(cars_df[i] ,cars_df['price'])
    st.pyplot()

  st.subheader("Visualisation Selector")
  plt_type = st.multiselect("Select Chart or Plot" , ("Histogram" , "Boxplot" , "Correlation Heatmap"))  
  if "Histogram" in plt_type:
    st.subheader(f"Histogram")
    columns = st.selectbox("Select the Column to create Histogram" , ("carwidth" , "enginesize" , "horsepower"))
    plt.figure(figsize = (15 , 10))
    plt.title(f"Histogram for {columns}")
    plt.hist(cars_df[columns] , bins = "sturges" , edgecolor = "Black")
    st.pyplot()

  if "Boxplot" in plt_type:
    st.subheader(f"Histogram")
    columns = st.selectbox("Select the Column to create Boxplot" , ("carwidth" , "enginesize" , "horsepower"))
    plt.figure(figsize = (15 , 10))
    plt.title(f"Boxplot for {columns}")
    sns.boxplot(cars_df[columns])
    st.pyplot()  

  if "Correlation Heatmap" in plt_type:
    st.subheader(f"Correlation Heatmap")
    plt.figure(figsize = (15 , 10))
    sns.heatmap(cars_df.corr() , annot = True)
    st.pyplot() 