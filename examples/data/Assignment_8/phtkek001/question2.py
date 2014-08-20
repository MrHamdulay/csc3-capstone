"""Kekolo Phetla
phtkek001"""

string=input("Enter a message:\n")

def count_pairs(string):
    if len(string)<2:
        return 0
    elif string[0]==string[1]:
        return 1+ count_pairs(string[2:])
    else:
        return count_pairs(string[1:])
    
print("Number of pairs: ", end="")
print(count_pairs(string)) 