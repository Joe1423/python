fruits = ['manzanas', 'peras', 'piña', 'uvas']

print(fruits)

print(fruits[-1]) #Returns el último elemento de la lista

fruits[1] = 'melocotones'  #Cambia peras por melocotones

#####################
#INSERTAR ELEMENTOS #
#####################

fruits.append('peras') #Añade peras al final de la lista

fruits.insert(3, 'fresas') #Añade en la posición 3 fresas

####################
#ELIMINAR ELEMENTOS#
####################

del fruits[1] #Elimina el elemento en la posición 1

popped_fruit = fruits.pop() #Saca el último elemento de la lista y lo guarda en popped_fruit

other_fruit_popped = fruits.pop(2) #Saca el que está en la posición 2 y lo guarda en la variable

fruits.remove('manzanas') #elimina el elemento de la lista cuyo valor sea manzana *Sólo elimina el primer elemento que coincida.

################
#ORDENAR LISTAS#
################

cars = [ 'bmw', 'lamborghini', 'ferrari', 'mercedez']

cars.sort() #ordena alfabeticamente los elementos de la lista

print(cars)

cars.sort(reverse=True) #Ordena alfabeticamente en orden inverso

sorted(cars) #Ordena la lista pero sin modificar el orden original

sorted(cars, reverse=True) #Lo mismo que sorted pero descendente

print(sorted(cars, reverse=True))

cars.reverse() #Invierte el orden original de la lista

######################
#LONGITUD DE LA LISTA#
######################

print(len(cars)) #returns 4, el número de elementos en la lista

###################
#RECORRER LA LISTA#
###################

for car in cars:
    print(car)  #Imprime cada uno de los elementos de la lista

##################
#LISTAS NUMÉRICAS#
##################

print(range(1,10)) #Impime los números de 1 a 9, el último valor no se incluye

for x in range(1, 35):
    print(x)


myNumbers = list(range(1,11))  #Crea una lista con los números del 1 al 10

print(myNumbers)

even_numbers = list(range(2, 21, 2)) #Crea una lista con los números del uno al 20 empezando por dos, el último dos indica que debe hacerlo de dos en dos a partir del valor inicial

print(even_numbers)


#GUARDAR LAS POTENCIAS(2) DE LOS PRIMEROS 10 NUMEROS:

al_cuadrado = []

for value in range(1, 11):
    al_cuadrado.append(value ** 2)


print(al_cuadrado)

#MÁXIMO
print(min(al_cuadrado)) #Devuelve el valor más pequeño de la lista

print(max(al_cuadrado)) #Devuelve el valor más grande de las lista

print(sum(al_cuadrado)) #Devuelve la suma de los valores de la lista


#La lista al_cuadrado también puede construirse en una misma linea de código por ejemplo:

al_cuadrado2 = [value**2 for value in range(1, 11)]

print(al_cuadrado2)


#un bucle que recorre sólo la segunda mitad de un array que tiene los números del 1 al 10

one_to_ten = []

for x in range(1, 11):
    one_to_ten.append(x)

for value in one_to_ten[5:]:
    print(value)


##################
#COPIAR UNA LISTA#
##################

mis_colores = ['azul', 'amarillo', 'rojo']

colores_favoritos = mis_colores[:]

print(colores_favoritos)