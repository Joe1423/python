import json

highest_scores = { 
    'Mary' : 400,
    'John' : 350,
    'Helen' : 270
    }

filename = 'scores.json'

with open(filename, 'w') as memory:
    json.dump(highest_scores, memory)

print('Los datos se han almacenado')