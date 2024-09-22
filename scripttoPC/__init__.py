import json,random

try:
    
    
    with open('objects\\items_name.json', 'r') as items:
        global item
        item = json.load(items)
    with open('objects\\entities.json', 'r') as entities:
        global entity
        entity = json.load(entities)
except FileNotFoundError:
    print("[Error finding objects folder && files]\n")
    
class combat:
    def __init__(self, damage : list[int], health :int):
        self.damage = damage
        self.health = health
        
    def healthDeduct(self):
        deduction = random.randint(self.damage[0], self.damage[1])
        return (self.health - int(deduction))

class items:
    pass

class entities:
    pass
