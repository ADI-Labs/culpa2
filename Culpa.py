# -*- coding: utf-8 -*-

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
    # prof_searches = session.query(Professors.professor).filter(Professors.professor.last_name.ilike("%{0}%".format(prof))).limit(5).all()
    r = requests.get("http://api.culpa.info/professors/search/"+prof);
    json_response = r.json()

    prof_searches = json_response['professors']

    if len(prof_searches) == 0:
        response = {
          "set_attributes":
          {
            "review_professor": "-1"
          },
          "messages": [
            {
              "text":  "There doesn't seem to be a professor with that name. Check your spelling or search another professor."
            }
          ]
        }
        return jsonify(response)
    else:
        professor_options = []

        for prof in prof_searches[0:5]:
            professor_options.append({
                "title": prof['first_name'] + " " + prof['last_name'],
                "set_attributes": {
                    "review_professor": prof['first_name'] + " " + prof['last_name'],
                    "review_professor_id": prof['id']
                },
                "block_names": ["Class Search"],
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

    for course in courses[0:5]:
        course_options.append({
            "title": course['name'],
            "set_attributes": {
                "review_class": course['name'],
                "review_professor_id": prof_id
            },
            "block_names": ["Review Entry"],
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

@app.route('/searchClass')
def search_class():
    lookup_class = request.args.get('lookup_class')
    r = requests.get("http://api.culpa.info/courses/search/"+lookup_class);
    json_response = r.json()

    courses = json_response['courses']

    if len(courses) == 0:
        response = {
          "set_attributes":
          {
            "lookup_class": "-1"
          },
          "messages": [
            {
              "text":  "There doesn't seem to be a class with that name. Check your spelling or search another class."
            }
          ]
        }
    else:
        course_options = []

        for course in courses[0:5]:
            course_options.append({
                "title": course['name'],
                "set_attributes": {
                    "lookup_class": course['name'],
                    "lookup_class_id": course['id'],
                },
                "block_names": ["Choose Class Professor"],
                "type": "show_block"
            })

        response = {
            'messages': [
                {
                    "text": "Here's the classes that look like \"{{lookup_class}}\". Which one would you like to look at?",
                    "quick_replies": course_options
                }
            ]
        }

    return jsonify(response)

@app.route('/getProfessorByClass')
def get_professor_by_class():
    lookup_class_id = request.args.get('lookup_class_id')
    r = requests.get("http://api.culpa.info/professors/course_id/"+lookup_class_id);
    json_response = r.json()

    prof_searches = json_response['professors']

    professor_options = []

    for prof in prof_searches[0:5]:
        professor_options.append({
            "title": prof['first_name'] + " " + prof['last_name'] + " U+1F603",
            "set_attributes": {
                "lookup_professor": prof['first_name'] + " " + prof['last_name'],
                "lookup_professor_id": prof['id']
            },
            "block_names": ["Get Review"],
            "type": "show_block"
        })

    response = {
        'messages': [
            {
                "text": "Which of these teachers would you like to look at?",
                "quick_replies": professor_options
            }
        ]
    }

    return jsonify(response)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
