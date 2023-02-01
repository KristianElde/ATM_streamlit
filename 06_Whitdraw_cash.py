import streamlit as st
from pages.Modules.DB_func_streamlit import *
from streamlit_extras.switch_page_button import switch_page

def whitdraw_cash():
    if st.session_state.indexx == 'null':
        st.warning('You are not logged into an user. Please log in to a valid user in order to use this page.')
        if st.button('Return to main menu'):
            switch_page('main_menu')
    else:
        st.title("Elde's ATM")
        user_list = st.session_state.db
        active_user = user_list[st.session_state.indexx]
        st.subheader(f'Logged in to user: {active_user.username}')
        st.write('How much do you want to whitdraw?')
        whitdraw_amount = st.text_input('')
        if st.button('Whitdraw'):
            if int(whitdraw_amount) <= active_user.balance and int(whitdraw_amount) > 0:
                active_user.balance -= int(whitdraw_amount)
                st.write(f'You have succsessfully whitdrawn {whitdraw_amount}. You now have {active_user.balance}$ in your account.')
                st.session_state.db = user_list
            elif int(whitdraw_amount) > active_user.balance:
                st.write('Insuficcient funds on account. Try to whitdraw a lower amount.')
            else:
                st.write('Input was not accepted. Type in the amount you want to whitdraw. Please try again.')
        if st.button('Go back'):
            switch_page('user_menu')


whitdraw_cash()