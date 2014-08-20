#Program to output a list of unique inputted words 
#Nevarr Pillay - PLLNEV006
#1 May 2014

#List that will contain the words
words = []

def readIn(): 
    """Reads in all unique words until the sentinel DONE"""
    word = input("Enter strings (end with DONE):\n")
    count = 0
    while word != "DONE":
        check = True
        for i in words:      
            if i == word:
                check = False
        #If the word has not been entered before, it is added to the list of words        
        if check == True:
            words.append(word)
        word = input()           
        
def output(): 
    """Outputs all the words in order"""
    print("\nUnique list:")
    for i in words:
        print(i)
    
def main():
    readIn()
    output()
    
if __name__ == "__main__":
    main()