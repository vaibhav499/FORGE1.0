import streamlit as st

def apply_theme():
    st.markdown(
        """
        <style>
        body {
            background-color: #0e0e0e;
            color: white;
        }
        .stButton button {
            background-color: #f5c518;
            color: black;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
