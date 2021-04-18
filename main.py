from controllers import loginPage
from controllers import signUpPage
from controllers import groups
import streamlit as st

PAGES = {
	"loginPage": loginPage,
	"signUpPage": signUpPage,
	"groups": groups
}
st.sidebar.title('Navigation')
st.sidebar.button('what is up')
selection = st.sidebar.radio("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()




