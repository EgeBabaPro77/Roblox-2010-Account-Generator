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
    url = f"https://www.roblox.com/avatar-thumbnails?params=%5B%7BuserId:{user_id}%7D%5D"
    response = requests.get(url)
    
    if response.status_code == 200:
        json_data = response.json()
        
        if json_data and isinstance(json_data, list) and len(json_data) > 0:
            if json_data[0] is None or json_data[0]['name'] == "null":
                return "Banlı"
            else:
                return json_data[0]['name']
        else:
            return None
    else:
        return None

while True:
    id = random.randint(12530000, 12535000)
    idd = [id]
    username = get_username(id)
    time.sleep(0.2)
    if username == "Banlı":
        print(Fore.RED + f"UserId: {id} Not Found!")
    elif username[0:6] == "roblox":
        continue
    elif username.find("xitx") == -1 and username.find("xitt") == -1 and username.find("tixt") == -1:
        time.sleep(0.2)
        a = requests.post('https://presence.roblox.com/v1/presence/last-online', json={'userIds': idd}).json()['lastOnlineTimestamps'][0]['lastOnline'].split('T')[0]
        b = a[0:4]
        c = int(b)
        x = robloxpy.User.External.CreationDate(id)
        y = x.split("/")
        z = int(y[2])
        if len(username) == 20 and z == 2010 and int(c) == 2010:
            print(Fore.GREEN + f"Username: {username} UserId: {id} LastOnline: {c} Password: l0l0l0l")
    id += 1
