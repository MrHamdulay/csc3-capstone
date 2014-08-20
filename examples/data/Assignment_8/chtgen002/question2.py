"""CHTGEN002
09/05/2014
Number of pairs"""

def count_pairs (sentence): #function
    
    if (len(sentence)<=1): #if 1 character or less, no pairs
        return 0
    
    else:
        if (sentence[0]==sentence[1]): #1st character = 2nd character
            return 1+count_pairs(sentence[2::])
        else:
            return 0+count_pairs(sentence[1::])
        
sentence=input("Enter a message:\n") #input of sentence

print("Number of pairs:", count_pairs(sentence)) #recursion occurs here