import pyrebase

class db:
	def __init__(self):
		config = {
		"apiKey": "AIzaSyDe2CZpsYPIMQneper6tEe_qaAO9XDWNzQ",
		"authDomain": "hive-f0de6.firebaseapp.com",
		"databaseURL": "https://hive-f0de6.firebaseio.com",
		"storageBucket": "hive-f0de6.appspot.com",
		"serviceAccount": "/Users/derektang/Downloads/hive-f0de6-firebase-adminsdk-5k61d-4cb9e04361.json"
		}
		self.firebase = pyrebase.initialize_app(config)
		self.auth = self.firebase.auth()

	def add_user(self, email, password):
		self.auth.create_user_with_email_and_password(email, password)
