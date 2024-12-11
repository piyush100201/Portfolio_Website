import streamlit as st
import pandas

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

content2 = """
           Below you can find some of the apps I have built in Python. 
           Feel free to contact me. 
           Would really appreciate any feedback to improve on the apps.
           """

st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data.csv", sep = ";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        # st.link_button(label = "Source Code", url = row["url"])  -- link in form of button
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image(row["image"])
        st.write(f"[Source Code]({row['url']})")



