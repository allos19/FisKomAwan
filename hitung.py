import streamlit as st

x = st.number_input("Insert a number")
sx = st.text_input("satuan", "C")
st.write("The current number is ", x,' ',sx)

\begin{multicols}{2}
st.latex(r'''
  K = C + 273.15
  ''') 
st.latex(r''
  F = \left(\frac{9}{5} \times C \right)
  '')  
 

sy = st.text_input("Converted to", "C")
y = 0 
if (sx == 'C'):
  if (sy == 'C'):
    y = x
  elif (sy == 'K'):
    y = x+273.15
  elif (sy == 'F'):
    y = ((9/5)*x)+32
  else :
    pass 
  
st.write(x, ' ', sx, '=', y, sy)
