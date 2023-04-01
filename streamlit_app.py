import streamlit as st
import pandas as pd
import plotly.express as px
import requests

# Set page configuration
st.set_page_config(
    page_title="Sample Streamlit App",
    page_icon=":memo:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title
st.title("Sample Streamlit App with Airdrop Data Visualization")

# Load data
url = "https://api.flipsidecrypto.com/api/v2/queries/5b6a2816-65cb-47a1-b2b9-39318a79889f/data/latest"
response = requests.get(url)
data = response.json()

# Create a DataFrame
df = pd.DataFrame(data)

# Display data as a table
st.header("Airdrop Data")
st.write(df)

# Visualize data
st.header("Airdrop Amount Distribution")
fig1 = px.pie(df, values="WALLETS", names="AIRDROP_AMOUNT", title="Number of Wallets per Airdrop Amount Range")
st.plotly_chart(fig1)

st.header("Airdrop Volume Distribution")
fig2 = px.pie(df, values="AIRDROP_VOLUME", names="AIRDROP_AMOUNT", title="Airdrop Volume per Airdrop Amount Range")
st.plotly_chart(fig2)
