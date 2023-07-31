import pandas as pd
import warnings
import pickle
import time
import streamlit as st
import plotly.graph_objects as go
import PIL
from PIL import Image

df = pd.read_csv('telco-customer-churn.csv')

interface = st.container()

with interface:

    st.title('About Dataset')

    st.subheader('The dataset includes information about:')

    st.markdown("<p style='font-size: 20px;'>1. Customers who left within the last month – Churn column (Target).</p>",unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>2. Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies.</p>",unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>3. Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges.</p>",unsafe_allow_html=True)
    st.markdown("<p style='font-size: 20px;'>4. Demographic info about customers – gender, age range, and if they have partners and dependents.</p>",unsafe_allow_html=True)
   
    st.info(f'The dataset consist of {df.shape[0]} rows by {df.shape[1]} columns')
    st.info('Most of the features are categorical except for 3 columns (tenure , MonthlyCharges , TotalCharges)')
    
    show_data = st.checkbox("Show Data")
 
    if show_data:
        st.write(df)

    st.markdown('***')
    
    st.subheader('Churn distribution')
    
    fig = go.Figure()

    fig.add_trace(go.Pie(labels=['No Churn', 'Churn'], values=df['Churn'].value_counts(), name='Churn',
                     marker=dict(colors=['gold', 'mediumturquoise'], line=dict(color='#000', width=2))))

    fig.update_traces(hoverinfo="label+percent", textfont_size=16)

    # Update the layout of the plot
    fig.update_layout(height=450)

    # Show the plot in Streamlit app using st.plotly_chart
    st.plotly_chart(fig)
    
    st.markdown('***')
    
    st.subheader('Distributions by Churn')
    
    selected_column = st.selectbox("Select a feature", [col for col in df.columns if col not in               ['customerID','MonthlyCharges','TotalCharges','Churn']])
    
    data_grouped = df.groupby([selected_column, 'Churn']).size().unstack().reset_index()

    # Create the Plotly figure
    fig = go.Figure()
    fig.add_trace(go.Bar(x=data_grouped[selected_column], y=data_grouped['No'], name='Not Churned', marker_color='tomato'))
    fig.add_trace(go.Bar(x=data_grouped[selected_column], y=data_grouped['Yes'], name='Churned', marker_color='aquamarine'))

    fig.update_traces(marker_line=dict(color='#000', width=2), textfont_size=16)

    fig.update_layout(title=f'<b>{selected_column} Distribution by Churn</b>', xaxis_title=selected_column, yaxis_title='Count',
                      barmode='group', showlegend=True, height=400, width=700,title_font = dict(size = 24))

    # Show the plot in Streamlit app using st.plotly_chart
    st.plotly_chart(fig)

    
