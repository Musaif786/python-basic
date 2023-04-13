import requests
import json

url = "https://musaif.netlify.com"

x = requests.get(url)
print(x.status_code)

def send_sms(number,message):
    smsUrl = "https://www.fast2sms.com/dev/bulkV2"
    params = {
        'authorization' : 'yWN8tXc1hEwsHALoYT6F2qizK9QuRr5PjCBOmnV4JplGD0bIfxazxCZmLkOiBeF3tJfgUP07j2HVQs1d',
        "sender_id" : "FSTSMS",
        "message" : message,
        'numbers' : number,
        'route' : 'p',
        'language' : 'english'

    }
    resp = requests.get(smsUrl, params=params)
    dis = resp.json()
    print(dis)
    
    
send_sms("7995587687","hello how are you")
    