#Phumelele Ndimande
#Assingment 8

def pairs(string,letter):
#counts number of letter pairs in a string
    #ENDS IF STRING IS LESS THAN 2 CHARACTERS 
    if len(string) < 2:
        if letter == string and string != "": #If the first letter and the last letter of the previous recursion are equal 
            return 1
        else:
            return 0
#will only run if there are letters remaining 
    else:        
        pair = string[:2] #compares adjacent letters
        if pair[0] == pair[1]: #for identical letters
            return 1 + pairs(string[2:],"")
        elif letter == pair[0]: #If the firstnand last letter of the previous recursion are identical 
            return 1 + pairs(string[2:],"")
        else: #when not identical
            return 0 + pairs(string[2:],pair[1])
    
def main():
    message = input("Enter a message:\n")
    print("Number of pairs:", pairs(message,""))
    

main()
