import os, time, json
import main, __init__, style_metadata

class panels:
    
    def profile_panel(file_json):
        profile = file_json
        style_metadata.style.logo()
        
        for metaData in profile["user-meta-data"]:
            metaData = metaData
        for profileData in profile["user-profile"]:
            profileData = profileData
            
        print(f"[WELCOME TO YOUR PROFILE! {metaData['user_name']}]")
        print(f"""
            Username: {metaData["user_name"]} 
            Level:   [{profileData["level"]}]
            rank: [{profileData["rank"]}]""")

def json_check(fileJSON_name) -> None:
    global fileJSON
    global userData
    
    fileJSON = fileJSON_name
    with open(fileJSON,  'r') as data:
        userData = json.load(data)

def start_menu():
    style_metadata.style.logo()
    
    stats = {**userData, "user-profile":[{
             "rank":"bronze",
             "elo":1000,
             "level":0,
             "xp":0,
             }]}
    
    if userData["isNew"] == "yes":
        with open(fileJSON, 'w') as writeData:
            new_add = json.dump(stats, writeData, indent=4)
        
    for data in userData["user-meta-data"]:
        user = data["user_name"]
    
    print("[WELCOME TO SCRIPTTO MENU-PANEL!]\n")
    print(f"welcome back!, {user}\n\n")
    json_check(fileJSON)
    
    options = {'1':"start-single",
               '2':"start-online [Not yet]",
               '3':"profile",
               '4':"store",
               '5':"save & go-back-login-panel",
               '6':"quit",}
    
    
    for nums, opts in options.items():
        print(f"${nums}:{opts}")
    print()
    
    while True:
        userChoice = input("> ")
        
        if userChoice == '1':
            pass
        elif userChoice == '2':
            pass
        elif userChoice == '3':
            time.sleep(0.43)
            os.system('cls')
            return panels.profile_panel(userData)
        elif userChoice == '4':
            pass
        elif userChoice == '5':
            print("[saving..]\n")
            userData["isNew"] = "no"
            dataNew = {**userData}
            with open(fileJSON, 'w') as writeData:
                new_add = json.dump(dataNew, writeData, indent=4)
            time.sleep(.89)
            os.system('cls')
            return main.user_panel()
        
        elif userChoice == '6':
            print("[scriptto has stopped]")
            break
        
        else:
            print("[Invalid Argument]\n")
            time.sleep(0.43)
            os.system('cls')
            return start_menu()