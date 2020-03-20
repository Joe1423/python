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
    print(key)

#Este es el comportamiento habitual por tanto escribir 'for key in persona' produce exactamente el mismo resultado que usando .keys()
    
