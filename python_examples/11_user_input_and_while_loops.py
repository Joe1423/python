name = input("What's your name?  ")

print('Hola ' + name + '!')

#Por defecto todo lo que se recibe de la función input() se toma como un string, si se quiere recibir un valor numérico hay que hacer la transformación con la función correspondiente, por ejemplo, para números se usa int()

edad = input('¿Cuántos años tienes?  ')

type(edad) #returns string

edad = int(edad)

if edad >= 18:
    print('Tienes edad suficiente para votar')
else:
    print('Aún no puedes votar')

#############
#WHILE LOOPS#
#############

contador = 1

while contador <= 5:
    print(contador)
    contador += 1


#using a flag

#this part of the program repeats what you say until you type 'quit'

prompt = 'Tell me a word? '

active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        #break tiene el mismo efecto
    else:
        print(message)


#continue hace que el bucle pase al siguiente ciclo. Este programa saca todos los números impares menores de 10

contador = 1
while contador <= 10:
    if contador % 2 == 0:
        continue
    else:
        print(contador)
        contador += 1


    