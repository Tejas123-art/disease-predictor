import streamlit as st
from function import user_login_check
from disease_predictor import mainfun


def userlogin():

    st.subheader('user login page')
    user_id = st.text_input("user_id:",'enter_id')
    password = st.text_input("password:",type='password')
    if st.button("login"):
        if user_login_check(user_id, password):
            mainfun()
        else:
            st.error("invalid credentials if not signed signup")