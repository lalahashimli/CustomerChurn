import streamlit as st
import sklearn
import pandas as pd
import warnings
import pickle
import time
import PIL
from PIL import Image


warnings.filterwarnings(action='ignore')

# Load the DataFrame
df = pd.read_csv('telco-customer-churn.csv')


# Load the image
churn_image = Image.open('Churn.webp')

interface = st.container()

with interface:

    # Create the Streamlit app
    st.title('Telco Customer Churn')

    st.image(churn_image, width= 300,use_column_width = True)

    st.subheader('Project Description')

    st.markdown("<p style='font-size: 20px;'>This is a machine learning project and the goal is to develop a customer churn prediction model for a telecommunications company. We aim to identify factors that contribute to churn and build a predictive model to forecast which customers are likely to churn in the near future.</p>",unsafe_allow_html = True)

    st.markdown('***')

    st.subheader('Key Insights')


    st.success("- Gender has no effect on Churn Rate")
    st.success("- Senior citizens have a higher probability of churn than younger citizens")
    st.success("- Majority of customers who don't have partners churn")
    st.success("- Customers without any dependents are more likely to churn than customers with a dependent")
    st.success("- Customers who are using fiber optic service tend to churn")
    st.success("- Customers with month-month contract are likely to churn")
    st.success("- Majority of customers who left the company were having Electronic Check as Payment Method")
    st.success("- Customers using the rest of the services have low churn rates compared to customers who don't")
    st.success("- Half of the customers who use PaperlessBilling left the company")
    st.success("- Majority of the customers who are with the company for a long time are not leaving")

    
