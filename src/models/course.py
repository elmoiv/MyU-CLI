decide = lambda i, t: t(i) if i else None

grade_to_gpa = {
    'A+': 4,
    'A': 4,
    'A-': 3.7,
    'B+': 3.3,
    'B': 3,
    'B-': 2.7,
    'C+': 2.3,
    'C': 2,
    'C-': 1.7,
    'D+': 1.3,
    'D': 1,
    'F': 0,
}
class Course:
    def __init__(self, name, code, hours, degree, grade):
        self.code = code
        self.name = name
        self.hours = decide(hours, float)
        self.degree = decide(degree, float)
        self.grade = decide(grade, str)
        self.gpa = grade_to_gpa.get(grade, -1)
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'hours': self.hours,
            'degree': self.degree,
            'grade': self.grade,
            'gpa': self.gpa,
        }

    def __repr__(self):
        return f'Course<{self.code}>'
