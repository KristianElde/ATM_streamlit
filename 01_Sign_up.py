import streamlit as st
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page


def sign_up_page():
    user_list = []
    read_db(user_list)
    st.title("Elde's ATM")
    st.subheader('Sign up')
    st.write('Lets get you signed up! Choose your prefered username and password.')
    username = st.text_input('Username:', placeholder='Username')
    password = st.text_input('Password:', placeholder='Password')
    if st.button('Confirm'):
        check_username = 0
        for i in user_list:
            if i.username == username:
                st.write('Username allready in use')
                check_username = 1
        if check_username == 0:
            new_user = user(username, password,0)
            user_list.append(new_user)
            write_db(user_list)
            st.write('User successfully created')
    if st.button('return'):
        switch_page('main_menu')



sign_up_page()