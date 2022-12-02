import streamlit as st
from login import userlogin
from signup import usersignup

def main():
    st.title("welcome to team_name")
    st.subheader("please login")
    options=['userlogin','user signup']
    choice = st.sidebar.selectbox("menu", options)

    if choice==options[0]:
        userlogin()
   
    elif choice==options[1]:
        usersignup()
    else:
        st.subheader("about tasks:")

if __name__ == '__main__':
    main()

