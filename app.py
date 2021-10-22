import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db

def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    # @app.route('/')
    # def get_greeting():
    #     excited = os.environ['EXCITED']
    #     greeting = "Hello" 
    #     if excited == 'true': greeting = greeting + "!!!!!"
    #     return greeting

    # @app.route('/coolkids')
    @app.route('/')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    return app

app = create_app()

if __name__ == '__main__':
    app.run()
    # app.run(host='0.0.0.0', port=8000, debug=True)
