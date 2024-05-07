import os
import pandas as pd
import json
import numpy as np
import mysql.connector
from sqlalchemy import create_engine



def data_collection():
    path = r"please provide the path"
    Agg_state_list=os.listdir(path)
    
    a = {'S':[], 'Y':[],'Q':[],'TY':[], 'Cnt':[], 'Amt':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                for l in range(len(data["data"]["transactionData"])):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["transactionData"][l]["name"]
                    data2 = data["data"]["transactionData"][l]["paymentInstruments"][0]["count"]
                    data3 = data["data"]["transactionData"][l]["paymentInstruments"][0]["amount"]
                    a["S"].append(S)
                    a["Y"].append(Y)
                    a["Q"].append(Q)
                    a["TY"].append(data1)
                    a["Cnt"].append(data2)
                    a["Amt"].append(data3)
    
    df = pd.DataFrame(a)

    path = r"please provide the path"
    Agg_state_list=os.listdir(path)

    a = {'State':[], 'Year':[],'Quater':[],'Reg_users':[], 'App_opens':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                S = i
                Y = j
                Q = "Q{0}".format(k.strip(".json"))
                data1 = data["data"]["aggregated"]["registeredUsers"]
                data2 = data["data"]["aggregated"]["appOpens"]
                a["State"].append(S)
                a["Year"].append(Y)
                a["Quater"].append(Q)
                a["Reg_users"].append(data1)
                a["App_opens"].append(data2)
    
    df1 = pd.DataFrame(a)

    path = r"please provide the path"
    Agg_state_list=os.listdir(path)

    a = {'State':[], 'Year':[],'Quater':[],'District':[], 'Tot_trans':[], 'Tot_amt':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                S = i
                Y = j
                Q = "Q{0}".format(k.strip(".json"))
                for l in range(len(data["data"]["hoverDataList"])):
                    data1 = data["data"]["hoverDataList"][l]["name"]
                    data2 = data["data"]["hoverDataList"][l]["metric"][0]["count"]
                    data3 = data["data"]["hoverDataList"][l]["metric"][0]["amount"]
                    a["State"].append(S)
                    a["Year"].append(Y)
                    a["Quater"].append(Q)
                    a["District"].append(data1)
                    a["Tot_trans"].append(data2)
                    a["Tot_amt"].append(data3)

    df2 = pd.DataFrame(a)

    path = r"please provide the path"
    Agg_state_list=os.listdir(path)

    a = {'State':[], 'Year':[],'Quater':[],'District': [], 'Reg_users':[], 'App_opens':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                for l in list(data["data"]["hoverData"].keys()):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["hoverData"][l]["registeredUsers"]
                    data2 = data["data"]["hoverData"][l]["appOpens"]
                    a["State"].append(S)
                    a["Year"].append(Y)
                    a["Quater"].append(Q)
                    a["District"].append(l)
                    a["Reg_users"].append(data1)
                    a["App_opens"].append(data2)

    df3 = pd.DataFrame(a)

    path = r"please provide the path"
    Agg_state_list=os.listdir(path)

    a = {'State':[], 'Year':[],'Quater':[],'District': [], 'trans_count':[], 'trans_amt':[]}
    b = {'State':[], 'Year':[],'Quater':[],'Pincodes': [], 'trans_count':[], 'trans_amt':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                for l in range(len(data["data"]["districts"])):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["districts"][l]["entityName"]
                    data2 = data["data"]["districts"][l]["metric"]["count"]
                    data3 = data["data"]["districts"][l]["metric"]["amount"]
                    a["State"].append(S)
                    a["Year"].append(Y)
                    a["Quater"].append(Q)
                    a["District"].append(data1)
                    a["trans_count"].append(data2)
                    a["trans_amt"].append(data3)
                for l in range(len(data["data"]["pincodes"])):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["pincodes"][l]["entityName"]
                    data2 = data["data"]["pincodes"][l]["metric"]["count"]
                    data3 = data["data"]["pincodes"][l]["metric"]["amount"]
                    b["State"].append(S)
                    b["Year"].append(Y)
                    b["Quater"].append(Q)
                    b["Pincodes"].append(data1)
                    b["trans_count"].append(data2)
                    b["trans_amt"].append(data3)

    df4 = pd.DataFrame(a)
    df5 = pd.DataFrame(b)

    path = r"please provide the path"
    Agg_state_list=os.listdir(path)

    a = {'State':[], 'Year':[],'Quater':[],'District': [], 'Reg_usr':[]}
    b = {'State':[], 'Year':[],'Quater':[],'Pincodes': [], 'Reg_usr':[]}

    for i in Agg_state_list:
        path1 = "{0}/{1}".format(path,i)
        Agg_state_list_year = os.listdir(path1)
        for j in Agg_state_list_year:
            path2 = "{0}/{1}".format(path1,j)
            Agg_state_list_year_Quat = os.listdir(path2)
            for k in Agg_state_list_year_Quat:
                path3 = "{0}/{1}".format(path2,k)
                data = open(path3,"r")
                data = json.load(data)
                for l in range(len(data["data"]["districts"])):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["districts"][l]["name"]
                    data2 = data["data"]["districts"][l]["registeredUsers"]
                    a["State"].append(S)
                    a["Year"].append(Y)
                    a["Quater"].append(Q)
                    a["District"].append(data1)
                    a["Reg_usr"].append(data2)
                for l in range(len(data["data"]["pincodes"])):
                    S = i
                    Y = j
                    Q = "Q{0}".format(k.strip(".json"))
                    data1 = data["data"]["pincodes"][l]["name"]
                    data2 = data["data"]["pincodes"][l]["registeredUsers"]
                    b["State"].append(S)
                    b["Year"].append(Y)
                    b["Quater"].append(Q)
                    b["Pincodes"].append(data1)
                    b["Reg_usr"].append(data2)

    df6 = pd.DataFrame(a)
    df7 = pd.DataFrame(b)

    return df,df1,df2,df3,df4,df5,df6,df7
    

def data_cleaning(df,df1,df2,df3,df4,df5,df6,df7):
    state_dict = {
        'andaman-&-nicobar-islands': "Andaman & Nicobar",
        'andhra-pradesh': "Andhra Pradesh",
        'arunachal-pradesh': "Arunachal Pradesh",
        'assam': "Assam",
        'bihar': "Bihar",
        'chandigarh': "Chandigarh",
        'chhattisgarh': "Chhattisgarh",
        'dadra-&-nagar-haveli-&-daman-&-diu': "Dadra and Nagar Haveli and Daman and Diu",
        'delhi': "Delhi",
        'goa': "Goa",
        'gujarat': "Gujarat",
        'haryana': "Haryana",
        'himachal-pradesh': "Himachal Pradesh",
        'jammu-&-kashmir': "Jammu & Kashmir",
        'jharkhand': "Jharkhand",
        'karnataka': "Karnataka",
        'kerala': "Kerala",
        'ladakh': "Ladakh",
        'lakshadweep': "Lakshadweep",
        'madhya-pradesh': "Madhya Pradesh",
        'maharashtra': "Maharashtra",
        'manipur': "Manipur",
        'meghalaya': "Meghalaya",
        'mizoram': "Mizoram",
        'nagaland': "Nagaland",
        'odisha': "Odisha",
        'puducherry': "Puducherry",
        'punjab': "Punjab",
        'rajasthan': "Rajasthan",
        'sikkim': "Sikkim",
        'tamil-nadu': "Tamil Nadu",
        'telangana': "Telangana",
        'tripura': "Tripura",
        'uttar-pradesh': "Uttar Pradesh",
        'uttarakhand': "Uttarakhand",
        'west-bengal': "West Bengal"
    }
    df["S"] = df["S"].replace(state_dict)

    df1["State"] = df1["State"].replace(state_dict)

    df2["State"] = df2["State"].replace(state_dict)
    df2["District"] = df2["District"].str.replace("district","")
    df2["District"] = df2["District"].str.title()

    df3["State"] = df3["State"].replace(state_dict)
    df3["District"] = df3["District"].str.replace("district","")
    df3["District"] = df3["District"].str.title()

    df4["State"] = df4["State"].replace(state_dict)
    df4["District"] = df4["District"].str.title()

    df5["State"] = df5["State"].replace(state_dict)

    df6["State"] = df6["State"].replace(state_dict)
    df6["District"] = df6["District"].str.title()

    df7["State"] = df7["State"].replace(state_dict)

    return df,df1,df2,df3,df4,df5,df6,df7


def sql_db_val_insert(a,b):
    username = 'root'
    password = ''
    host = 'localhost'
    database = 'Phonepe'

    engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}/{database}')

    if b==1:
        a.to_sql(name='agg_trans', con=engine, if_exists='append', index=False)
    elif b==2:
        a.to_sql(name='agg_usr', con=engine, if_exists='append', index=False)
    elif b==3:
        a.to_sql(name='map_dist_trans', con=engine, if_exists='append', index=False)
    elif b==4:
        a.to_sql(name='map_dist_usr', con=engine, if_exists='append', index=False)
    elif b==5:
        a.to_sql(name='top_trans_dist', con=engine, if_exists='append', index=False)
    elif b==6:
        a.to_sql(name='top_trans_pin', con=engine, if_exists='append', index=False)
    elif b==7:
        a.to_sql(name='top_usr_dist', con=engine, if_exists='append', index=False)
    else:
        a.to_sql(name='top_usr_pin', con=engine, if_exists='append', index=False)

    engine.dispose()


a,b,c,d,e,f,g,h = data_collection()
a,b,c,d,e,f,g,h = data_cleaning(a,b,c,d,e,f,g,h)

mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 )
mycursor = mydb.cursor(buffered=True)

mycursor.execute("create database if not exists Phonepe")
mycursor.execute("use Phonepe")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_trans (
        S VARCHAR(255),
        Y VARCHAR(255),
        Q VARCHAR(255),
        TY VARCHAR(255),
        Cnt FLOAT,
        Amt FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS agg_usr (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        Reg_users FLOAT,
        App_opens FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS map_dist_trans (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        District VARCHAR(255),
        Tot_trans FLOAT,
        Tot_amt FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS map_dist_usr (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        District VARCHAR(255),
        Reg_users FLOAT,
        App_opens FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS top_trans_dist (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        District VARCHAR(255),
        trans_count FLOAT,
        trans_amt FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS top_trans_pin (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        Pincodes VARCHAR(255),
        trans_count FLOAT,
        trans_amt FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS top_usr_dist (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        District VARCHAR(255),
        Reg_usr FLOAT
    )
""")
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS top_usr_pin (
        State VARCHAR(255),
        Year VARCHAR(255),
        Quater VARCHAR(255),
        Pincodes VARCHAR(255),
        Reg_usr FLOAT
    )
""")

j = 1
for i in [a,b,c,d,e,f,g,h]:
    sql_db_val_insert(i,j)
    j += 1
