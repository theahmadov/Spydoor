import json
from re import I
import requests
from colorama import *
import core.js as js

def getinfo(username):
    url = "https://api.github.com/users/{}".format(username)
    data = requests.get("https://api.github.com/users/{}".format(username)).text
    js.jsd(f"{username}-github", data)
    need = [
            'followers',
            'location',
            'public_repos',
            'location',
            'bio',
            'email'
        ]
    req = requests.get(url).json()
    dt = js.pdata(need, req)
    print(json.dumps(dt, indent= True))