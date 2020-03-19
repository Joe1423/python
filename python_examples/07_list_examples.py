#Cuenta hasta 20

for numero in range(1, 21):
    print(numero)

#Crea una lista con los números de 1 a 1000000

one_to_million = []

for x in range(1, 1000001):
    one_to_million.append(x)

#print(one_to_million)

#el valor más pequeño de la lista

print(min(one_to_million))

#y el más grande

print(max(one_to_million))

#y la suma de todos los valores 

print(sum(one_to_million))


#Numeros impares de 1 a 20

odds_before_20 = []

for i in range(1, 21, 2):
    odds_before_20.append(i)

print(odds_before_20)


#múltiplos de 3 hasta 30

mult_3 = []

for s in range(1, 11):
    mult_3.append(3 * s)

print(mult_3)


#El cubo de los 10 primeros números con list_comprehension

first_10_cube = [value**3 for value in range(1, 11)]

print(first_10_cube)