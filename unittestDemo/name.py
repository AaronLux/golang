from name_function import get_formatted_name

print("Enter 'q' at any time to quite:")
while True:
    first = input("\nPlz give me a 1st name:")
    if first=='q':
        break
    last = input("\nPlz give me a last name:")
    if last=='q':
        break

    formatted_name = get_formatted_name(first,last)
    print(formatted_name)