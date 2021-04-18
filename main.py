from controllers import loginPage
from controllers import signUpPage
import streamlit as st

PAGES = {
	"loginPage": loginPage,
	"signUpPage": signUpPage
}

st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()