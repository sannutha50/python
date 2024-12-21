import streamlit as st
salary=st.number_input("enter the salary:",min_value=1,step=1)
if(salary<10000):
      hra=(67/100)*salary
      da=(73/100)*salary
elif(salary<20000):
      hra=(69/100)*salary
      da=(76/100)*salary
else:
  hra=(73/100)*salary
  da=(89/100)*salary
gross=hra+da+salary
st.write("The gross salary is: ",gross)