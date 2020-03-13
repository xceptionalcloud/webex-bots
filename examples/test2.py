import configparser
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder
config = configparser.RawConfigParser()
config.read('/var/www/settings.ini')

gAuth = config['GIPHIER']['Token']
kAuth = config['KHALKEUS']['Token']

room = config['MNE']['ID']

images = {
    'ayb': config['IMAGES']['AYB'],
    'developer': config['IMAGES']['Developer'],
    'afx': config['IMAGES']['Afx'],
    'automation': config['IMAGES']['Automation'],
    'hephaestus': config['IMAGES']['Hephaestus'],
    'turk': config['IMAGES']['Turk'],
    'matters': config['IMAGES']['Matters']
}
m = MultipartEncoder({'roomId': room,
                      'text': 'hey boss',
                      'files': (images['hephaestus'], open(images['hephaestus'], 'rb'),
                      'image/png')})

r = requests.post('https://api.ciscospark.com/v1/messages', data=m,
                  headers={'Authorization': 'Bearer {auth}'.format(auth=kAuth),
                  'Content-Type': m.content_type})

print(r.text)
