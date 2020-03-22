#To remove and instance in a list by his value we can use remove() but this only works if the instance only appears once in the list. Let's see how to fix this:

pets = ['cat', 'fish', 'dog', 'squirrel', 'dog', 'bat', 'raccoon', 'dog']

count = 0
while 'dog' in pets:
    pets.remove('dog')
    count += 1

print('Se borraron ' + str(count) + ' ocurrencias.')