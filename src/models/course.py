decide = lambda i, t: t(i) if i else None

class Course:
    def __init__(self, name, code, hours, degree, grade):
        self.code = code
        self.name = name
        self.hours = decide(hours, float)
        self.degree = decide(degree, float)
        self.grade = decide(grade, str)
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'hours': self.hours,
            'degree': self.degree,
            'grade': self.grade,
        }

    def __repr__(self):
        return f'Course<{self.code}>'
