import os, random, time
from main import user_panel

def start_menu():
    print("[SCRIPTTO alpha;0.11]\n\n")
    
    while True:
        enter = input("[enter to go back]")
        
        if enter:
            user_panel()