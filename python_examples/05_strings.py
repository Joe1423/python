# myWord = 'ferrocarril'

# #Obtiene el número de caracteres
# len(myWord)

# #acceder a un carácter en particular 
# myWord[0] # f
# myWord[1] # e
# # ...
# #los ínidices negativos cuentan desde el final de la palabra:
# myWord[-1] # l
# myWord[-2] # i
# #...

# #slice un trozo de la palabra 
# myWord[1:4] # Desde el carácter 1 al 4  erro
# myWord[:2] # Del 0 al 2  fer
# myWord[:] # Toda la palabra

# #concatenación 
# myWord + ' volador' # ferrocarril volador

# #multiplicaición 
# myWord * 3 #la palabra ferrocarril 3 veces


# str() #cambia el tipo de dato a string

# list() #crea un array con los carácteres de un string

# ''.join() #une un array en una única cadena

# myWord.find('erro') #Busca estos caracteres dentro de la cadena devuelve la posición del primer carácter de la cadena a buscar

# myWord.replace('err', 'xyz') #Remplaza el primer argumento por el segundo dentro de una cadena fxyzocarril. No modifica el valor original de la cadena

# line = 'aaa,bbb,ccc,ddd'

# line.split(',') #separa la cadena tomando como delimitador el argumento ['aaa', 'bbb', 'ccc', 'ddd']

# myWord.upper() #covierte a mayúsculas FERROCARRIL

# myWord.lower() #convierte a minúsculas 

# myWord.isalpha() #Devuelve True si la variable esta compuesto sólo por letras

# myWord.rstrip() #Elimina espacios en blanco a la derecha

###################################################

name = 'juan mendez'

print(name.title()) #returns Juan Mendez

print(name.lower()) #returns juan mendez

print(name.upper()) #returns JUAN MENDEZ

###################################################

print('\t') #tabulación

print('\n') #nueva linea

###################################################

language = ' Python '

print(language.rstrip()) #returns Python sin el espacio a la derecha

print(language.lstrip()) #returns Python sin el espacio a la izquierda

print(language.strip()) #returns Python sin espacios ni al principio ni al final

###################################################

#No se pueden usar print con variables del tipo int o float hay que cambiarlos a string con el método str()

numero = 1955

print(str(numero))
