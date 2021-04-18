import streamlit as st
from controllers import groups 

def app():
	st.title("LOGIN PAGE")
	st.write("hi my name is leon")
	if st.button('do not press'):
		groups.app()
	else:
		st.write('good job')