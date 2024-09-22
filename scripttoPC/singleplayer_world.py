import random, os, time, json
from __init__ import *

for enemy in entity["enemy"]:
    for rock in enemy["rock"]:
        rockHP = rock["health"]
        rockDMG = rock["damage"]
    
print(f"rock: HP[{rockHP}] _ POSSIBLE DMG: {rockDMG}")
health = 100
while True:
    input(f"{health} __")
     
    if input == input:
        health = combat(rockDMG, health).healthDeduct()
        if health < 1:
            print("dead")
            break