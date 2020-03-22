#In order to make the function accepts an argument as optional you have to give it a default value as an empty string and defining how it must proceed in case that this argument was given or not

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return formatted name"""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name

    return full_name.title()


musician = get_formatted_name('John', 'Lee', 'Hooker')

print(musician)

actor = get_formatted_name('Joaquin', 'Phoenix')

print(actor)
