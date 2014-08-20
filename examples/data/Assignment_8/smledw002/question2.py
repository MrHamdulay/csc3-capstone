#Author         : Edwin Samuels
#Student number : SMLEDW002
#Date           : 2014 - 05 -09
#Function       : counts duplicates in a string
#Title          : Question 1


def counter(string):
    """Counts the number of pairs in a string"""
    #converts a string into a list
    string = list(string)

    if len(string) <= 1:
        return 0
    #removes values to prevent overlapping pairs
    if string[0] == string[1]:
        string.remove(string[0])
        string.remove(string[0])
        return counter(string) + 1

    string.remove(string[0])
    return counter(string)


test_value = input("Enter a message:\n")
print("Number of pairs:", counter(test_value))



