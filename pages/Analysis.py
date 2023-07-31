import pandas as pd
import warnings
import pickle
import time
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import PIL
from PIL import Image

warnings.filterwarnings(action='ignore')

df = pd.read_csv('telco-customer-churn.csv')

df.drop('customerID',axis = 1,inplace = True)

interface = st.container()

with interface:
    st.title('Analysis')
    
    st.subheader('Numerical Features')
    
    selected_column = st.selectbox('Select a feature', [col for col in df.columns if col in ['tenure','MonthlyCharges','TotalCharges']])
    
    fig = px.histogram(df, x=selected_column, nbins=40, title=f'Distribution of {selected_column}', labels={'x': selected_column, 'count': 'Frequency'})

    # Adding border to the bars
    fig.update_traces(marker_line_width=1, marker_line_color='black')

    # Setting the layout
    fig.update_layout(width=600, height=500,title_font = dict(size = 24))

    # Display the plot in Streamlit
    st.plotly_chart(fig)
    
    st.markdown('***')
    
    st.subheader('Categorical Features')
    

    selected_column = st.selectbox('Select a feature', [col for col in df.columns if col not in ['Churn','tenure','MonthlyCharges','TotalCharges']])
        

    plot_values, plot_type = st.columns(2)
    
    with plot_values:
        plot_values = st.radio("Show plot for:",options=['All', 'Churn', 'Not Churn'])
    

    with plot_type:
        plot_type = st.radio("Show plot as:",options=['Pie', 'Bar'])

    # Filter the DataFrame based on the selected plot values
    if plot_values == 'Churn':
        df_filtered = df[df.Churn == 'Yes']
    elif plot_values == 'Not Churn':
        df_filtered = df[df.Churn == 'No']
    else:
        df_filtered = df  # Show plot for all data

    # Create the plot based on the selected plot type
    if plot_type == 'Bar':
    # Calculate the percentage of each value in the selected column
        value = df_filtered[selected_column].value_counts(normalize=True) * 100

        fig = px.bar(x=value.index, y=value.values,text=value.values.round(2),color=value.index, height=400, width=350,color_discrete_sequence=['LightCoral','springgreen','lightblue','gold'])
        
        fig.update_layout(xaxis_title=selected_column, yaxis_title='Percentage',title=f'Bar Plot of {selected_column} for {plot_values}',font = dict(size = 25),title_font = dict(size = 24))
        
        fig.update_traces(marker_line_width=2, marker_line_color='black')

        st.plotly_chart(fig)

    else:
        fig = px.pie(df_filtered, names=selected_column, title=f'Pie Chart of {selected_column} for {plot_values}',
                     color_discrete_sequence=['darkorange', 'lightgreen'])
        
        fig.update_traces(marker_line_width=2, marker_line_color='black')
        
        fig.update_layout(width=500, height=400,title_font = dict(size = 24),font = dict(size = 25))
        st.plotly_chart(fig)

