with open('sample.txt') as contenido:
    #readlines() crea una lista, y almacena en ella cada una de las lineas
    lines = contenido.readlines()

print(type(lines)) #returns list

for line in lines:
    print(line)

