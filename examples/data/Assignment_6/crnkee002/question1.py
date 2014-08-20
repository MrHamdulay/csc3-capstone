"""A5Q1 - Right aligning an array
20/04/2014
CRNKEE002"""

def main():
    get_list()
    align_list()
    print_list()

#set the empty array    
NameArray=[]

#get the list of names    
def get_list():
    global NameArray
    print("Enter strings (end with DONE):")
    name = ""
    while name.upper() != "DONE":        
        NameArray.append(name)
        name = input()
        
#align the list    
def align_list():
    global NameArray
    longest = 0
    
    #get the longest name
    for i in range(len(NameArray)):
        if len(NameArray[i]) > longest:
            longest = len(NameArray[i])
            
    #align all the names
    for i in range(len(NameArray)):
        current = len(NameArray[i])
        NameArray[i] = "{0: >{space}}".format(NameArray[i], space = longest)
    
#print the array    
def print_list():
    print("")
    print("Right-aligned list:")
    #iterate through the array
    for i in range(1, len(NameArray)):
        print(NameArray[i])
    
#choose whther to run the program or not
if __name__ == "__main__":
    main()