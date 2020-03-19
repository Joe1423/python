# import sys

# print(sys.platform)
# print(2**100)
# x = 'Spam!'
# print(x * 8)

#script con python:
#Primera linea ruta del intérprete

!/usr/bin/python

#OR 

!/usr/bin/env python    #Busca el intérprete de acuerdos a la configuración en las variables de entorno (forma recomendada)

#----------------------------

#Hacer que python ejecute un archivo en la misma sesión con reload()

from imp import reload

reload()  #Acepta como argumento un módulo ya cargado



#Acceder a un atributo de un modulo (variables, funciones, clases.. etc)

#objeto.atributo

import empleados          #copia el modulo entero y lo ejecuta aquí

print(empleados.empleado1)

#OR 

from empleados import empleado1   #(copia los nombres)

print(empleado1)

# > Juan


#La función dir muestra todos los atributos dentro del módulo

dir(emplados)

exec(open('miScript.py').read())  #ejecuta un script directamente "copia" el código del script para ejecutarlo aquí. (downside) Puede sobrescribir variables existentes en el script actual. Mejor usar import

