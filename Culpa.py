from flask import Flask
from sqlalchemy import create_engine
import sqlite3 as sql
app = Flask(__name__)
HOST = ""

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/saveReview')
def store_review():
    sql.adapters();


if __name__ == '__main__':
    app.run()


def setup():
    engine = create_engine()