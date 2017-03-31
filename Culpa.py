import os
from flask import Flask, jsonify
import json
import requests
from flask import request
from Models import Courses,Departments,Professors,Reviews
from sqlalchemy import create_engine, func,select
from setup import session

app = Flask(__name__)
HOST = ""

@app.route('/')
def hello_world():
    return 'CULPA2 API Server'

@app.route('/saveReview')
def store_review():
    tr = True;

@app.route('/getProfessor')
def get_professor():
    prof = request.args.get('prof')
    prof_searches = session.query(Professors.professor).filter(Professors.professor.last_name.like("%Rob%")).all()
    with open("./data/professor.json", 'r') as f:
        _data = f.read()
        return_prof = json.loads(_data)
        # for i in range(len(prof_searches)):
        #     return_prof['messagess'][0]['quick_replies'][i]['title'] = prof_searches[i].first_name + " " + prof_searches[i].middle_name + " " + prof_searches[i].last_name
        return jsonify(return_prof)

@app.route('/getClass')
def get_class():
    prof_id = request.args.get('id')
    r = requests.get("http://api.culpa.info/professor_id/"+prof_id);
    with open("./data/class.json", 'r') as f:
        _data = f.read()
        course_obj = json.loads(_data)
        # for i in range(course_objs.courses):
        #     course_obj.messages[0].quick_replies[i].title = course_objs.courses[i].name
        return jsonify(course_obj)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
