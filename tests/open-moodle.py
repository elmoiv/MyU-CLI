import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.myu import Myu

USERNAME = '1111111'
PASSWORD = '1111111'

myu = Myu(USERNAME, PASSWORD)
print('>>> Conencting to Myu...')
myu.connect()

print('>>> Openning Moodle...')
myu.open_moodle()