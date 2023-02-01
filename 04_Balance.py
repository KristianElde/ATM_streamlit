import streamlit as st
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page

def balance_page():
    if st.session_state.indexx == 'null':
        st.warning('You are not logged into an user. Please log in to a valid user in order to use this page.')
        if st.button('Return to main menu'):
            switch_page('main_menu')
    else:
        st.title("Elde's ATM")
        user_list = st.session_state.db
        active_user = user_list[st.session_state.indexx]
        st.subheader(f'Logged in to user: {active_user.username}')
        st.write('Your balance:')
        st.info(f'**{active_user.balance}$**')
        if st.button('Go back'):
            switch_page('user_menu')


balance_page()