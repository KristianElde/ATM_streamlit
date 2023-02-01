import streamlit as st
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page

def deposit_money_page():
    if st.session_state.indexx == 'null':
        st.warning('You are not logged into an user. Please log in to a valid user in order to use this page.')
        if st.button('Return to main menu'):
            switch_page('main_menu')
    else:
        st.title("Elde's ATM")
        user_list = st.session_state.db
        active_user = user_list[st.session_state.indexx]
        st.subheader(f'Logged in to user: {active_user.username}')
        st.write('How much do you want to deposit?')
        deposit_amount = st.text_input('')
        if st.button('Deposit'):
            if int(deposit_amount) > 0:
                active_user.balance += int(deposit_amount)
                st.write(f'You have succsessfully deposited {deposit_amount}. You now have {active_user.balance}$ in your account.')
                st.session_state.db = user_list
            else:
                st.write('Input was not accepted. Type in the amount you want to whitdraw. Please try again.')
        if st.button('Go back'):
            switch_page('user_menu')


deposit_money_page()