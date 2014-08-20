#30 April 2014
#Program to return unique strings from a list
#LYLJON002

dicWords = {}           #initialising dictionary and list
arrUnique = []


string = input("Enter strings (end with DONE):\n") 

while string != "DONE": 
        if string in dicWords.keys():
                dicWords[string] = dicWords[string] + 1        #increase count
        else:
                dicWords.update({string : 1})           #add to dictionary keys
                arrUnique.append(string)                #add to list items
        string = input("")


print()
print("Unique list:")
for k in range(0, len(arrUnique)):
        print(arrUnique[k])             #output unique list