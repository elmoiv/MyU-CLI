import bs4
from ..models.hour_progress_course import HourProgressCourse

def html_findall(page):
    soup = bs4.BeautifulSoup(
                        page,
                        "html.parser"
                        )
    return soup.findAll

def html_find(page):
    soup = bs4.BeautifulSoup(
                        page,
                        "html.parser"
                        )
    return soup.find

class HoursProgressExtractor:
    def __init__(self, html: str):
        self.__data = html

    def process(self):
        hour_progress_courses = []
        try:
            # Get main table
            main_table = html_find(self.__data)('table', {'class': 'table table-bordered table-sm'}).find('tbody')

            # Get rows that only contains courses
            # Skip those sectional rows (e.g: those showing semster name)
            rows = [*filter(
                lambda i: len(i.findAll('td')) == 8,
                main_table.findAll('tr')
            )]

            for row in rows:
                cells = iter(row.findAll('td'))
                hour_progress_courses.append(
                    HourProgressCourse(
                        code=next(cells).text,
                        name=next(cells).text,
                        hours=next(cells).text,
                        ctype=next(cells).text,
                        prequisite=next(cells).text,
                    )
                )
            
            return hour_progress_courses

        except AttributeError:
            return None