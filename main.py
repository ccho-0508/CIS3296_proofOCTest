import requests
import json

link = "https://fim.temple.edu/idp/profile/SAML2/Redirect/SSO;jsessionid=0EFB6F2B274E32CC98A4CDEEA09C59B3?execution=e1s1"

def login(email, password):
    s = requests.Session()
    payload = {
        'j_username': email,
        'j_password': password
    }

    response = s.post(link, data=payload)

    print(response)
    return s

session = login('tun66463', 'Chobomi@@1838')

