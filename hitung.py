import streamlit as st

x = st.number_input("Insert a number")
st.write("The current number is ", x)

st.latex(r'''
  x^2 =
  ''')
