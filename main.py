import streamlit as st

st.set_page_config(layout = "wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/piyush.jpg")

with col2:
    st.title("Piyush Jain")
    content = """
              Hello everyone, I am a python developer. 
              I created this portfolio website to showcase my python projects.
              """
    st.info(content)



