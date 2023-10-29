# Car Price Prediction
This project is a Car Price Prediction web application that uses Streamlit to provide an interactive interface for exploring car price data and making price predictions based on various features.
## Table of Contents
- [Getting Started](#gettingstarted)
- [Data Preparation](#datapreparation)
- [Navigation](#navigation)
- [Features](#features)
- [Contributing](#contributing)
## Getting Started
Before using the Car Price Prediction web application, you need to set up your environment and load the necessary data. Follow these steps:

1. **Configure the Home Page**: Set the title, icon, layout, and initial sidebar state for the application's home page.
2. **Load the Dataset**: A function, **load_data()**, is provided in the 'main_app.py' file to load the car price dataset. This function also performs data preprocessing tasks, such as extracting car company names, replacing misspelled company names, creating dummy variables, and more. The resulting dataset is used for prediction.
3. **Navigation**: The application provides a navigation sidebar with radio buttons that allow you to switch between different pages: Home, View Data, Visualize Data, and Predict Data.

## Data Preparation
1. **Dataset Loading**: The car price dataset is loaded from the "car-prices.csv" file.
2. **Feature Engineering**: Features such as car company names, numeric values for 'doornumber' and 'cylindernumber', and dummy variables for categorical columns are created.
3. **Data Cleaning**: Misspelled car company names are corrected, and unnecessary columns are dropped.
4. **Data Transformation**: The dataset is prepared for machine learning by converting non-numeric columns to dummy variables.

## Features
1. **Data Exploration**: You can view the raw dataset, analyze it, and create various visualizations.
2. **Machine Learning Predictions**: The application allows you to make car price predictions using machine learning models.
3. **User-Friendly Interface**: Streamlit is used to create an easy-to-use web interface.

## Contributing
Contributions to the Car Price Prediction project are welcome. To contribute, follow these steps:

Fork the repository on GitHub.
1. Create a new branch for your feature or bug fix.
2. Make your changes and commit them with clear, concise commit messages.
3. Push your changes to your fork.
4. Create a pull request to the main repository.
