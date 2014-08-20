#vhrjoc001

#question 2 assignment 8

#making a program that counts the number of pairs in a strirng

def pairs(c): #paired letters , c for characters

    if len(c)<2:

        return 0

    elif c[0]==c[1]:

        return 1 + pairs(c[2:])

    else:

        return 0 + pairs(c[1:])

    

string=input("Enter a message:\n")

print("Number of pairs:",pairs(string))