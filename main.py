from controllers import loginPage
from controllers import signUpPage
from controllers import groups
import streamlit as st

from Database import db_helper

import streamlit as st

def main():
	PAGES = {
		"loginPage": loginPage,
		"signUpPage": signUpPage,
		"groups": groups
	}

	#hive_db = db_helper.db()
	#hive_db.add_user("leonhsieh@yahoo.com", "100999shieh")

	st.sidebar.title('Navigation')
	selection = st.sidebar.radio("Go to", list(PAGES.keys()))
	page = PAGES[selection]
	page.app()

if __name__ == "__main__":
	main()

