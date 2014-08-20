""" Charles Schleich-SCHCHA027
2014-May-01
"""
#program where the user can enter a list of strings and these strings are then printed in the same order but without duplicates.
def q1():
    opt=""
    listOfStrings =[]
    print("Enter strings (end with DONE):")
    while opt!= "DONE":
        opt = input("")
        if opt not in listOfStrings and opt != "DONE" :
            listOfStrings.append(opt)
    
    print("\nUnique list:")
    for i in range(len(listOfStrings)):
        print(listOfStrings[i])


if __name__== "__main__":
    q1()
    