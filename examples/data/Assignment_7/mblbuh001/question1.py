# question1.py
# Name: Buhlebezwe
# Student Number: MBLBUH001
# Date: 30 April 2014

list_string = []                                        #create list_string
string = input("Enter strings (end with DONE):\n")
while string != "DONE":                                 
    if string in list_string:                           #check and pass if string has already been entered
        pass
    else:
        list_string.append(string)                      #check and append if string has not been entered yet
    string = input ("")
    
print()
print("Unique list:")

for i in list_string:
    print(i)                                            #print unique list of strings