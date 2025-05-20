import requests
import json
from constants import API_KEY

search_url = "https://api.golfcourseapi.com/v1/search"
get_course_url = "https://api.golfcourseapi.com/v1/courses/{id}"
api_healthcheck_url = "https://api.golfcourseapi.com/v1/healthcheck"




def check_api_health():
    response = requests.get(api_healthcheck_url)
    print(response.status_code)
    if response.status_code == 200:
        return "good response from api"
    else:
        return "bad response from api"
    
def search_for_course(search_query):
    header = {
        "Authorization": API_KEY
    }

    params = {
        "search_query": search_query
    }

    response = requests.get(search_url, headers=header, params=params)

    data = response.json()
    return data