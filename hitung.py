import streamlit as st

x = st.number_input("Insert a number")
sx = st.text_input("satuan", "C")
st.write("The current number is ", x,' ',sx)

st.latex(r'''
  K = C + 273.15
  ''') 

sy = st.text_input("Converted to", "C")
y = 0 
if (sx == 'C'):
  if (sy == 'C'):
    y = x
  elif (sy == 'K'):
    y = x+273.15
  elif (sy == 'F'):
    y = (x+32)*(5/9)
  else :
    pass 
  
st.write(x, ' ', sx, '=', y, sy)
