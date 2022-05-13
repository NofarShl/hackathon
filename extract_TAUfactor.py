import json
import requests
import urllib

course_dict = {"0368-1118": "", "0366-1111": "", "0366-1101": ""}
URL = "https://www.tau-factor.com/api/v1/courses/?course_code="

for course in course_dict.keys():
    URL += str(course)
    response = urllib.request.urlopen(URL)
    data = json.loads(response.read())
    course_dict[course] = data["results"][0]["instances"][0]["statistics"]["mean"]
    URL = str("https://www.tau-factor.com/api/v1/courses/?course_code=")

print(course_dict)