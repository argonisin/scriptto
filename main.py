import os, time, threading, json
from menu import start_menu

def user_panel():
    print("[WELCOME TO THE LOGIN/SIGN-UP PANEL!]\n")
    def log_in():
        print("[SCRIPTTO-LOG_IN_MENU]\n")
        print("Welcome to the log-in page!,\nPlease enter the correct details.\n\n")
        
        while True:
            userName = input("username: ")
            
            if userName:
                try:
                    fileName = f"player_{userName.lower()}.json"
                    with open(fileName, 'r') as user_data:
                        Udata = json.load(user_data)
                    for data in Udata["user-meta-data"]:
                        if userName == data["user_name"]:
                            while True:
                                password = input("password: ")
                                if password == data["password"]:
                                    print("\nWelcome in!")
                                    time.sleep(0.20)
                                    print("\nLoading script(to).game :)")
                                    time.sleep(3)
                                    os.system('cls')
                                    start_menu()                                    
                                    break
                                else:
                                    print("[Invalid password!]")
                        else:
                            print("[Invalid username!]") 
                except Exception:
                    print("[Invalid username!]")
                    time.sleep(0.43)
                    os.system('cls')
                    log_in()
                
                  
                break
            
    def sign_up():
        print("[SCRIPTTO-SIGN_UP_MENU]\n")
        print("Welcome to the sign-up page!,\nLet's have our humble beginnings with you.\n\n")
        
        json_metaData_format = {
            "user-meta-data": [
                {"user_name": None,
                 "password": None, 
                 "bio": None
                }
            ]
        }
        
        for data in json_metaData_format["user-meta-data"]:
            while True:
                userName = input("username: ")
                password = input("password: ")
                
                if userName:
                    data["user_name"] = userName
                if password:
                    data["password"] = password
                fileName = f"player_{userName}.json"
                
                with open(fileName, 'w') as newFile:
                    newFile = json.dump(json_metaData_format, newFile, indent=4)
                print(f"Succesfully Signed-Up! Check your json_account in the folder:\n[{os.path.dirname(os.path.abspath(__file__))}]")
                time.sleep(0.5)
                print("Enter your details on the log-in panel [wait for 2.4s]")
                time.sleep(2.4)
                os.system('cls')
                user_panel()
                break
                
                    
    options = {'lg':"log_in",
               'sg':"sign_up",
               'qt':"quit"}
    
    for cmd, opts in options.items():
        print(f"{cmd}:{opts}")
    print()
    
    run = True
    while run:
        user_cli = input(": ")
        
        if user_cli == 'lg':
            os.system('cls')
            log_in()
            break
        elif user_cli == 'sg':
            os.system('cls')
            sign_up()
            break
        elif user_cli == 'qt':
            print("See ya later!")
            break
        else:
            print("\ninvalid argument\n")
            time.sleep(0.43)
            os.system('cls')
            user_panel()
    
def sysCheck(json):
    pass

if __name__ == "__main__":
    user_panel()