import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

df = pd.read_csv('data.csv')

st.header("The Best Company")

st.write("    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")

st.subheader("Our Team")

col1, col2, col3 = st.columns(3)

for index, row in df.iterrows():
    if index % 3 == 0:
        with col1:
            st.subheader(
                (f"{row['first name']} {row['last name']}").capitalize())
            st.write((f"{row['role']}").capitalize())
            st.image("images/" + f"{row['image']}")
    elif index % 3 == 1:
        with col2:
            st.subheader(
                (f"{row['first name']} {row['last name']}").capitalize())
            st.write((f"{row['role']}").capitalize())
            st.image("images/" + f"{row['image']}")
    else:
        with col3:
            st.subheader(
                (f"{row['first name']} {row['last name']}").capitalize())
            st.write((f"{row['role']}").capitalize())
            st.image("images/" + f"{row['image']}")
