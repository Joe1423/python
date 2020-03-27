from name_function import get_formatted_name

print("Print q at anytime to quit.")

while True:
    first = input("\nYour first name: ")
    if first.lower() == 'q':
        break
    last = input("\nYour last name: ")
    if last.lower() == 'q':
        break

    formatted_name = get_formatted_name(first, last)

    print("\nNeatly formatted name: " + formatted_name)