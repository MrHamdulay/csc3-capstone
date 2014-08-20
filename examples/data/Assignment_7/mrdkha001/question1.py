"""Program printing no duplicates
Khanyisile Morudu
27 April 2014"""


#initializing variables
arrString = []
arrString_nd = []               
string = input("Enter strings (end with DONE):\n")

#getting the data till done is typed
while string.upper()!= "DONE":
    arrString.append(string)
    string = input("")


#creating list without duplicates    
for i in range(len(arrString)):
    if arrString[i] not in arrString_nd:
        arrString_nd.append(arrString[i])

#printing it
print("\nUnique list:")
for i in range(len(arrString_nd)):
    print(arrString_nd[i])
    
        
        