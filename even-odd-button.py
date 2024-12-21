import streamlit as st
st.title("This is a simple app")
st.header("this is heading")
st.subheader("this is sub-header")
st.success("success msg")
num1=st.number_input("Enter number",min_value=1,step=1)
if st.button("EVEN/ODD"):
   if num1%2==0:
       st.success("Even number")
   else:
       st.error("Odd number")

