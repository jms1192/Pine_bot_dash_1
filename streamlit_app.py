import streamlit as st
import pandas as pd
import requests

# Set page configuration
st.set_page_config(
    page_title="Sample Streamlit App",
    page_icon=":memo:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title
st.title("Sample Streamlit App")

# Load data
url = "https://api.flipsidecrypto.com/api/v2/queries/16065efe-6ac5-4678-8cf9-837b287cdf1f/data/latest"
response = requests.get(url)
data = response.json()

# Create a DataFrame
df = pd.DataFrame(data)

# Display data
st.write(df)
