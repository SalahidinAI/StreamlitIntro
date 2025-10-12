import streamlit as st

st.title('Анкета')

name = st.text_input('Name: ')
age = st.number_input('Age: ', min_value=10, max_value=80)
course = st.text_input('Course: ')
field = st.selectbox('Course: ', ['AI', 'Fullstack', 'DevOps'])

if st.button('Send'):
    st.success(name)
    st.success(age)
    st.success(course)
    st.success(field)

if st.button('Show in one line'):
    st.write(name, age, course, field)


# Just practice

# str
st.title('Book')
st.write('Book')
st.text('Book')

# inputs
st.number_input('Age: ', min_value=0, max_value=100, step=5)
st.text_input('Name: ', placeholder='Name please', key='u must set key if u used text_input more than once')

# selection
st.selectbox('Select:', ['apple', 'banana', 'pear', 'pineapple'])

# button
if st.button('Green'):
    st.success('The button is pressed successfully')
if st.button('Red'):
    st.error('The button is pressed successfully')
if st.button('Yellow'):
    st.warning('The button is pressed successfully')
if st.button('Info'):
    st.info('The button is pressed successfully')

