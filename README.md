# customerChurn

## Project Description
This is a machine learning project and the goal is to develop a customer churn prediction model for a telecommunications company. We aim to identify factors that contribute to churn and build a predictive model to forecast which customers are likely to churn in the near future.

## Data Source: 
‘telco-customer-churn.csv’ - The Telco Customer Churn dataset is a publicly available dataset on IBM Sample Data Sets (https://community.ibm.com/community/user/businessanalytics/blogs/steven-macko/2019/07/11/telco-customer-churn-1113). That provides information on customers of a telecommunications company and whether they have churned or not. 

## Data Characteristics: 
The dataset consists of 7043 observations and 21 variables. The variables include both demographic and service-specific information about the customers, such as their gender, age, contract type, payment method, and usage patterns. The dataset contains both categorical and continuous variables. The categorical variables include binary, nominal, and ordinal data, while the continuous variables include ratio and interval data. The target variable is "Churn" which is a binary variable indicating whether the customer has churned or not. The other variables are potential predictors that can be used to build a predictive model for customer churn.

## Data Preparation:
In this stage, I cleaned and preprocessed the data to prepare it for analysis and modeling. This includes handling missing values, encoding categorical variables, scaling numerical variables, and handling outliers if necessary.

## Exploratory Data Analysis (EDA):
In this stage, we performed exploratory data analysis to gain insights into the data and identify patterns or relationships between variables.I also used various statistical and visualization techniques to examine the distribution of the variables, the correlation between the variables.

## Model Selection:
In this stage, I experimented with several classification models, including Logistic Regression, Decision Tree, Random Forest, and Gradient Boosting, and evaluated their performance using cross-validation and various performance metrics such as AUC, precision, recall, and F1 score.I selected Gradient boosting as the best performing model based on its performance on the test dataset.

## Model Deployment:
In this stage,I deployed the selected model in Streamlit Community Cloud.This is the link to my web app: https://tyqm42ijjjfmtawyhty73.streamlit.app/
