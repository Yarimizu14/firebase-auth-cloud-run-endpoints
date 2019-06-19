import os

from flask import Flask, request, jsonify
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials

cred_path = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
if cred_path:
    cred = credentials.Certificate(cred_path)
    default_app = firebase_admin.initialize_app(cred)
else:
    default_app = firebase_admin.initialize_app()

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return jsonify({
        'message': 'Hello World!!'
    })

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))