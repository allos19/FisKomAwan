import streamlit as st

x = st.number_input("Insert a number")
sx = st.text_input("satuan", "C")
st.write("The current number is ", x,' ',sx)

col1, col2 = st.columns(2)

with col1:
  st.latex(r'''K = C + 273.15''') 
  st.latex(r'''F = \left(\frac{9}{5} \times C \right)''')  

with col2:
  st.latex(r'''R = \left(\frac{4}{5} \times C \right)''') 
                                                                                                   
 

sy = st.text_input("Converted to", "C")
y = 0 
if (sx == 'C'):
  if (sy == 'C'):
    y = x
  elif (sy == 'K'):
    y = x+273.15
  elif (sy == 'F'):
    y = ((9/5)*x)+32
  elif (sy == 'R'):
    y = (4/5)*x
  else :
    pass 
  
st.write(x, ' ', sx, '=', y, sy)
