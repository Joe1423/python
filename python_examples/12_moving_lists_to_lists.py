#Users that need to be verified 

unconfirmed_users = ['maria', 'luis', 'john', 'estela', 'roberto']

#Confirmed users

confirmed_users = []

#Move each user from one list to the other 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print('Verificando al usuario ' + current_user)
    confirmed_users.append(current_user)

print('Done.')

print('The next users have been successfully verified:')
for user in confirmed_users:
    print(user)