import json
import firebase_admin
from firebase_admin import credentials, db


def init_firebase():
    cred = credentials.Certificate("keys/mlops-crawler-firebase.json")
    with open('keys/databaseURL.json') as f:
        data = json.load(f)
        firebase_admin.initialize_app(cred, data)
    print('Initialize firebase done.')


def updateData(data):
    db.reference()
    ref = db.reference("/raw")
    ref.update(data)
