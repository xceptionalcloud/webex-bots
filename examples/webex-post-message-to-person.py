import configparser
import requests
import datetime
from requests_toolbelt.multipart.encoder import MultipartEncoder
config = configparser.RawConfigParser()
config.read('settings.ini')

gAuth = config['GIPHIER']['Token']
kAuth = config['KHALKEUS']['Token']
aAuth = config['AARON']['Token']

room = config['CHICO']['ID']
person = 'alangford@xceptional.com'

images = {
    'ayb': config['IMAGES']['AYB'],
    'developer': config['IMAGES']['Developer'],
    'afx': config['IMAGES']['Afx'],
    'automation': config['IMAGES']['Automation'],
    'hephaestus': config['IMAGES']['Hephaestus'],
    'turk': config['IMAGES']['Turk'],
    'matters': config['IMAGES']['Matters'],
    'lunch': config['IMAGES']['Lunch'],
    'garfield': config['IMAGES']['Garfield'],
    'towel': config['IMAGES']['Towel']
}
m = MultipartEncoder({'roomId': room,
                      'text': 'test',
                      'files': (images['hephaestus'], open(images['hephaestus'], 'rb'),
                      '')})

r = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer {auth}'.format(auth=aAuth),
                  'Content-Type': m.content_type})

print(r.text)
