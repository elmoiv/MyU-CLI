from myu import Myu

# myu = Myu(username='800125805', password='Khaled_2811999')
myu = Myu(username='800125542', password='merna18Mm')
print('>>> Conencting to Myu...')
myu.connect()
grades = myu.get_courses_grades()
# print(grades.to_dict())
grades.plot_gpa()
# data = myu.get_personal_data()
# print(data.to_dict())
# print('>>> Openning Moodle...')
# print(myu.moodle_url)
# myu.open_moodle()