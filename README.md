# Phonepe Pulse Data Visualization and Exploration:A User-Friendly Tool Using Streamlit and Plotly
## Overview
PhonePe Pulse Data Visualization is a project aimed at analyzing and visualizing transaction data and user behavior on the PhonePe platform. The project utilizes Python libraries such as Pandas, Plotly, and Streamlit to retrieve, process, and visualize the data which is stored in a MySQL database. Through interactive visualizations, we can gain insights into various aspects of PhonePe transactions, including transaction trends, transaction types, user demographics, geographic analysis, and more.
## Table of Contents
- [Key Technologies and Skills](#key-technologies-and-skills)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Approach](#approach)
- [Contact](#contact)
# Key Technologies and Skills
- Python Scripting
- Streamlit
- Data Cleaning and analysis
- Pandas-Dataframe
- Database management using MySql
- Data visualization using Plotly
# Installation
To run this project, please install below python packages as prerequisites and download git from below mentiond link.
Git - (https://git-scm.com/downloads)
```bash
pip install streamlit
pip install mysql-connector-python
pip install pandas
pip install pymysql sqlalchemy
pip install plotly
pip install numpy
```
# Usage
To use this project, Please follow the below steps.
- To clone the PhonePe Pulse data:```git clone https://github.com/PhonePe/pulse.git```
- To clone this repository: ```git clone https://github.com/Gokulakkrizhna/PhonePe-Pulse.git```
- Install the required packages: ```pip install -r requirements.txt ```
- To extract data and store in Mysql:```python Datacoll_dataclean.py```
- Run the Streamlit app: ```streamlit run Dataextract_visual.py```
- Access the app in your browser at ```http://localhost:8501```
# Features
- Fetch PhonePe transaction and user data from Github
- Data Cleaning and pre-processing
- Store data in a MySQL database
- Analyzing the data with the help of SQL queries
- Visualize data using Plotly and Pandas DataFrames
- User-friendly interface powered by Streamlit
