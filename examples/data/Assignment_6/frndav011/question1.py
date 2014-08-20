#Create empty array/list
strings = []

#Get input
string = input("Enter strings (end with DONE):\n")
#Place input into list

if string.upper() == 'DONE':
    print("\nRight-aligned list:")
else:
    while string.upper()!= 'DONE':
        strings.append(string)
        string = input()
    #Determine the maximum number of places     
    maxL = max(map(len, strings))
    #Use for mat to right align strings
    right_align = ">{}".format(maxL)    
    
    #Prints out strings right aligned
    
    print("\nRight-aligned list:")
    for string in strings:
        print (format(string, right_align))