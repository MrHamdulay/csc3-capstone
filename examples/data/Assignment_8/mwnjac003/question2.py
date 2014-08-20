# program to count number of pairs repeated in a string 
# by Jacob Mwanza
# 06/05/2014

def check(word):
    counter = 0
    if len(word) == 1:
        return 0
    elif len(word) == 2:
        if (word[0] == word[1]):
            counter += 1
            return counter 
        else: 
            return counter
        
    else: 
        if (word[0] == word[1]):
            counter += 1
            return (counter + check(word[2:]))
            
        else:
            return (counter + check(word[1:]))
            
        
    
def main():
    word = input("Enter a message:\n")
    print("Number of pairs:",check(word))
    
main()