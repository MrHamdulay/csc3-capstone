#Program to count number of repated pairs in a string using recursion
#Nevarr Pillay - PLLNEV006
#4 May 2014

def pairs(word,letter):
    """Counts the number of pairs of letters in string"""
    #Ends when the string is less than 2 characters
    if len(word) < 2:
        if letter == word and word != "": #If the first letter and the last letter of the previous recursion are equal 
            return 1
        else:
            return 0
    #Runs if there are letters left
    else:        
        pair = word[:2] #Looks at the two adjacent letters
        if pair[0] == pair[1]: #If letters are equal
            return 1 + pairs(word[2:],"")
        elif letter == pair[0]: #If the first letter and the last letter of the previous recursion are equal 
            return 1 + pairs(word[2:],"")
        else: #If not equal
            return 0 + pairs(word[2:],pair[1])
    
def main():
    message = input("Enter a message:\n")
    print("Number of pairs:", pairs(message,""))
    
if __name__ == "__main__":
    main()