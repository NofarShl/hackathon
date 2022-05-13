import json

file_name = "courses.json"
file_dict = json.loads(file_name)
for course in file_dict:
    course_type = course["type"]
    faculty = course["faculty"]
    course_num = course["course_number"]
    course_name = course["course_name"]
    proff = course["professor"]
    exam_essay = course["exam_essay"]
    exam_date = course["exam_date"]
    nakaz = course["nakaz"]
    Course = course(course_type,faculty,course_num,course_name,proff,exam_essay,exam_date,nakaz)







