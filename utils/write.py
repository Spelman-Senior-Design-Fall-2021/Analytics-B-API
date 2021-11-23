import firebase_admin
from firebase_admin import credentials, db

cred_obj = credentials.Certificate('./analytics-b-api-firebase-adminsdk-dos39-1db36dc4b1.json')
default_app = firebase_admin.initialize_app(cred_obj, {
	'databaseURL': 'https://analytics-b-api-default-rtdb.firebaseio.com/'
	})


# def store(s_results, p_results):
def store(data):
    ref = db.reference("/query")
    
    ref.set(data)