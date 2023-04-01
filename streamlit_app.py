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
st.title("Sample Streamlit App with 3 Full-Width Tabs")

# Tabs
st.sidebar.title("Tabs")

with st.sidebar.container():
    tab1 = st.button("Tab 1", key="tab1")
with st.sidebar.container():
    tab2 = st.button("Tab 2", key="tab2")
with st.sidebar.container():
    tab3 = st.button("Tab 3", key="tab3")

# Load data
url = "https://api.flipsidecrypto.com/api/v2/queries/5b6a2816-65cb-47a1-b2b9-39318a79889f/data/latest"
response = requests.get(url)
data = response.json()

# Create a DataFrame
df = pd.DataFrame(data)

# Content
if tab1:
    st.header("Tab 1")

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

elif tab2:
    st.header("Tab 2")
    # Add your content for Tab 2 here
elif tab3:
    st.header("Tab 3")
    # Add your content for Tab 3 here
else:
    st.header("Select a tab from the sidebar.")
