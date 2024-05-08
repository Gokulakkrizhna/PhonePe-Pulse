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
# Approach
```Data Collection```: Clone the PhonePePulse data from the GitHub repository to your local directory, ensuring seamless access. 
```Data Cleaning```: Refine pre-processing methods like Data handling is applied to the collected data.
```Store data in MySql```: The collected data is stored in a MySQL database. Employ the MySQL Connector package to establish a connection with the MySQL localhost server. 
```SQLAlchemy and PyMySQL```: These 2 will facilitate the creation of a temporary connection to the MySQL database, enabling bulk insertion of data.
```Setup the Streamlit app```: Streamlit is a user-friendly web development tool that simplifies the process of creating intuitive interfaces. With Streamlit, you can easily design a straightforward UI where users can input a channel ID and quickly access all relevant details in a simple manner.
```Data Analysis```: Using SQL queries, the retrieved data has been analyzed and visualized in Streamlit through Pandas DataFrame.
```Data Visualization```: The retrieved data has been visualized using Plotly to gain valuable insights from the datasets.

The provided code utilizes Python scripting along with various libraries to fetch data from the PhonePe Pulse GitHub repository. Data handling procedures are applied, and the processed data is stored in a MySQL database. Subsequently, the stored data is utilized for data visualization to gain valuable insights. Additionally, it incorporates a Streamlit web application to facilitate user interaction.

Here's a breakdown of what the code does:
- Importing all the neccessary libraries includes ```Streamlit``` which creates UI to interact with user and display the analysed data, ```Pandas``` which helps to display the analysed data in Streamlit web,```mysql-connector-python``` will create a connection between python and MySql server,```numpy``` which will help in mathematical conversion,```Plotly```  is employed to visualize the data and gain insights from it,```OS``` assists in reading data from the local directory,```JSON``` is used to load JSON files into Python,```pymysql sqlalchemy``` will create a temporary connection with MySql database for a bulk insertion.
```bash
import os
import pandas as pd
import json
import numpy as np
import mysql.connector
from sqlalchemy import create_engine
import streamlit as st
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
```
- ```Datacoll_dataclean``` file is responsible for fetching data from the local directory and performing necessary data cleaning operations. Once the data is cleaned, it will be stored in a MySQL database using SQLAlchemy.**Note: Replace your actual path in ```path```**
```bash
path = r"please provide the path"
```
- ```Dataextract_visual```  file is used to extract the data stored in MySQL and visualize it to derive valuable insights using Plotly.
- 
