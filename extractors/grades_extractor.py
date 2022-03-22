import bs4
from models.course import Course
from models.semester import Semester

def html_findall(page):
    soup = bs4.BeautifulSoup(
                        page,
                        "html.parser"
                        )
    return soup.findAll

class CoursesGradesExtractor:
    def __init__(self, html: str):
        self.__data = html

    def __get_courses(self, table):
        '''
        Yields courses info
        '''
        courses = table.find('tbody').findAll('tr')
        for course in courses:
            course = iter(course.findAll('td'))
            yield Course(
                code=next(course).text,
                name=next(course).text.strip('\n'),
                hours=next(course).text,
                degree=next(course).text,
                grade=next(course).text,
            )

    def __get_gpa_stuff(self, table):
        '''
        Yields footer elements (Term GPA, GPA, .. etc)
        '''
        footer = table.find('tfoot').find('div', {'class': 'row'})
        for row in footer.findAll('div'):
            key = row.text
            value = row.find('span').text
            yield key.replace(value, '').strip()


    def process(self):
        semesters = []
        try:
            # Get all cards (semesters)
            cards = html_findall(self.__data)('div', {'class': 'card'})
            for card in cards:
                
                # Get semester name and year
                s_head = card.find('div', {'class': 'card-header'}).text
                s_title, s_year = s_head.split()

                grade_table = card.find('table', {'class': 'table'})
                
                # Get semester courses
                courses = self.__get_courses(grade_table)
                
                # Get semester gpa meta info
                footer = self.__get_gpa_stuff(grade_table)

                semesters.append(
                    Semester(
                        name=s_title,
                        year=s_year,
                        courses=[*courses],
                        term_gpa=next(footer),
                        total_gpa=next(footer),
                        attempted_hours=next(footer),
                        total_earned_hours=next(footer),
                    )
                )

            return semesters[::-1]
        except AttributeError:
             return []
    