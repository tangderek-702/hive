import streamlit as st
from controllers import groups 

def app():
	st.title("LOGIN PAGE")
	name = st.text_input("Enter your username")

	if(st.button('Submit')):
	    result = name.title() + "is valid"
	    st.success(result)

	password = st.text_input("Enter your password")
	if(st.button('Submit2')):
		result = password.title() + "is valid"
		st.success(result)