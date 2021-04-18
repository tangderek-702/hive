import streamlit as st

def app():
	st.title("SIGN UP PAGE")
	st.write("hi my name is not leon")
	name = st.text_input("Enter a username")

	if(st.button('Submit')):
	    result = name.title()
	    st.success(result)