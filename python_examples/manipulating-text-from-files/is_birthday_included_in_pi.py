filename = 'first_100000_digits_of_pi.txt'

active = True

while active:
    with open(filename) as pi_digits:
        lines = pi_digits.readlines()

    pi_string = ''

    for line in lines:
        pi_string += line

    print("\nLet's see if your birthday appears in the first 100000 digits of pi\n")

    birthday = input('Insert you birthday in the form mmddyy : ')

    if birthday in pi_string:
        print('\nHell yeah it appears \n')
    else:
        print('\nNah, it doesnt appear\n')

    repeat = input("Do you want to try again? (y/n)")

    if repeat.lower() == 'n':
        active = False   