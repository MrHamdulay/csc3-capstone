# program to create dictionary of strings from a list
# by Jacob Mwanza
# 27/04/2014


def dict1():
    
    
    dictionary = []
    
    
    # collect strings
    word = input("Enter strings (end with DONE):\n")
    while word != 'DONE':
        dictionary.append(word)        
        word = input()
        
    dictionary2 = []
    print()
    print("Unique list:")
    # add unique strings    
    for name in dictionary:    
        if name not in dictionary2:
            dictionary2.append(name)
    
    # print contents of unique list
    for i in range(len(dictionary2)):
        print(dictionary2[i])
    
dict1()