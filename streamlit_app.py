import streamlit as st

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

# Content
if tab1:
    st.header("Tab 1da ad d as das dads ")
    # Add your content for Tab 1 here
elif tab2:
    st.header("Tab 2")
    # Add your content for Tab 2 here
elif tab3:
    st.header("Tab 3")
    # Add your content for Tab 3 here
else:
    st.header("Select a tab from the sidebar.")
