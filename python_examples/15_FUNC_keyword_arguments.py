def display_employee_info(name, profession):
    """Shows personal data about the given employee."""
    print('The employee ' + name + ' works at ' + profession + '.')

#display_employee_info('Juan', 'Systems management')

#The order matters if you don't want to mess it up you can provide the value for the arguments the following way:

display_employee_info(profession='Management of Systems', name='Juan')