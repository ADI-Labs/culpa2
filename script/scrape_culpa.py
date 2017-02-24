# Scrape down all the courses and professors from CULPA.
# Assumes you are running from the root of the project.

import requests
import json

BASE_URL = 'http://api.culpa.info'

departments = json.loads(open('./data/departments.json', 'r').read())

for dept in departments['departments']:
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