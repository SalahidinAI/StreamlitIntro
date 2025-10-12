import  streamlit as st
import random

st.title('WELCOME')

with st.sidebar:
    st.header('MENU')
    v = st.radio('Choose', ['palindrom', 'calculator', 'game'])


if v == 'palindrom':
    st.title('Check palindrome')
    word = st.text_input('Type word:')

if st.button('Check'):
    if word == '':
        st.warning('Type word!')
    elif word == word[::-1]:
         st.success(f'{word} is palindrome!')
    else:
         st.error(f'{word} — is NOT palindrome!')



elif v == 'calculator':
    st.title('Simple calculator ')


    num1 = st.number_input('Type first number:')
    num2 = st.number_input('Type second number:')

    operation = st.selectbox('Choose operation:', ['+', '-', '*', '/'])
    if st.button('Calculate'):
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                st.error('It is impossible to divide by zero!')
            else:
                result = num1 / num2
        else:
            result = None

        if operation != '/' or num2 != 0:
            st.info(f'Result: {num1} {operation} {num2} = {result}')




elif v == 'game':
    st.title('Guess the number ')


    number_one = st.number_input('Lowest number:', value=1, step=1)
    number_two = st.number_input('Highest number:', value=10, step=1)


    if 'secret_number' not in st.session_state:
        st.session_state.secret_number = None
    if 'count' not in st.session_state:
        st.session_state.count = 0


    if st.button('Start the ga e'):
        st.session_state.secret_number = random.randint(number_one, number_two)
        st.session_state.count = 0
        st.success(f'The game is started!')


    if st.session_state.secret_number:
        number = st.number_input(f'Type any number between {int(number_one)} and {int(number_two)}:', step=1)
        if st.button('Check'):
            st.session_state.count += 1
            if number > st.session_state.secret_number:
                st.warning('This number is greater')
            elif number < st.session_state.secret_number:
                st.info('This number is less')
            else:
                st.success(f'Congratulations {st.session_state.secret_number} you found for {st.session_state.count} attempts!')

                st.session_state.secret_number = None