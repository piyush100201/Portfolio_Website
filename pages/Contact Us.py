import streamlit as st
import send_email

st.title("Contact Me")

with st.form(key = "email_form"):
    user_email = st.text_input(label = "Your email address")
    user_message = st.text_area(label = "Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{user_message}
"""
    button = st.form_submit_button()
    if button:
        send_email.send_email(message)
        st.info("Your email was sent successfully")


