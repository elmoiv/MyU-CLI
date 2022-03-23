from myu import Myu

USERNAME = '123456789'
PASSWORD = '*********'

myu = Myu(USERNAME, PASSWORD)
print('>>> Conencting to Myu...')
myu.connect()

print('>>> Getting Courses Grades...')
grades = myu.get_courses_grades()
# print(grades.to_dict())
grades.plot_gpa()
# data = myu.get_personal_data()
# print(data.to_dict())
# print('>>> Openning Moodle...')
# print(myu.moodle_url)
# myu.open_moodle()
