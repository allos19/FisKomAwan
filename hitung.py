import streamlit as st

x = st.number_input(
        "Insert a number", value=None, placeholder='Tuliskan angka...")
st.write("The current number is ", x)

st.latex(r'''
  y = a x^2 + b x + c
  ''')
