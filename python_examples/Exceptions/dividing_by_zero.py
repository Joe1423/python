#How to handle errors, like dividing by 0 

print("Give me to numbers and i'll divide them.")
print("Enter 'q' to quit.")

active = True

while active:
    first_number = input("\nFirst number: ")
    second_number = input("\nSecond number: ")

    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("\nIt's not possible to divide by 0!")
    else:
        print("\nanswer: " + str(answer))

    again = input("\nWould you like to try again? (y/n) ")

    if again.lower() == 'n':
        active = False