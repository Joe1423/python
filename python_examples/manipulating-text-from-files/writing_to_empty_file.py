#openning a file in write mode adding 'w', to open() method as second argument

filename = 'sample.txt'

with open(filename, 'w') as content:
    content.write('Hola mi nombre es Juan\n')
    content.write('and im learning python\n')

#if you use 'a' instead of 'w' the content will be appended to the file instead

with open(filename, 'a') as content:
    content.write('Esta linea se añadió después\n')
    content.write('y esta también\n')

#read the file

with open(filename) as text:
    texto = text.read()
    print(texto)
