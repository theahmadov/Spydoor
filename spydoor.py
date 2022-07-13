from colorama import *
from sys import exit
import requests
import os
from dotenv import load_dotenv
from core import githubscrape
import time
from lib.portscan import scan
load_dotenv()

class info:
    github=os.getenv("github")
    ip = requests.get("https://api.ipify.org").text
    
    
def banner():
    """
 ___              _                
/ __> ___  _ _  _| | ___  ___  _ _ 
\__ \| . \| | |/ . |/ . \/ . \| '_>
<___/|  _/`_. |\___|\___/\___/|_|  
     |_|  <___'                  
     """
    print("""
 ___              _                
/ __> ___  _ _  _| | ___  ___  _ _ 
\__ \| . \| | |/ . |/ . \/ . \| '_>
<___/|  _/`_. |\___|\___/\___/|_|  
     |_|  <___'                  

                    [+] Spydoor terminal created by TheSadError
    """)
class log:
    username = os.getenv("lusername")
    password = os.getenv("lpassword")
    logf = False

def specialcommands(command):
    if command == "ip":
        print(Fore.BLUE+f"IP : {info.ip}")
    elif command == "gitinfo":
        githubscrape.getinfo(info.github)
    elif command.startswith("ports"):
        url = command.split("ports ")
        scan(url[1])
    elif command == "help":
        print("ip : prints ip ")
        print("gitinfo : prints github information (edit .env file to use it for you.) ")
        print("ports url : port scan url")
        print("help : help for commands")
    else:
        try :
            os.system(command)
        except :
            print(Fore.RED+"[!] Unknown command : {command} , Type help for list commands.")


def login(username,password):
    if username=="error" and password == "clear":
        log.logf = True
    else:
        log.logf = False
        os.system("python3 ./python-packets/accesdenied.py")
        print(Fore.RED+"[!] Login Acces Denied")
        print(Fore.RED+"Exitting...")
        time.sleep(1)

        exit(0)

if __name__ == "__main__":
    os.system("cls")
    banner()
    login(log.username,log.password)
    while log.logf:
        ask = input(Fore.YELLOW+"$ ")
        specialcommands(ask)