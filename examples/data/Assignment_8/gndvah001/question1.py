"""recursion palindrome
Vahin Gounden
2014-05-07"""

def main():
    word = input("Enter a string:\n")
    w = len(word)
    wle = w//2      
    counter = 0
    counter2 = w-1 
    x = 0
    palin(word,wle,counter,counter2,x)
       
 
def palin(word,wle,counter,counter2,x): 
    if counter <= wle:
        if word[counter] == word[counter2]:
            palin(word,wle,counter + 1,counter2 - 1,x + 1)
    if counter > wle or word[counter] != word[counter2]:
        if x > 0:
            print("Palindrome!")
        else:
            print("Not a palindrome!")    
        
            
main()
