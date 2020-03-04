import configparser
import requests
config = configparser.RawConfigParser()
config.read('var/www/settings.ini')
#auth = config['KHALKEUS']['Token']
auth = config['AARON']['Token']

r = requests.get('https://api.ciscospark.com/v1/rooms',
                  headers={'Authorization': 'Bearer {auth}'.format(auth=auth)})

print(r.text)
