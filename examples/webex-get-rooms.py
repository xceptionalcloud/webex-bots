import configparser
import requests
config = configparser.RawConfigParser()
config.read('settings.ini')
auth = config['KHALKEUS']['Token']

r = requests.get('https://api.ciscospark.com/v1/rooms',
                  headers={'Authorization': 'Bearer {auth}'.format(auth=auth)})

print(r.text)