import streamlit as st
from random import randint

with st.sidebar:
    st.header('Kyrgyz AI')
    option = st.radio('Options', ['Main', 'Palindrome', 'Calculator', 'Find the number'])


if option == 'Main':
    st.title('Welcome to Kyrgyz AI')

elif option == 'Palindrome':
    st.title('Palindrome checker')
    user_word = st.text_input('Type to check palindrome:', placeholder='write something')
    if st.button('Check'):
        if user_word == user_word[::-1]:
            st.success(f'{user_word} is palindrome')
        else:
            st.error(f'{user_word} is NOT palindrome')

elif option == 'Calculator':
    st.title('Calculator program')
    first_num = st.number_input('First number', step=1)
    second_num = st.number_input('Second number', step=1)
    symbol = st.selectbox('Choose operation', ['*', '/', '+', '-'])
    if st.button('Calculate'):
        if symbol == '*':
            st.success(f'Result: {first_num * second_num}')
        if symbol == '/':
            st.success(f'Result: {first_num / second_num}')
        if symbol == '+':
            st.success(f'Result: {first_num + second_num}')
        if symbol == '-':
            st.success(f'Result: {first_num - second_num}')

if option == 'Find the number':
    num_from = st.number_input('From:', step=1, key='first')
    num_to = st.number_input('To:', step=1, key='second')
    random_num = randint(num_from, num_to)
    for i in range(5):
        user = st.number_input('Your option:', step=1)
        if st.button('Check'):
            if user == random_num:
                st.success('Congratulations!')
                break
            elif user > random_num:
                st.info(f'Random number is less than {user}')
            elif user < random_num:
                st.info(f'Random number is greater than {user}')


    # while True:
    #     user = st.number_input('Your option:', step=1)
    #     if st.button('Check'):
    #         if user == random_num:
    #             st.success('Congratulations!')
    #             break
    #         elif user > random_num:
    #             st.info(f'Random number is less than {user}')
    #         elif user < random_num:
    #             st.info(f'Random number is greater than {user}')

# if 'random_num' not in st.session_state:
#     st.session_state.random_num = None
#
# if 'game_started' not in st.session_state:
#     st.session_state.game_started = False
#
# option = 'Find the number'
#
# if option == 'Find the number':
#     num_from = st.number_input('From:', step=1, key='first')
#     num_to = st.number_input('To:', step=1, key='second')
#
#     if st.button('Start Game'):
#         if num_from >= num_to:
#             st.error("⚠️ 'From' should be less than 'To'")
#         else:
#             st.session_state.random_num = randint(num_from, num_to)
#             st.session_state.game_started = True
#             st.success('Game started! Try to guess the number.')
#
#     if st.session_state.game_started:
#         user = st.number_input('Your guess:', step=1, key='guess')
#         if st.button('Check'):
#             random_num = st.session_state.random_num
#             if user == random_num:
#                 st.success('🎉 Congratulations! You guessed the number!')
#                 st.session_state.game_started = False
#             elif user > random_num:
#                 st.info('🔽 Random number is less than your guess.')
#             else:
#                 st.info('🔼 Random number is greater than your guess.')

# else:
#     st.info('This page is not realized yet')

