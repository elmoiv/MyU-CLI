import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.myu import Myu

USERNAME = '800125805'
PASSWORD = 'Khaled_2811999'

myu = Myu(USERNAME, PASSWORD)
print('>>> Conencting to Myu...')
myu.connect()

print('>>> Getting Courses Grades...')
grades = myu.get_courses_grades()

print('>>> Plotting Grades...')
grades.plot_gpa()