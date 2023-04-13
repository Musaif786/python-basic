#This is testing python file for splunk

import os
import sys
import requests

url = 'https://musaif.netlify.com'
url1 = 'https://w3schools.com/python/demopage.ph'
#x = requests.get(url1, params = {"model": "Mustang"})
#x = requests.get(url1)
myobj = {'somekey': 'somevalue'}

#x = requests.post(url, json = myobj)
x = requests.delete('https://w3schools.com/python/demopage.php')

print(x.text)
print(x.status_code)

print("check whether above modules are running or not")