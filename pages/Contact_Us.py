import streamlit as st
import pandas as pd
from send_email import send_email

df = pd.read_csv("topics.csv")
topicos = [top for top in df["topic"]]

with st.form(key="Formulario_email"):
    user_email = st.text_input("Your Email Address:")
    user_subject = st.selectbox(label="What topic do you want to discuss?",
                                options=topicos)
    raw_message = st.text_area("Text:")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
topic {user_subject}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your message was sent sucessfully!")
