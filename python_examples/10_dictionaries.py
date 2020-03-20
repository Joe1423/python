alien_0 = {'color' : 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

#Añadir más propiedades 

alien_0['position_X'] = 20
alien_0['position_Y'] = 40

print(alien_0)

#Eliminar una propiedad

del alien_0['color']

#########################
#RECORRER UN DICCIONARIO#
#########################

persona = {
    'nombre' : 'juan',
    'edad' : 26,
    'telefono' : 657987987,
    'direccion' : 'Calle Falsa 123',
    'profesión' : 'Administrador de sistemas'
    }

for key, value in persona.items():
    print('\nKey: ' + key + ', value: ' + str(value) + ';')

#Si sólo se necesita las llaves y no el valor se usa keys() en lugar de items()

print('El diccionario persona almacena los sgtes datos:')

for key in persona.keys():
    print(key + ': ' + str(persona[key]) + ';')

#Este es el comportamiento habitual por tanto escribir 'for key in persona' produce exactamente el mismo resultado que usando .keys()
    
if 'dni' not in persona.keys():
    print('No hay un dni asociado')

#obtener el dicccionario ordenado

for key, value in sorted(persona.items()):
    print('key: ' + key + ', value: ' + str(value) + ';')

########################
#LOOPING THROUGH VALUES#
########################

for value in persona.values():
    print(value)

#PARA EVITAR RESULTADOS REPETIDOS SE USA set()

favorite_languajes = {
    'ana' : 'Python',
    'charles' : 'Java',
    'Mary' : 'Php',
    'Lewis' : 'Python',
    'John' : 'Ruby',
    'Ollie' : 'Python'
    }

for value in set(favorite_languajes.values()):
    print(value)

#Only print python once


######################
#LIST OF DICTIONARIES#
######################

europe = {
    'France' : 'Paris',
    'Holland' : 'Amsterdam',
    'Spain' : 'Madrid',
    'United kingdom' : 'London',
    'Germany' : 'Berlin'
    }

america = {
    'Brazil' : 'Brazilia',
    'Argentina' : 'Buenos Aires',
    'Colombia' : 'Bogotá',
    'Perú' : 'Lima'
    }

asia = {
    'China' : 'Beijin',
    'Japan' : 'Tokyo',
    'South Korea' : 'Seoul'
    }

continents = [america, europe, asia]

print(continents[2])


########################
#A LIST IN A DICTIONARY#
########################

pizza = {
    'crust' : 'thick',
    'toppings' : ['cheese', 'onion', 'beef', 'mushrooms']
    }

print(pizza['toppings'])

#You can also make a dictionary inside other dictionary

users = {
    'mari25' : {
        'name' : 'Maria',
        'age' : 25
        },

    'TonyX' : {
        'name' : 'Anthony',
        'age' : 21
        }
    }

for user, data in users.items():
    print('\nUsername: ' + user)
    print('Name: ' + data['name'] + ', age: ' + str(data['age']))

