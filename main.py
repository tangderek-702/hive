from controllers import loginPage
from controllers import signUpPage
from controllers import groups
import streamlit as st
import SessionState



from Database import db_helper

import streamlit as st

def main():
	st.markdown(
	    """
	    <style>
	    .reportview-container .main{
	    	max-width: {max_width}px;
	        background: url("https://i.imgur.com/nFyJFSO.png")
	    }
	    </style>
	    """,
	    unsafe_allow_html=True
	)
	st.sidebar.title('Navigation')

	sesh = SessionState.get(curr_page = 0)
	PAGES = {
		0: loginPage,
		1: signUpPage,
		2: groups
	}

	if st.sidebar.button('Login:'):
		sesh.curr_page = 0
	if st.sidebar.button('Sign Up:'):
		sesh.curr_page = 1
	if st.sidebar.button('Groups:'):
		sesh.curr_page = 2
	st.markdown('----------------------------------')

	#hive_db = db_helper.db()
	#hive_db.add_user("leonhsieh@yahoo.com", "100999shieh")

	#st.write('PAGE NUMBER:', sesh.curr_page)
	page_turning_function = PAGES[sesh.curr_page]
	#t.write(sesh.curr_page)
	page_turning_function.app()



if __name__ == "__main__":
	main()

