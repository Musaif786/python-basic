## python script for get request ###

import requests
import config

#print(config.url())

def getFun(txt):
    url = config.getUrl()
    req = requests.get(url)
    if req.status_code ==200:
        #response = req.content
        data =req.text
        #data =req.json()
        with open(txt,'a') as file:
            #getFun() 
            file.write(data + "\n\n")
        print("Data is saved {} file".format(txt))
        
        
        #readfile(txt) / to read the content
    
    else:
        print("failed to add logs")
def readfile(txt):
    with open(txt,'r') as file:
        lines = file.readlines()
        for i in lines:
            print(i.strip())
    
txt = 'savelogs.json'
getFun(txt)     
#savelogs(getFun())
#print(getFun())