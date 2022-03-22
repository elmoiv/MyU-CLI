__import__('warnings').filterwarnings("ignore")

import requests
import os

BASE_URL = 'https://myu.mans.edu.eg/'
LOGIN_URL = BASE_URL + 'login'
MOODLE_URL = BASE_URL + 'moodle/moodle?{}&app_id=48&click_item_id='

class MyuDaemon(requests.Session):
    def __init__(self, username, password):
        super().__init__()
        self.username = username
        self.password = password
        self.__data = None
        self.__id = None
    
    def connect(self):
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
        self.post(LOGIN_URL, data=login_payload, verify=False)

        # Get home page data
        self.__data = self.get(BASE_URL, verify=False).text
        self.__id = self.__data.split('UID = ')[-1].split(';')[0]
    
    @property
    def moodle_url(self):
        moodle_raw = self.get(
            MOODLE_URL.format(self.__id),
            verify=False
            ).text
        
        return moodle_raw.split('url = ')[-1].split(';')[0]
    
    def open_moodle(self):
        os.system('start "" ' + self.moodle_url)
