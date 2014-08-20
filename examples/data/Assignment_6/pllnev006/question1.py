#Program to input a list of names
#Nevarr Pillay - PLLNEV006
#22 April 2014

names = []
length = 0

def readIn(): #Reads in all the names until the sentinel "DONE"
    name = input("Enter strings (end with DONE):\n")
    while name != "DONE":
        names.append(name)
        name = input()
        
def longest(): #Determines the length of the longest name     
    global length
    for i in names:
        if len(i) > length:            
            length = len(i)
        
def output(): #Creates a right-aligned format template using the longest length and outputs all the names
    print("\nRight-aligned list:")
    align = "{0:>" + str(length) + "}"
    for i in names:
        print(align.format(i))
    
def main():
    readIn()
    longest()
    output()
    
if __name__ == "__main__":
    main()