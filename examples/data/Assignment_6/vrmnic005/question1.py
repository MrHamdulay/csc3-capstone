#VRMNIC005
#assignment 6 question 1

def right_aligned():
    """takes a set of strings and right aligns them with the longest string"""
    all_values = []

    value = input("Enter strings (end with DONE): \n")
    while value != "DONE":
        all_values.append(value)    #adds new values onto the end of the list
        value = input()

    print("\nRight-aligned list: ")
    if all_values != []:
        max_length = max(map(len, all_values))  #finds max length of the values in the list

        for value in all_values:
            print("{0:>{1}}".format(value, max_length)) #prints the strings right aligned by max length
    

right_aligned()

