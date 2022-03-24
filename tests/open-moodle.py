import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.myu import Myu

myu = Myu(json_path='credentials.json')

print('>>> Conencting to Myu...')
myu.connect()

print('>>> Openning Moodle...')
myu.open_moodle()