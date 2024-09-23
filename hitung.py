import streamlit as st

x = st.number_input("Insert a number")
sx = st.selectbox("Unit", ("C", "K", "F", "R"), key='sx')
st.write("The current number is ", x,' ',sx)

#col1, col2 = st.columns(2)
#with col1:
st.latex(r'''K = C + 273.15''') 
st.latex(r'''F = \left(\frac{9}{5} \times C \right)''')  
#with col2:
st.latex(r'''R = \left(\frac{4}{5} \times C \right)''') 
                                                                                                   
sy = st.selectbox("Converted to", ("C", "K", "F", "R"), key='sy')
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

if (sx == 'K'):
  if (sy == 'C'):
    y = x-273.15
  elif (sy == 'K'):
    y = x
  elif (sy == 'F'):
    y = (x-273.15)*(9/5)+32
  elif (sy == 'R'):
    y = (x-273.15)*(4/5)
  else :
    pass

if (sx == 'F'):
  if (sy == 'C'):
    y = (x-32)*((5/9)
  elif (sy == 'K'):
    y = (x-32)*(5/9)+273.15
  elif (sy == 'F'):
    y = x
  elif (sy == 'R'):
    y = (x-32)*(4/9)
  else :
    pass

if (sx == 'R'):
  if (sy == 'C'):
    y = x*(5/4)
  elif (sy == 'K'):
    y = x*(5/4)+273.15
  elif (sy == 'F'):
    y = x*(9/4)+32)
  elif (sy == 'R'):
    y = x
  else :
    pass
	 
st.write(x, ' ', sx, '=', y, sy)
