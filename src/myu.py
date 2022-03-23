__import__('warnings').filterwarnings("ignore")

import requests
import os

from .exceptions import LoginFailedException
from .sections.personal_data import PersonalData
from .sections.courses_grades import CoursesGrades

BASE_URL = 'https://myu.mans.edu.eg/'
LOGIN_URL = BASE_URL + 'login'
PROFILE_URL = BASE_URL + 'personal/?{}&app_id=2&click_item_id='
MOODLE_URL = BASE_URL + 'moodle/moodle?{}&app_id=48&click_item_id='
GRADES_URL = BASE_URL + 'education/grades?{}&app_id=4&click_item_id='

class Myu(requests.Session):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.__data = None
        self.__id = None
    
    def connect(self):
        # Change Language to English
        self.cookies.set('SP_django_language', 'en', domain='myu.mans.edu.eg')
        
        # Getting csrf
        main_resp = self.get(BASE_URL, verify=False)
        csrf_token = main_resp.headers['Set-Cookie'] \
                              .split('csrftoken=')[-1].split(';')[0]
        # Logging in
        login_payload = {
            'csrfmiddlewaretoken': csrf_token,
            'txtUserName': self.username,
            'txtPassword': self.password,
            'hdnLang': 'en',
        }
        self.post(LOGIN_URL, data=login_payload)

        # Get home page data
        home_resp = self.get(BASE_URL)

        # Check if login is a success
        if not 'sessionid=' in home_resp.headers['Set-Cookie']:
            raise LoginFailedException('Incorrect username or password!') 

        self.__data = home_resp.text
        self.__id = self.__data.split('UID = ')[-1].split(';')[0]
    
    @property
    def moodle_url(self):
        moodle_raw = self.get(
            MOODLE_URL.format(self.__id),
            ).text

        return moodle_raw.split('url = "')[-1].split('";')[0]
    
    def open_moodle(self):
        os.system(f'start "" "{self.moodle_url}"')

    def get_personal_data(self):
        user_resp = self.get(PROFILE_URL)
        return PersonalData(user_resp.text)
    
    def get_courses_grades(self):
        grade_resp = self.get(GRADES_URL)
        return CoursesGrades(grade_resp.text)

