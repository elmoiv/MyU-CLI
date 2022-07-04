decide = lambda i, t: t(i) if i else None

class HourProgressCourse:
    def __init__(self, name, code, hours, ctype, prequisite):
        self.code = code
        self.name = name
        self.hours = decide(hours, int)
        self.type = ctype
        self.prequisite = prequisite
    
    def to_dict(self):
        return {
            'code': self.code,
            'name': self.name,
            'hours': self.hours,
            'type': self.type,
            'prequisite': self.prequisite,
        }

    def __repr__(self):
        return f'HourProgressCourse<{self.code}>'