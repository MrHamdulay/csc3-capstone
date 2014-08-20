""" Getting a list of strings and aligning to the right
danica van der zandt
24 april 2014"""

#get an input from the user and store it into the empty string
strings=[]

string=input("Enter strings (end with DONE):\n")
if string== "DONE":
    print("\nRight-aligned list:")
else:
    while string != "DONE":
        strings.append(string)
        string=input("")
    
    
    #get the max length of the strings entered
    max_length=max(strings, key=len)
    #print(max_length)
    int_max_length=len(max_length)
    #print(int_max_length)
    
    
    #return each string in a new ling but aligned to the right according to int_max_len
    print("\nRight-aligned list:")
    for string in strings:
        print(string.rjust(int_max_length))
