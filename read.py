import json

def read():
  with open("/home/pauly/Documents/Code/astris/data/chars.json") as file:
    data = json.load(file)
  return data

def write(decoded):
    with open("/home/pauly/Documents/Code/astris/data/chars.json", 'w') as file:
      file.write(json.dumps(decoded, sort_keys=True, indent=4, separators=(',', ': ')))

def update(function, alias, name):
    json_decoded = read()
    if function == "add":
      json_decoded[alias] = name
      write(json_decoded)
    elif function == "delete":
      del json_decoded[alias]
      write(json_decoded)
    elif function == "update":
      pass
  