import json

try:
    with open('objects\\items_name.json', 'r') as items:
        item = json.load(items)
    with open('objects\\entities.json', 'r') as entities:
        entitiy = json.load(entities)
except FileNotFoundError:
    print("[Error finding objects folder && files]\n")
    
class combat:
    pass

class items:
    pass

class entities:
    pass
