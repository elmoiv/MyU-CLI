decide = lambda i, t: t(i) if i else None

class Semester:
    def __init__(
        self,
        name,
        year,
        courses,
        term_gpa,
        total_gpa,
        attempted_hours,
        total_earned_hours
    ):
        self.name = name
        self.year = year
        self.courses = courses
        self.term_gpa = decide(term_gpa, float)
        self.total_gpa = decide(total_gpa, float)
        self.attempted_hours = decide(attempted_hours, float)
        self.total_earned_hours = decide(total_earned_hours, float)
    
    def to_dict(self):
        return {
            'name': self.name,
            'year': self.year,
            'courses': [
                course.to_dict() for course in self.courses
            ],
            'term gpa': self.term_gpa,
            'total gpa': self.total_gpa,
            'attempted hours': self.attempted_hours,
            'total earned hours': self.total_earned_hours,
        }

    def __repr__(self):
        return f'Semester<{self.year}, {self.name}>'
