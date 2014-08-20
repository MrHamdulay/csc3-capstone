def printer(words,l): # gets 2 parameters
    print("\nRight-aligned list:")
    for i in range (len(words)): #iterates the number of str in list
        space = l-len(words[i])
        print(" " * space + words[i])
        
        
def start():
    w = input("Enter strings (end with DONE):\n")
    words = []  ##mpty list for strings
    leng = len(w) # length of the input string
    while w != "DONE":    # stops iterating when w = DONE   
        words.append(w) #adds the input to the list
        w = input()   #gets the next input
        if leng < len(w):# ensures that the length sent back is the largest string
            leng = len(w)
    printer(words,leng) #calls printer function
start()