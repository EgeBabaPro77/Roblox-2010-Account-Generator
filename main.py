import requests
import random
from colorama import Fore, Back, Style
import time
import robloxpy

id = 12532999

print(Fore.RED + '''
 .d8888b.                           888 d8b          
d88P  Y88b                          888 Y8P          
Y88b.                               888              
 "Y888b.   888d888 .d88b.  888  888 888 888  8888b.  
    "Y88b. 888P"  d8P  Y8b `Y8bd8P' 888 888     "88b 
      "888 888    88888888   X88K   888 888 .d888888 
Y88b  d88P 888    Y8b.     .d8""8b. 888 888 888  888 
 "Y8888P"  888     "Y8888  888  888 888 888 "Y888888 
''')
print("Roblox 2010 Account Generator")
print(Style.RESET_ALL)


def get_username(user_id):
    url = f"https://api.roblox.com/users/{user_id}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()['Username']
    else:
        return None

while True:
    id = random.randint(12533000, 12535000)
    username = get_username(id)
    time.sleep(0.2)
    if username == "0x000A":
        print(Fore.RED + f"UserId: {id} Not Found!")
    elif username[0:6] == "roblox":
        continue
    elif username.find("xitx") == -1 and username.find("xitt") == -1:
        lol = f"https://api.roblox.com/users/{id}/onlinestatus/"
        responsex = requests.get(lol)
        time.sleep(0.2)
        a = responsex.json()['LastOnline']
        b = a.split("-")
        c = b[0]
        x = robloxpy.User.External.CreationDate(id)
        y = x.split("/")
        z = int(y[2])
        if len(username) == 20 and z == 2010 and int(c) == 2010:
            print(Fore.GREEN + f"Username: {username} UserId: {id} LastOnline: {c} Password: l0l0l0l")
    id += 1
