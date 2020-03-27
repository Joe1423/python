import json

filename = 'scores.json'

with open(filename) as stuff:
    scores = json.load(stuff)

print(scores)
