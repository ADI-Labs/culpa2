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
    prof = request.args.get('review_professor')
    prof_searches = session.query(Professors.professor).filter(Professors.professor.last_name.ilike("%{0}%".format(prof))).limit(5).all()

    if len(prof_searches) == 0:
        return jsonify({})
    else:
        professor_options = []

        for prof in prof_searches:
            professor_options.append({
                "title": prof.first_name + " " + prof.last_name,
                "set_attributes": {
                    "review_professor": prof.first_name + " " + prof.last_name,
                    "review_professor_id": prof.professor_key
                },
                "block_names": ["Entry Class Demo"],
                "type": "show_block"
            })

        response = {
            'messages': [
                {
                    "text": "Which of these names looks right?",
                    "quick_replies": professor_options
                }
            ]
        }

        return jsonify(response)

@app.route('/getClass')
def get_class():
    prof_id = request.args.get('review_professor_id')
    r = requests.get("http://api.culpa.info/courses/professor_id/"+prof_id);
    json_response = r.json()
    courses = json_response['courses']


    course_options = []

    for course in courses:
        course_options.append({
            "title": course['name'],
            "set_attributes": {
                "review_class": course['name'],
                "review_professor_id": prof_id
            },
            "block_names": ["Entry Class Demo"],
            "type": "show_block"
        })

    response = {
        'messages': [
            {
                "text": "Here's the classes taught by {{review_professor}}. Which one would you like to review?",
                "quick_replies": course_options
            }
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
