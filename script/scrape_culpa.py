# Scrape down all the courses and professors from CULPA.
# Assumes you are running from the root of the project.

import requests
import json
from Models.Departments import departmemt
from Models.Professors import professor
from Models.Courses import course
from sqlalchemy import create_engine
from sqlalchemy.orm  import sessionmaker
import os

URI = "postgres://xeeqkeipvcflil:fead0f891152e8f657d7ee59ba256aa36c24fed629a0ee765b6a6aac6da2610f@ec2-54-225-236-102.compute-1.amazonaws.com:5432/d7mipabothqsm0"
engine = create_engine(URI)
engine.connect()
Session = sessionmaker(bind=engine)
session = Session()

def scrape():
    BASE_URL = 'http://api.culpa.info'

    departments = json.loads(open('./data/departments.json', 'r').read())

    for dept in departments:
        id = dept['id']
        name = dept['name']

        # Get courses for the department.

        response = requests.get(BASE_URL + '/courses/department_id/' + str(id))
        if response.status_code != 200:
            print("Error reading courses for department {0}".format(id))
        else:
            blob = json.loads(response.text)
            courses = blob['courses']
            num_courses = len(courses)
            # print("Retrieved {0} courses for the {0} department".format(num_courses, name))
            short_name = name.lower().replace(" ", "-")
            with open("./data/courses/{0}.json".format(short_name), 'w') as f:
                f.write(json.dumps(courses))

        # Get professors for the department

        response = requests.get(BASE_URL + '/professors/department_id/' + str(id))
        if response.status_code != 200:
            print("Error reading professors for department {0}".format(id))
        else:
            blob = json.loads(response.text)

            if blob['status'] == 'failed':
                print("Error reading professors for department {0}".format(id))
            else:
                profs = blob['professors']
                num_profs = len(profs)

                # print("Retrieved {0} professors for the {0} department".format(num_profs, name))
                short_name = name.lower().replace(" ", "-")
                with open("./data/professors/{0}.json".format(short_name), 'w') as f:
                    f.write(json.dumps(profs))


def save_departments(department):
    departments = json.loads(department)
    for dept in departments:
        dept1 = departmemt(name=dept['name'])
        session.add(dept1)
        session.commit()


def save_professors(prof2):
    professors = json.loads(prof2)
    for prof in professors:
        prof1 = professor(nugget=prof['nugget'], first_name=prof['first_name'], last_name=prof['last_name'], middle_name=prof['middle_name'])
        session.add(prof1)
        session.commit()


def save_courses(course_json):
    courses = json.loads(course_json)
    for course1 in courses:
        course2 = course(department_ids=course1['department_ids'], name=course1['name'], number=course1['number'])
        session.add(course2)
        session.commit()


def save():
    with open("../data/departments.json", 'r') as f:
        _data = f.read()
        #print(_data + "may be empty")
        #save_departments(_data)
    for filename in os.listdir('../data/courses'):
        with open("../data/courses/{0}".format(filename), 'r') as f:
            #save_courses(f.read())
            tr = True
    for data_file in os.listdir("../data/professors"):
        with open("../data/professors/{0}".format(data_file), 'r') as f:
           tr = True;
           save_professors(f.read())


save()



