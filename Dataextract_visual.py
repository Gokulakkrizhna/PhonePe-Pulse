import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go


def format_value(value):
    if value >= 10000000: 
        return f"{value/10000000:.2f} Cr"
    elif value >= 100000: 
        return f"{value/100000:.2f} L"
    else:
        return str(value)
    

def streamlit_home():
    tab1, tab2, tab3, tab4,tab19= st.tabs(["Home", "Data visualization", " Statistics Data","Transaction Insights","User Insights"])

    with tab1:
        st.header(':violet[PhonePe Pulse]', divider='rainbow')
        # if st.button("Go Digital"):
        option = st.selectbox('For which data do you like to see visualization?',("",'Transaction', 'User'))
        if option:
            option1 = st.selectbox('For which year do you like to see visualization?',("",'2018', '2019', '2020', '2021', '2022', '2023'))
            if option1:
                option2 = st.selectbox('For which Quater do you like to see visualization?',("",'Q1', 'Q2', 'Q3', 'Q4'))
                if option2:
                    st.success('Data has been fetched and it has been visualized', icon="✅")

    with tab2:
        option3 = st.selectbox('How do you like to visualize the data?',("","India","Global","State"))
        if option3 == "India":
            if option == "Transaction":
                    st.write('Below is the Geo india Data visualiztion of transaction data for the year {0} in the quater {1}'.format(option1, option2))
                    mycursor.execute("WITH gokul AS (SELECT * FROM agg_trans WHERE Y = '{0}') \
                        SELECT * FROM gokul WHERE Q = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index = [i for i in range(1,len(out)+1)])
                    df["density"] = np.log10(df["Amt"])
                    df['Total_Transaction_Amount'] = df.groupby('S')['Amt'].transform('sum')
                    df['Formatted_Transaction_Amount'] = df['Total_Transaction_Amount'].apply(format_value)
                    
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='S',
                        color='density',
                        color_continuous_scale='earth',
                        custom_data=[df["Formatted_Transaction_Amount"]],
                    )

                    fig.update_traces(hovertemplate='<b>%{location}</b><br>Transaction Amount: %{customdata[0]}')
                    fig.update_geos(fitbounds="locations", visible=False)

                    st.plotly_chart(fig, use_container_width=True)

                    with st.expander("Do you wish to see the raw data?"):
                        st.dataframe(df)

            else:
                st.write('Below is the Geo india Data visualiztion of user data for the year {0} in the quater {1}'.format(option1, option2))
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_usr WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Reg_users', 'App_opens'],index = [i for i in range(1,len(out)+1)])
                df["density"] = np.log10(df["Reg_users"])
                df['Total_user'] = df.groupby('State')['Reg_users'].transform('sum')
                
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='density',
                    color_continuous_scale='earth',
                    custom_data=[df["Total_user"]],
                )

                fig.update_traces(hovertemplate='<b>%{location}</b><br>Registered Users: %{customdata[0]}')
                fig.update_geos(fitbounds="locations", visible=False)

                st.plotly_chart(fig, use_container_width=True)

                with st.expander("Do you wish to see the raw data?"):
                    st.dataframe(df)

        elif option3 == "Global":
            if option == "Transaction":
                    st.write('Below is the Geo india Data visualiztion of transaction data for the year {0} in the quater {1}'.format(option1, option2))
                    mycursor.execute("WITH gokul AS (SELECT * FROM agg_trans WHERE Y = '{0}') \
                        SELECT * FROM gokul WHERE Q = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index = [i for i in range(1,len(out)+1)])
                    df["density"] = np.log10(df["Amt"])
                    df['Total_Transaction_Amount'] = df.groupby('S')['Amt'].transform('sum')
                    df['Formatted_Transaction_Amount'] = df['Total_Transaction_Amount'].apply(format_value)
                    
                    fig = px.choropleth(
                        df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='S',
                        color='density',
                        color_continuous_scale='earth',
                        custom_data=[df["Formatted_Transaction_Amount"]],
                    )

                    fig.update_traces(hovertemplate='<b>%{location}</b><br>Transaction Amount: %{customdata[0]}')
                    fig.update_geos(projection_type="orthographic", landcolor="white", oceancolor="MidnightBlue", showocean=True, lakecolor="LightBlue", visible=False)

                    st.plotly_chart(fig, use_container_width=True)

                    with st.expander("Do you wish to see the raw data?"):
                        st.dataframe(df)

            else:
                st.write('Below is the Geo india Data visualiztion of user data for the year {0} in the quater {1}'.format(option1, option2))
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_usr WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Reg_users', 'App_opens'],index = [i for i in range(1,len(out)+1)])
                df["density"] = np.log10(df["Reg_users"])
                df['Total_user'] = df.groupby('State')['Reg_users'].transform('sum')
                
                fig = px.choropleth(
                    df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='density',
                    color_continuous_scale='earth',
                    custom_data=[df["Total_user"]],
                )

                fig.update_traces(hovertemplate='<b>%{location}</b><br>Registered Users: %{customdata[0]}')
                fig.update_geos(projection_type="orthographic", landcolor="white", oceancolor="MidnightBlue", showocean=True, lakecolor="LightBlue", visible=False)

                st.plotly_chart(fig, use_container_width=True)

                with st.expander("Do you wish to see the raw data?"):
                    st.dataframe(df)
        
        elif option3 == "State":
            option4 = st.selectbox("Please select the state",('','Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'))
            if option == "Transaction":
                    st.write('Below is the Geo India State wise Data visualiztion of transaction data for the year {0} in the quater {1}'.format(option1, option2))
                    mycursor.execute("WITH gokul AS (SELECT * FROM agg_trans WHERE Y = '{0}') \
                        SELECT * FROM gokul WHERE Q = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index = [i for i in range(1,len(out)+1)])
                    df["density"] = np.log10(df["Amt"])
                    df['Total_Transaction_Amount'] = df.groupby('S')['Amt'].transform('sum')
                    df['Formatted_Transaction_Amount'] = df['Total_Transaction_Amount'].apply(format_value)
                    
                    state_df = df[df['S'] == option4]

                    # Plot choropleth map for Tamil Nadu
                    fig = px.choropleth(
                        state_df,
                        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        featureidkey='properties.ST_NM',
                        locations='S',
                        color='Amt',  # You can change this to the column you want to visualize
                        color_continuous_scale='Reds',
                        title='State wise Transaction Amount',
                        custom_data=[state_df["Formatted_Transaction_Amount"]]
                    )
                    fig.update_traces(hovertemplate='<b>%{location}</b><br>Registered Users: %{customdata[0]}')
                    fig.update_geos(fitbounds="locations", visible=False)

                    st.plotly_chart(fig, use_container_width=True)

                    with st.expander("Do you wish to see the raw data?"):
                        st.dataframe(state_df)

            elif option == "User":
                st.write('Below is the Geo india Data visualiztion of user data for the year {0} in the quater {1}'.format(option1, option2))
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_usr WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Reg_users', 'App_opens'],index = [i for i in range(1,len(out)+1)])
                df["density"] = np.log10(df["Reg_users"])
                df['Total_user'] = df.groupby('State')['Reg_users'].transform('sum')

                state_df = df[df['State'] == option4]

                # Plot choropleth map for Tamil Nadu
                fig = px.choropleth(
                    state_df,
                    geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                    featureidkey='properties.ST_NM',
                    locations='State',
                    color='Reg_users',  # You can change this to the column you want to visualize
                    color_continuous_scale='Reds',
                    title='State wise Reg User',
                )

                fig.update_geos(fitbounds="locations", visible=False)

                st.plotly_chart(fig, use_container_width=True)
                
                with st.expander("Do you wish to see the raw data?"):
                    st.dataframe(state_df)


    with tab3:
        if option3 != "State" and option3 != "":
            if option == "Transaction":
                st.header(":red[Transaction Stats]")
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_trans WHERE Y = '{0}') \
                    SELECT * FROM gokul WHERE Q = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index = [i for i in range(1,len(out)+1)])

                #total transaction count and total transaction amount
                st.subheader(":violet[General Transaction Stats]")
                Tot_trans_count = df["Cnt"].sum()
                Tot_trans_count_format = format_value(Tot_trans_count)
                Tot_trans_amt = df["Amt"].sum()
                Tot_trans_amt_format = format_value(Tot_trans_amt)
                st.write("All PhonePe transactions (UPI + Cards + Wallets): :blue[{0}({1})]".format(Tot_trans_count, Tot_trans_count_format))
                st.write("Total payment value: :blue[{0}({1})]".format(Tot_trans_amt,Tot_trans_amt_format))
                with st.expander("Do you wish to visualize the data?"):
                    random_x = [Tot_trans_count, Tot_trans_amt]
                    names = ['Total Transaction count', 'Total Transaction amount']
                    fig1 = px.pie(values=random_x, names=names)
                    st.plotly_chart(fig1, use_container_width=True)

                #transaction count based on transaction type
                st.subheader(":violet[Transaction by Categories]")
                a = df.groupby('TY')['Cnt'].sum().reset_index()
                a["Formatted_count"] = a["Cnt"].apply(format_value)
                st.dataframe(a)
                with st.expander("Do you wish to visualize the data?"):
                    fig2 = px.line(a, x='TY', y='Cnt', title='Line Plot', labels={'x': 'Transacion type', 'y': 'Transacion count'})
                    st.plotly_chart(fig2, use_container_width=True)

                tab5, tab6, tab7= st.tabs(["States", "District", " Postal Codes"])

                with tab5:
                    #top 10 states
                    b = df.groupby('S')['Cnt'].sum().reset_index()
                    b = b.sort_values(by=["Cnt"],ascending=False)
                    b = b.head(10)
                    b["Formatted_count"] = b["Cnt"].apply(format_value)
                    st.dataframe(b)
                    with st.expander("Do you wish to visualize the data?"):
                        fig3 = px.bar(b, x='S', y='Cnt', title='Top 10 States by Transaction Count')
                        st.plotly_chart(fig3, use_container_width=True)

                with tab6:
                    #top 10 district
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_trans_dist WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'District', 'trans_count', 'trans_amt'],index = [i for i in range(1,len(out)+1)])
                    c = df.groupby('District')['trans_count'].sum().reset_index()
                    c = c.sort_values(by=["trans_count"],ascending=False)
                    c = c.head(10)
                    c["Formatted_count"] = c["trans_count"].apply(format_value)
                    st.dataframe(c)
                    with st.expander("Do you wish to visualize the data?"):
                        fig4 = px.scatter(c, x='District', y='trans_count', title='Top 10 District by Transaction Count')
                        st.plotly_chart(fig4, use_container_width=True)

                with tab7:
                    #top 10 pincodes
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_trans_pin WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Pincodes', 'trans_count', 'trans_amt'],index = [i for i in range(1,len(out)+1)])
                    d = df.groupby('Pincodes')['trans_count'].sum().reset_index()
                    d = d.sort_values(by=["trans_count"],ascending=False)
                    d = d.head(10)
                    d["Formatted_count"] = d["trans_count"].apply(format_value)
                    st.dataframe(d)
                    with st.expander("Do you wish to visualize the data?"):
                        fig5 = px.line(d, x='Pincodes', y='trans_count', title='Top 10 Pincodes by Transaction Count', labels={'x': 'Transacion type', 'y': 'Transacion count'})
                        st.plotly_chart(fig5, use_container_width=True)

            else:
                st.header(":red[User Stats]")
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_usr WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Reg_users', 'App_opens'],index = [i for i in range(1,len(out)+1)])

                #total register user and total app open
                st.subheader(":violet[General User Stats]")
                Tot_reg_usr = df["Reg_users"].sum()
                Tot_reg_usr_format = format_value(Tot_reg_usr)
                Tot_app_open = df["App_opens"].sum()
                Tot_app_open_format = format_value(Tot_app_open)
                st.write("Registered PhonePe users till {0} {1}: :blue[{2}({3})]".format(option2,option1,Tot_reg_usr, Tot_reg_usr_format))
                if Tot_app_open != 0:
                    st.write("PhonePe app opens in {0} {1}: :blue[{2}({3})]".format(option2,option1,Tot_app_open, Tot_app_open_format))
                else:
                    st.write("PhonePe app opens in {0} {1}: :blue[Unavailable]".format(option2,option1))
                with st.expander("Do you wish to visualize the data?"):
                    random_x = [Tot_reg_usr, Tot_app_open]
                    names = ['Total Register User', 'Total App open']
                    fig = px.pie(values=random_x, names=names)
                    st.plotly_chart(fig, use_container_width=True)

                tab8, tab9, tab10= st.tabs(["States", "District", " Postal Codes"])

                with tab8:
                    a = df.groupby('State')['Reg_users'].sum().reset_index()
                    a = a.sort_values(by=["Reg_users"],ascending=False)
                    a = a.head(10)
                    a["Formatted_count"] = a["Reg_users"].apply(format_value)
                    st.dataframe(a)
                    with st.expander("Do you wish to visualize the data?"):
                        fig = px.bar(a, x='State', y='Reg_users', title='Top 10 States by Register User Count')
                        st.plotly_chart(fig, use_container_width=True)

                with tab9:
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_usr_dist WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'District', 'Reg_usr'],index = [i for i in range(1,len(out)+1)])
                    b = df.groupby('District')['Reg_usr'].sum().reset_index()
                    b = b.sort_values(by=["Reg_usr"],ascending=False)
                    b = b.head(10)
                    b["Formatted_count"] = b["Reg_usr"].apply(format_value)
                    st.dataframe(b)
                    with st.expander("Do you wish to visualize the data?"):
                        fig1 = px.scatter(b, x='District', y='Reg_usr', title='Top 10 District by Register User')
                        st.plotly_chart(fig1, use_container_width=True)

                with tab10:
                    #top 10 pincodes
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_usr_pin WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Pincodes', 'Reg_usr'],index = [i for i in range(1,len(out)+1)])
                    c = df.groupby('Pincodes')['Reg_usr'].sum().reset_index()
                    c = c.sort_values(by=["Reg_usr"],ascending=False)
                    c = c.head(10)
                    c["Formatted_count"] = c["Reg_usr"].apply(format_value)
                    st.dataframe(c)
                    with st.expander("Do you wish to visualize the data?"):
                        fig2 = px.line(c, x='Pincodes', y='Reg_usr', title='Top 10 Pincodes by Register User', labels={'x': 'Pincodes', 'y': 'Register User'})
                        st.plotly_chart(fig2, use_container_width=True)

        elif option3 == "State":
            if option == "Transaction":
                st.header(":red[Transaction Stats]")
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_trans WHERE Y = '{0}') \
                    SELECT * FROM gokul WHERE Q = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index = [i for i in range(1,len(out)+1)])
                df = df[df["S"] == option4]

                #total transaction count and total transaction amount
                st.subheader(":violet[General Transaction Stats]")
                Tot_trans_count = df["Cnt"].sum()
                Tot_trans_count_format = format_value(Tot_trans_count)
                Tot_trans_amt = df["Amt"].sum()
                Tot_trans_amt_format = format_value(Tot_trans_amt)
                st.write("All PhonePe transactions (UPI + Cards + Wallets): :blue[{0}({1})]".format(Tot_trans_count, Tot_trans_count_format))
                st.write("Total payment value: :blue[{0}({1})]".format(Tot_trans_amt,Tot_trans_amt_format))
                with st.expander("Do you wish to visualize the data?"):
                    random_x = [Tot_trans_count, Tot_trans_amt]
                    names = ['Total Transaction count', 'Total Transaction amount']
                    fig1 = px.pie(values=random_x, names=names)
                    st.plotly_chart(fig1, use_container_width=True)

                #transaction count based on transaction type
                st.subheader(":violet[Transaction by Categories]")
                a = df.groupby('TY')['Cnt'].sum().reset_index()
                a["Formatted_count"] = a["Cnt"].apply(format_value)
                st.dataframe(a)
                with st.expander("Do you wish to visualize the data?"):
                    fig2 = px.line(a, x='TY', y='Cnt', title='Line Plot', labels={'x': 'Transacion type', 'y': 'Transacion count'})
                    st.plotly_chart(fig2, use_container_width=True)

                tab5, tab6= st.tabs(["District", " Postal Codes"])

                with tab5:
                    #top 10 district
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_trans_dist WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'District', 'trans_count', 'trans_amt'],index = [i for i in range(1,len(out)+1)])
                    df = df[df["State"] == option4]
                    c = df.groupby('District')['trans_count'].sum().reset_index()
                    c = c.sort_values(by=["trans_count"],ascending=False)
                    c = c.head(10)
                    c["Formatted_count"] = c["trans_count"].apply(format_value)
                    st.dataframe(c)
                    with st.expander("Do you wish to visualize the data?"):
                        fig4 = px.scatter(c, x='District', y='trans_count', title='Top 10 District by Transaction Count')
                        st.plotly_chart(fig4, use_container_width=True)

                with tab6:
                    #top 10 pincodes
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_trans_pin WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Pincodes', 'trans_count', 'trans_amt'],index = [i for i in range(1,len(out)+1)])
                    df = df[df["State"] == option4]
                    d = df.groupby('Pincodes')['trans_count'].sum().reset_index()
                    d = d.sort_values(by=["trans_count"],ascending=False)
                    d = d.head(10)
                    d["Formatted_count"] = d["trans_count"].apply(format_value)
                    st.dataframe(d)
                    with st.expander("Do you wish to visualize the data?"):
                        fig5 = px.line(d, x='Pincodes', y='trans_count', title='Top 10 Pincodes by Transaction Count', labels={'x': 'Transacion type', 'y': 'Transacion count'})
                        st.plotly_chart(fig5, use_container_width=True)

            else:
                st.header(":red[User Stats]")
                mycursor.execute("WITH gokul AS (SELECT * FROM agg_usr WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                out=mycursor.fetchall()
                df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Reg_users', 'App_opens'],index = [i for i in range(1,len(out)+1)])
                df = df[df["State"] == option4]

                #total register user and total app open
                st.subheader(":violet[General User Stats]")
                Tot_reg_usr = df["Reg_users"].sum()
                Tot_reg_usr_format = format_value(Tot_reg_usr)
                Tot_app_open = df["App_opens"].sum()
                Tot_app_open_format = format_value(Tot_app_open)
                st.write("Registered PhonePe users till {0} {1}: :blue[{2}({3})]".format(option2,option1,Tot_reg_usr, Tot_reg_usr_format))
                if Tot_app_open != 0:
                    st.write("PhonePe app opens in {0} {1}: :blue[{2}({3})]".format(option2,option1,Tot_app_open, Tot_app_open_format))
                else:
                    st.write("PhonePe app opens in {0} {1}: :blue[Unavailable]".format(option2,option1))
                with st.expander("Do you wish to visualize the data?"):
                    random_x = [Tot_reg_usr, Tot_app_open]
                    names = ['Total Register User', 'Total App open']
                    fig = px.pie(values=random_x, names=names)
                    st.plotly_chart(fig, use_container_width=True)

                tab7, tab8= st.tabs(["District", " Postal Codes"])

                with tab7:
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_usr_dist WHERE Year = '{0}') \
                    SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'District', 'Reg_usr'],index = [i for i in range(1,len(out)+1)])
                    df = df[df["State"] == option4]
                    b = df.groupby('District')['Reg_usr'].sum().reset_index()
                    b = b.sort_values(by=["Reg_usr"],ascending=False)
                    b = b.head(10)
                    b["Formatted_count"] = b["Reg_usr"].apply(format_value)
                    st.dataframe(b)
                    with st.expander("Do you wish to visualize the data?"):
                        fig1 = px.scatter(b, x='District', y='Reg_usr', title='Top 10 District by Register User')
                        st.plotly_chart(fig1, use_container_width=True)

                with tab8:
                    #top 10 pincodes
                    mycursor.execute("WITH gokul AS (SELECT * FROM top_usr_pin WHERE Year = '{0}') \
                        SELECT * FROM gokul WHERE Quater = '{1}'".format(option1, option2))
                    out=mycursor.fetchall()
                    df = pd.DataFrame(out,columns=['State', 'Year', 'Quater', 'Pincodes', 'Reg_usr'],index = [i for i in range(1,len(out)+1)])
                    df = df[df["State"] == option4]
                    c = df.groupby('Pincodes')['Reg_usr'].sum().reset_index()
                    c = c.sort_values(by=["Reg_usr"],ascending=False)
                    c = c.head(10)
                    c["Formatted_count"] = c["Reg_usr"].apply(format_value)
                    st.dataframe(c)
                    with st.expander("Do you wish to visualize the data?"):
                        fig2 = px.line(c, x='Pincodes', y='Reg_usr', title='Top 10 Pincodes by Register User', labels={'x': 'Pincodes', 'y': 'Register User'})
                        st.plotly_chart(fig2, use_container_width=True)

    with tab4:
        #1 overall trends of count and transaction irrespective of their year
        st.subheader("Exploring the Trend: Transaction Count and Transaction Amount Over Time")
        mycursor.execute("select Y,sum(Cnt),sum(Amt) from agg_trans group by Y")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["Y","Cnt","Amt"],index=[i for i in range(1,len(out)+1)])
        fig = make_subplots(rows=1, cols=2)

        fig.add_trace(
            go.Scatter(x=df['Y'], y=df['Cnt']),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Y'], y=df['Amt']),
            row=1, col=2
        )

        fig.update_layout(height=600, width=800)
        st.plotly_chart(fig, use_container_width=True)

        #2 Quater wise analysis
        st.subheader("Exploring the Trend: Transaction Count and Transaction Amount Over Quater and Time")
        mycursor.execute("select Y,Q,sum(Cnt),sum(Amt) from agg_trans group by Y,Q")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["Y","Q","Cnt","Amt"],index=[i for i in range(1,len(out)+1)])
        
        fig = make_subplots(rows=1, cols=2)

        for i in range(len(df["Y"].unique())):
            fig.add_trace(
                px.line(df, x="Q", y="Cnt", color="Y").data[i],
                row=1, col=1
            )
            fig.add_trace(
                px.line(df, x="Q", y="Amt", color="Y").data[i],
                row=1, col=2
            )

        fig.update_layout(height=600, width=800)
        st.plotly_chart(fig, use_container_width=True)

        #3 Analyze transaction counts and amounts across different states
        st.subheader("Analyze Transaction counts and amounts across different States")
        tab11,tab12 = st.tabs(["Transaction Count","Transaction Amount"])
        mycursor.execute("select S,sum(Cnt),sum(Amt) from agg_trans group by S")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["S","Cnt","Amt"],index=[i for i in range(1,len(out)+1)])

        with tab11:
            df = df.sort_values(by="Cnt")
            fig = px.bar(df,x="S",y="Cnt")
            st.plotly_chart(fig, use_container_width=True)

        with tab12:
            df = df.sort_values(by="Amt")
            fig = px.bar(df,x="S",y="Amt")
            st.plotly_chart(fig, use_container_width=True)
        
        #4 Analyse the trends of transaction type with count and amount
        st.subheader("Analyse the trends of transaction type with count and amount")
        tab13,tab14 = st.tabs(["Transaction Count","Transaction Amount"])
        mycursor.execute("select * from agg_trans")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=['S', 'Y', 'Q', 'TY', 'Cnt', 'Amt'],index=[i for i in range(1,len(out)+1)])
        with tab13:
            fig = px.pie(df, values='Cnt', names='TY', title='Transaction Type Distribution')
            st.plotly_chart(fig, use_container_width=True)
        with tab14:
            fig = px.pie(df, values='Amt', names='TY', title='Transaction Type Distribution')
            st.plotly_chart(fig, use_container_width=True)

        #5 Analyse the trends of transaction type with count and amount for the particular year and quater
        st.subheader("Exploring Transaction Trends Across States: A Yearly and Quarterly Analysis by Transaction Type")
        mycursor.execute("select Y,S,Q,TY,sum(Cnt),sum(Amt) from agg_trans group by Y,S,Q,TY")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=['Y', 'S', 'Q', 'TY', 'Cnt', 'Amt'],index=[i for i in range(1,len(out)+1)])
        tab15,tab16 = st.tabs(["Transaction Count","Transaction Amount"])

        with tab15:
            fig = px.sunburst(df, path=["Y","Q","S","TY"], values='Cnt')
            st.plotly_chart(fig, use_container_width=True)
        
        with tab16:
            fig = px.sunburst(df, path=["Y","Q","S","TY"], values='Amt')
            st.plotly_chart(fig, use_container_width=True)

        #6 Analyse the trends with district with count and amount
        st.subheader("District-wise Analysis of Transaction Count and Transaction Amount")
        option5 = st.selectbox("Select the state",('','Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'))
        mycursor.execute("select State,  District, Tot_trans, Tot_amt from map_dist_trans where State = '{0}'".format(option5))
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["State","District","Tot_trans","Tot_amt"],index=[i for i in range(1,len(out)+1)])
        tab17,tab18 = st.tabs(["Transaction Count","Transaction Amount"])

        with tab17:
            df = df.sort_values(by="Tot_trans")
            fig = px.box(df, x="District", y="Tot_trans")
            st.plotly_chart(fig, use_container_width=True)

        with tab18:
            df = df.sort_values(by="Tot_amt")
            fig = px.box(df,x="District",y="Tot_amt")
            st.plotly_chart(fig, use_container_width=True)

    with tab19:
        #1 overall trends of Reg_users and App_opens irrespective of their year
        st.subheader("Exploring the Trend: Registered User and App Opens Over Time")
        mycursor.execute("select Year,sum(Reg_users),sum(App_opens) from agg_usr group by Year")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["Year","Reg_users","App_opens"],index=[i for i in range(1,len(out)+1)])
        fig = make_subplots(rows=1, cols=2)

        fig.add_trace(
            go.Scatter(x=df['Year'], y=df['Reg_users']),
            row=1, col=1
        )

        fig.add_trace(
            go.Scatter(x=df['Year'], y=df['App_opens']),
            row=1, col=2
        )

        fig.update_layout(height=600, width=800)
        st.plotly_chart(fig, use_container_width=True)

        #2 Quater wise analysis
        st.subheader("Exploring the Trend: Registered User and App Opens Over Quater and Time")
        mycursor.execute("select Year,Quater,sum(Reg_users),sum(App_opens) from agg_usr group by Year,Quater")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["Year","Quater","Reg_users","App_opens"],index=[i for i in range(1,len(out)+1)])
        
        fig = make_subplots(rows=1, cols=2)

        for i in range(len(df["Year"].unique())):
            fig.add_trace(
                px.line(df, x="Quater", y="Reg_users", color="Year").data[i],
                row=1, col=1
            )
            fig.add_trace(
                px.line(df, x="Quater", y="App_opens", color="Year").data[i],
                row=1, col=2
            )

        fig.update_layout(height=600, width=800)
        st.plotly_chart(fig, use_container_width=True)

        #3 Analyze Reg_users and App_opens across different states
        st.subheader("Analyze Registered User and App Opens across different States")
        tab20,tab21 = st.tabs(["Registerd User","App Opens"])
        mycursor.execute("select State,sum(Reg_users),sum(App_opens) from agg_usr group by State")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["State","Reg_users","App_opens"],index=[i for i in range(1,len(out)+1)])

        with tab20:
            df = df.sort_values(by="Reg_users")
            fig = px.bar(df,x="State",y="Reg_users")
            st.plotly_chart(fig, use_container_width=True)

        with tab21:
            df = df.sort_values(by="App_opens")
            fig = px.bar(df,x="State",y="App_opens")
            st.plotly_chart(fig, use_container_width=True)

        #4 Analyse the trends of transaction type with Reg_users and App_opens for the particular year, quater and state
        st.subheader("Exploring Trends Across States: A Yearly and Quarterly Analysis by Registered User and App Opens")
        mycursor.execute("select Year,State,Quater,sum(Reg_users),sum(App_opens) from agg_usr group by Year,State,Quater")
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=['Year', 'State', 'Quater', 'Reg_users', 'App_opens'],index=[i for i in range(1,len(out)+1)])
        tab22,tab23 = st.tabs(["Registerd User","App Opens"])

        with tab22:
            fig = px.sunburst(df, path=["Year","Quater","State"], values='Reg_users')
            st.plotly_chart(fig, use_container_width=True)
        
        with tab23:
            fig = px.sunburst(df, path=["Year","Quater","State"], values='App_opens')
            st.plotly_chart(fig, use_container_width=True)

        #6 Analyse the trends with district with count and amount
        st.subheader("District-wise Analysis of Registered User and App Opens")
        option6 = st.selectbox("Kindly select the state",('','Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh', 'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep', 'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh', 'Uttarakhand', 'West Bengal'))
        mycursor.execute("select State,  District, Reg_users, App_opens from map_dist_usr where State = '{0}'".format(option6))
        out=mycursor.fetchall()
        df = pd.DataFrame(out,columns=["State","District","Reg_users","App_opens"],index=[i for i in range(1,len(out)+1)])
        tab24,tab25 = st.tabs(["Registerd User","App Opens"])

        with tab24:
            df = df.sort_values(by="Reg_users")
            fig = px.box(df, x="District", y="Reg_users")
            st.plotly_chart(fig, use_container_width=True)

        with tab25:
            df = df.sort_values(by="App_opens")
            fig = px.box(df,x="District",y="App_opens")
            st.plotly_chart(fig, use_container_width=True)


mydb = mysql.connector.connect(
 host="localhost",
 user="root",
 password="",
 )
mycursor = mydb.cursor(buffered=True)

mycursor.execute("use Phonepe")

streamlit_home()