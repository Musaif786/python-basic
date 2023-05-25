### post script ##

import config
import requests
import os

#print(config.token())

url = config.postUrl()
token = config.token()

name = input('enter name here: ')
email = input('enter gamil: ')
gender = input('enter gender: ')
status = input('enter status: ')

data = dict()
data['name'] = name
data['email'] = email
data['gender'] = name
data['status'] = status

header = dict()
#headers['Authorization'] = token
header['Authorization'] = 'Bearer' + config.token()
header['Accept'] = 'application/json' 


r = requests.post(url, data = data, headers = header)
print(r.json())