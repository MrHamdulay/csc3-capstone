#kairav soni
#9/05/14
#Q1 Ass8

def convert(word):
    
    if len(word)>(1):
        
        if word[0]==word[-1]:
            x=convert(word[1:-1])
            return (x) 
        
        
        else:
            y=("Not a palindrome!")
            return (y)
        
        
    elif len(str(word))<=(1):
        z=("Palindrome!")
        return (z) 
    


if __name__=="__main__":
    word=input("Enter a string:\n")
    print(convert(word))
    
    