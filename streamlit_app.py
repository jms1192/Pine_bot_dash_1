import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Sample Streamlit App",
    page_icon=":memo:",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Title
st.title("Sample Streamlit App with 3 Tabs")

# Tabs
st.sidebar.title("Tabs")
tab1 = st.sidebar.button("Tab 1")
tab2 = st.sidebar.button("Tab 2")
tab3 = st.sidebar.button("Tab 3")

# Content
if tab1:
    st.header("Tab 1")
    # Add your content for Tab 1 here
elif tab2:
    st.header("Tab 2")
    # Add your content for Tab 2 here
elif tab3:
    st.header("Tab 3")
    # Add your content for Tab 3 here
else:
    st.header("Select a tab from the sidebar.")
