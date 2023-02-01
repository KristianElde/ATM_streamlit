import streamlit as st
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page

def log_in_page():
    user_list = []
    read_db(user_list)
    st.title("Elde's ATM")
    st.subheader('Log in')
    username = st.text_input('Username:', placeholder='Username')
    password = st.text_input('Password:', placeholder='Password')
    valid_user = 'n'
    if st.button('Confirm'):
        for i in range(len(user_list)):
            if username == user_list[i].username:
                if password == user_list[i].password:
                    st.session_state.indexx = i
                    st.session_state.db = user_list
                    switch_page('user_menu')
                else:
                    st.write('Wrong password')
                    valid_user = 'y'
        if valid_user == 'n':
                st.write('This user does not exist')
                

log_in_page()