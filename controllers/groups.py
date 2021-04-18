import streamlit as st
import numpy as np
import time

def app():
	icon_button, group_name, notification_ind = st.beta_columns(3)
	# You can use a column just like st.sidebar:
	icon_button.button('Hive 1')
	group_name.text("CalHacksHive!")
	notification_ind.text("3 Notifications")

	icon_button, group_name, notification_ind = st.beta_columns(3)
	# You can use a column just like st.sidebar:
	icon_button.button('Hive 3')
	group_name.text("TheBesties!")
	notification_ind.text("2 Notifications")

	icon_button, group_name, notification_ind = st.beta_columns(3)
	# You can use a column just like st.sidebar:
	icon_button.button('Hive 2')
	group_name.text("ThisIsOurGroupName")
	notification_ind.text("0 Notifications")
	
	