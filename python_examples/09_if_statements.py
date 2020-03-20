cars = ['ferrari', 'lamborghini', 'bmw', 'bugatti']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

###############################
#EVALUAR MULTIPLES CONDICIONES#
###############################

name = 'Juan'
age = 26

if age == 26 and name == 'Juan':
    print("Hola mi nombre es " + name + " y tengo " + str(age) + " años.")

if age == 18 or age == 26:
    print(name + " es mayor de edad")


########################################
#VER SI UN ELEMENTO EXISTE EN UNA LISTA#
########################################

cars = ['ferrari', 'lamborghini', 'bmw', 'bugatti']

'ferrari' in cars #returns True

'Honda' in cars #returns False

#Si no existe en una lista:

if 'mercedes' not in cars:
    print('mercedes no está en la lista de coches')
else:
    print('mercedez si está en la lista.')

##############
#IF-ELIF-ELSE#
##############

#No siempre se requiere el bloque ELSE

frutas = ['fresas', 'duraznos', 'naranjas']

if (frutas[0] == 'naranjas'):
    print('No me gustan las naranjas')
elif(frutas[1] == 'naranjas'):
    print('Me gusta desayunar naranjas')
else:
    print('La mejor fruta son las naranjas')

#Returns 'La mejor fruta son las naranjas'



###################################
#COMPROBAR SI UNA LISTA ESTÁ VACÍA#
###################################

jugadores= []

if jugadores:
    print('Ahora mismo hay ' + len(jugadores))
else:
    print('No hay nadie jugando ahora mismo')


#OTRO EJEMPLO

toppings_availables = ['queso', 'pepperoni', 'setas', 'carne picada', 'verdura']

requested_toppings = ['queso', 'setas', 'piña', 'carne picada', 'jamón']

for requested_topping in requested_toppings:
    if requested_topping in toppings_availables:
        print('Añadiendo ' + requested_topping)
    else:
        print('Lo sentimos, no nos queda ' + requested_topping)


