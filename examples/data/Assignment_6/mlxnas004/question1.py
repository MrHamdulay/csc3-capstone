"""nasha somoina meoli
24th april 2014
program to print a right-aligned listof words from a given list of words"""

def printrightalignedlist():
    # to tget the list
    x = input("Enter strings (end with DONE):\n")
    array = [x]
    while x != "DONE":
        
        x= input("")
        if x != "DONE":
            array.append(x)
        y =[]
        #to get the longest word and align the rest of the words accordingly
        for i in array:
            longest= len(i)
            y.append(longest)
        justify= max(y)
    print()
    print("Right-aligned list:")
    #to print right-aligned list
    if array!=["DONE"]:
        for i in array:
            i= (" "*(justify-len(i))+i)
            print(i)
        
printrightalignedlist()