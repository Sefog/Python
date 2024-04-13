import json
from urllib.request import urlopen
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
address = input('Enter an address - ')
if address == '':
    quit()
data = urlopen(address).read()
data = json.loads(data)
total = 0
for user in data['comments']:
    total = total + user['count']

print('Total comments:', total)
