from daemon import MyuDaemon

USERNAME = '123456789'
PASSWORD = 'ABCDEFGHI'

myu = MyuDaemon(USERNAME, PASSWORD)
print('>>> Conencting to Myu...')
myu.connect()
print('>>> Openning Moodle...')
myu.open_moodle()
