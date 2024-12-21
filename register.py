import streamlit as st
st.title("registration form")
name=st.text_input("enter your name")
email=st.text_input("enter your email")
phone_number=st.text_input("enter your phone number")
gender=st.radio("select your gender",("Male","Female"))
if(gender=="Male"):
    st.success("MALE")
else:
    st.success("FEMALE")
branch=st.selectbox("select branch",["csm","cse","it","ds"])
st.write("you seleccted ",branch)
if st.button("submit"):
    st.success("successfully registered")
if st.checkbox("agree"):
    st.text("agreed to our terms")