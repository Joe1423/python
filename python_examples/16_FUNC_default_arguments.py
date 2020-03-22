def describe_pet(name='pet_name', type='animal'):
    """Describes your pet."""
    print('I have a ' + type + ' and his name is ' + name)

#In case you call the function with no arguments it will display the default values in the definition

describe_pet()

describe_pet(type='reptile', name='Lewis')