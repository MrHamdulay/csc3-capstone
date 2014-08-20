"""program to count the number of pairs of characters in a string
Muhammad Nabeel Dulymamode
08/05/2014"""

def count_pair(string):
    if len(string) > 1:
        if string[0] == string[1]:
            return count_pair(string[2:]) + 1
        else:
            return count_pair(string[1:])
    else:
        return 0
    
msg = input("Enter a message:\n")
pairs = count_pair(msg)
print("Number of pairs:", pairs)