#VRMNIC005
#Assugnment 7, question 1

def no_duplicates():
    strings = []
    new_string = input("Enter strings (end with DONE): \n")

    while new_string != "DONE":
        if new_string not in strings:
            # first occurrence of string is added to list
            strings.append(new_string)
        new_string = input()

    print("\nUnique list:")
    for string in strings:
        print(string)

no_duplicates()
