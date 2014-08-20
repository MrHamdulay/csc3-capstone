"""Program that converts a list of strings to one without duplicates
JP Lanser
27 April 2014"""




string = input("Enter strings (end with DONE):\n") #Prompt user for input

the_list = [] 
while not string == "DONE": #Loop and add string to the list until user enters "DONE"
    if string not in the_list: #if the string is not in the list already, then add it to the list
        the_list.append(string)
    string=input()
    
    
print()
print("Unique list:")

for i in the_list: #loop through the list and print all the words
    print(i)
    