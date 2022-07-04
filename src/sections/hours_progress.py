from ..extractors.hours_progress_extractor import HoursProgressExtractor

class HoursProgress(HoursProgressExtractor):
    def __init__(self, data):
        super().__init__(data)
        self.__hour_progress_courses = self.process()

    def to_dict(self):
        return [
            prog.to_dict() for prog in self.__hour_progress_courses
        ]

    def credit_hours_only(self, by_name=False):
        return {
            course.name if by_name else course.code: course.hours \
            for course in self.__hour_progress_courses
        }

    @property
    def courses(self):
        return self.__hour_progress_courses