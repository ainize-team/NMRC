import json

import firebase_admin
from firebase_admin import credentials, db


def init_firebase():
    cred = credentials.Certificate("keys/mlops-crawler-firebase.json")
    with open('keys/databaseURL.json') as f:
        data = json.load(f)
        firebase_admin.initialize_app(cred, data)
    print('Initialize firebase done.')


def update_data(document_id, data):
    db.reference()
    ref = db.reference(f'/raw/{document_id}')
    ref.set(data)
