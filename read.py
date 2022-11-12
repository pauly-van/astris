import json

def read():
  with open("/home/pauly/Documents/Code/astris/chars.json") as peeps:
    data = json.load(peeps)
  return data