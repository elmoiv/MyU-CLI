import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.myu import Myu

myu = Myu(json_path='credentials.json')

print('>>> Conencting to Myu...')
myu.connect()

print('>>> Getting Courses Grades...')
courses = myu.get_courses_grades().courses_only

print('>>> Getting Credit Hours...')
hours_progress = myu.get_hours_progress()
credit_hours_bycode = hours_progress.credit_hours_only()
credit_hours_byname = hours_progress.credit_hours_only(by_name=True)

numerator = 0
denominator = 0

p_numerator = 0
p_denominator = 0

for course in courses:
    if course.degree == 0:
        continue
    p_numerator += course.degree
    p_denominator += 100
    gpa = course.gpa
    # if gpa > 0:
    credit_hours = credit_hours_bycode.get(course.code, -1)
    if course.code not in credit_hours_bycode:
        credit_hours = credit_hours_byname[course.name]
    numerator += gpa * credit_hours
    denominator += credit_hours

cGPA = numerator / denominator
perc = p_numerator / p_denominator

print()

print(f'Your cGPA                                 =  {cGPA}')
print(f'Your cGPA (rounded)                       =  {round(cGPA, 2)}')
print(f'Your percentage (cGPA related)            =  {cGPA / 4 * 100}%')
print(f'Your percentage (cGPA related) (rounded)  =  {round(cGPA / 4 * 100, 2)}%')
print(f'Your percentage                           =  {perc * 100}%')
print(f'Your percentage (rounded)                 =  {round(perc * 100, 2)}%')
input()