import streamlit as st
import csv
#from Elde_ATM import *
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page


def main_menu_page():
    st.session_state.indexx = 'null'
    st.title("Elde's ATM")
    st.subheader('What do you want to do?')
    if st.button('Sign up'):
        switch_page('sign_up')
    if st.button('Log in'):
        switch_page('log in')
    st.button('Exit and turn off ATM')


main_menu_page()