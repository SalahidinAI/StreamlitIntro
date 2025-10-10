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
