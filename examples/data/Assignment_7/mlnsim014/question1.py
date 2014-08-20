'''program list of strings without duplicates
Simangaliso Mlangeni
MLNSIM014
02 May 2014'''

#Function to acquire list of names from user
def getList():
    Lis = []
    str1 = input("Enter strings (end with DONE):\n")
    while str1 != 'DONE':
        Lis.append(str1)#appends name to the list
        str1 = input("")
    print()    
    return Lis

#invokes the fuction getList and stores list as data
data = getList()

#Function to print out unique list
def UniqueList():
    print("Unique list:") 
    modf = []#empty list to append unique names
    for i in data:
        if i in modf:#checks if name is in list and appends it if it is not
            continue
        modf.append(i)#appends unique names
    
    for j in modf:
        #prints out unique names
        print(j)

#calls fuction UniqueList
UniqueList()