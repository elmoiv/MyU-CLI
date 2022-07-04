import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.myu import Myu

myu = Myu(json_path='credentials.json')

print('>>> Conencting to Myu...')
myu.connect()

print('>>> Getting Courses Grades...')
courses = myu.get_courses_grades().courses_only
hours_progress = myu.get_hours_progress().credit_hours_only()
sorted_courses = sorted(courses, key=lambda i: i.degree)[::-1]

for course in sorted_courses:
    print(course.name.ljust(80), course.degree)

input()