import streamlit as st
from function import user_signup_check,user_signup




def usersignup():

    st.header("sign up page")
    user_id = st.text_input("user_id:",'enter id')
    password = st.text_input("password:",type='password')
    if st.button('signup'):
        if len(user_id) <4:
            st.error("charecter of usere idshould be more than 3")
        elif len(password) <7:
            st.error("password length should be more than 6")
        else:
            if user_signup_check(user_id):
                st.error("credientials alredy exists use different ")

            else:
                user_signup(user_id,password)
                st.success("signed up successfull please log in ")

    return