import os, time, json, style_metadata
import main

class profileJSON:
    pass
    def __init__(self, username, bio, elo, level, health):
        self.username = username
        self.bio = bio
        self.elo = elo
        self.level = level
        self.health = health

def json_check(fileJSON_name) -> None:
    global fileJSON
    global userData
    
    fileJSON = fileJSON_name
    with open(fileJSON,  'r') as data:
        userData = json.load(data)


def start_menu():
    
    stats = {**userData, "user-profile":[{
             "elo":1000,
             "level":0,
             "xp":0,
             }]}
    
    if userData["isNew"] == "yes":
        with open(fileJSON, 'w') as writeData:
            new_add = json.dump(stats, writeData, indent=4)
        
    for data in userData["user-meta-data"]:
        user = data["user_name"]
        bio = data["bio"]
        
    style_metadata.style.logo()
    print("[WELCOME TO SCRIPTTO MENU-PANEL!]\n")
    print(f"welcome back!, {user}\n\n")
    json_check(fileJSON)
    
    options = {'1':"start-single",
               '2':"start-online [Not yet]",
               '3':"profile",
               '4':"store",
               '5':"go_back_login",
               '6':"quit"}
    for nums, opts in options.items():
        print(f"[{nums}:{opts}]")
    print()
    
    while True:
        userChoice = input(">")
        
        if userChoice == '1':
            pass
        elif userChoice == '2':
            pass
        elif userChoice == '3':
            pass
        elif userChoice == '4':
            pass
        elif userChoice == '5':
            userData["isNew"] = "no"
            dataNew = {**userData}
            with open(fileJSON, 'w') as writeData:
                new_add = json.dump(dataNew, writeData, indent=4)
            os.system('cls')
            return main.user_panel()
            
        elif userChoice == '6':
            userData["isNew"] = "no"
            dataNew = {**userData}
            with open(fileJSON, 'w') as writeData1:
                new_add = json.dump(dataNew, writeData1, indent=4)
            print("scriptto has stopped")
            break