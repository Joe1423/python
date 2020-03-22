#Fill a dictionarie with answers taken from poll

responses = {}

ask_fruit = "What's your favourite fruit? "
ask_name = "What's your name? "
ask_next_person = "Would you like to invite a friend to take the poll? (y/n)"

poll_active = True

while poll_active:
    name = input(ask_name)
    fruit = input(ask_fruit)

    #Save into dictionarie
    responses[name] = fruit

    #will be another user?
    next_user = input(ask_next_person)

    if next_user.lower() == "n":
        poll_active = False


print('\nPolling is complete. These are the results: ')
for name, fruit in responses.items():
    print(name + ' said his/her favorite fruit is ' + fruit)


