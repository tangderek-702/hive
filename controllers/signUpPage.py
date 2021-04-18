import streamlit as st

def app():
	st.title("SIGN UP PAGE")
	name = st.text_input("Enter a username")

	if(st.button('Submit')):
	    result = name.title() + "is valid"
	    st.success(result)

	email = st.text_input("Enter your email")
	if(st.button('Submit1')):
	    result = email.title() + "is valid"
	    st.success(result)

	password = st.text_input("Enter your password")
	if(st.button('Submit2')):
		result = password.title() + "is valid"
		st.success(result)
