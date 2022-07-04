import matplotlib.pyplot as plt
from ..extractors.grades_extractor import CoursesGradesExtractor

class CoursesGrades(CoursesGradesExtractor):
    def __init__(self, data):
        super().__init__(data)
        self.__semesters = self.process()
    
    def to_dict(self):
        return [
            sem.to_dict() for sem in self.__semesters
        ]

    def plot_gpa(self):
        x_values = [f'{s.year} - {s.name}' for s in self.__semesters if s.term_gpa]
        y_values = [s.term_gpa for s in self.__semesters if s.term_gpa]

        plt.xticks(rotation=15)
        plt.plot(x_values, y_values)
        for a, b in zip(x_values, y_values): 
            plt.text(a, b, str(b))
        plt.show()

    @property
    def courses_only(self):
        courses = []
        for sem in self.__semesters:
            courses += sem.courses
        return courses

    @property
    def semesters(self):
        return self.__semesters