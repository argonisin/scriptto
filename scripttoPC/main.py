import os, time, json
import menu, style_metadata
from string import punctuation

class user:
    
    def sign_up():
        print("[SCRIPTTO-SIGN_UP_MENU]\n")
        print("Welcome to the sign-up page!,\nLet's have our humble beginnings with you.\n\n")
        
        gps = time.localtime()
        date = time.strftime("%D", gps)
        json_metaData_format = {
            "isNew": "yes",
            "user-meta-data": [
                {"user_name": None,
                 "password": None, 
                 "bio": None,
                 "joined_date": date
                }
            ]
        }
        
        for data in json_metaData_format["user-meta-data"]:
            while True:
                userName = input("username: ")
                password = input("password: ")
                
                if userName:
                    userList = [i for i in userName]
                    for i in range(len(userList)):
                        punc = [i for i in punctuation]
                        
                        if userList[i] in punc or ' ' in userList:   
                            print("\n[Special characters and spaces are not allowed]")
                            time.sleep(.67)
                            os.system('cls')
                            return user.sign_up()
                    
                    data["user_name"] = userName
                    if password:
                        data["password"] = password
                    fileName = f"accounts\\player_{userName.lower()}.json"
                    
                    with open(fileName, 'w') as newFile:
                        newFile = json.dump(json_metaData_format, newFile, indent=4)
                
                print(f"Succesfully Signed-Up! Check your json_account in the folder:\n[{os.path.dirname(os.path.abspath(__file__))}]")
                time.sleep(0.5)
                
                print("Enter your details on the log-in panel [wait for 2.4s]")
                time.sleep(2.4)
                os.system('cls')
                return user_panel()
            
                
    def log_in():
        log_in = user.log_in
        def userJsonCheck(user):
            try:
                fileName = f"accounts\\player_{user.lower()}.json"
                with open(fileName, 'r') as user_data:
                    Udata = json.load(user_data)
                menu.json_check(fileName)
                            
                for data in Udata["user-meta-data"]:
                    if user == data["user_name"]:
                                
                        while True:
                            password = input("password: ")
                                    
                            if password == data["password"]:
                                print("\nWelcome in!")
                                time.sleep(0.20)
                                
                                print("Loading script(to).game :)")
                                time.sleep(3)
                                os.system('cls')
                                return menu.start_menu()
                                
                            else:
                                print("[Invalid password!]")
                    else:
                        print("[Invalid username!]\n")
                        time.sleep(0.67)
                        os.system('cls')
                        return log_in()
                                
            except Exception as e:
                print("[Invalid username!]", e)
                time.sleep(0.67)
                os.system('cls')
                return log_in()
            
        print("[SCRIPTTO-LOG_IN_MENU]\n")
        print("Welcome to the log-in page!,\nPlease enter the correct details.")
        print("To exit type [;]\n\n")
        
        while True:
            userName = input("username: ")
            
            if userName == ';':
                time.sleep(0.67)
                os.system('cls')
                return user_panel()
            if userName:
                userJsonCheck(userName)
                break
            
def user_panel():
    style_metadata.style.logo()
    print("[WELCOME TO THE LOGIN/SIGN-UP PANEL!]\n")
                 
    options = {'lg':"log_in",
               'sg':"sign_up",
               'qt':"quit"}
    
    for cmd, opts in options.items():
        print(f"{cmd}:{opts}")
    print()
    
    while True:
        user_cli = input(": ")
        
        if user_cli == 'lg':
            os.system('cls')
            return user.log_in()
        elif user_cli == 'sg':
            os.system('cls')
            return user.sign_up()
            
        if user_cli == 'qt':
            print("See ya later!_scriptto has stopped")
            break
        else:
            print("\n[Invalid Argument]")
            time.sleep(0.43)
            os.system('cls')
            return user_panel()

if __name__ == "__main__":
    user_panel()