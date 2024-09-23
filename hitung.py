import streamlit as st

x = st.number_input("Insert a number")
sx = st.text_input("satuan", "C")
st.write("The current number is ", x,' ',sx)
sy = st.text_input("Converted to", "C")

st.writer(x, ' ', sx, '=...', sy)
