import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Sample Streamlit App",
    page_icon=":memo:",
    layout="centered",
)

# Title
st.title("Sample Streamlit App with 3 Tabs")

# Tabs
tab_selection = st.sidebar.selectbox("Choose a tab:", ("Tab 1", "Tab 2", "Tab 3"))

if tab_selection == "Tab 1":
    st.header("Tab 1")
    # Add your content for Tab 1 here
elif tab_selection == "Tab 2":
    st.header("Tab 2")
    # Add your content for Tab 2 here
else:  # Tab 3
    st.header("Tab 3")
    # Add your content for Tab 3 here
