from api_functions import *
import json

course_name = "riverridge"
data = search_for_course(course_name)

with open("example.json", 'w') as file:
    json.dump(data, file, indent=4)

