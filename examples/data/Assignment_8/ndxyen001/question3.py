# Yentl Naidu (NDXYEN001)
# 8 May 2014
# Assignment 8
# Question 3 - Moving the letter to the next letter in order to encrypt it

def move(s,e):
    if(len(s)!=0): 
        if(s[0]=="z"): # Using "z" as the current letter
            e=e+"a" # "z" will become "a" if it's moved to the next position
            return move(s[1:],e)
        elif(97<=ord(s[0])<122): # Using ascii table, if using lower case letters
            e=e+chr(ord(s[0])+1) # Add the next letter to the encrypted letters
            return move(s[1:],e)
        else:
            e=e+s[0] # If it is not a lower case letter, just add the current letter
            return move(s[1:],e)
    else:
        return e
    
if __name__== "__main__":
    s=input("Enter a message:\n") # Get input to use in the function
    new=move(s,"")
    print("Encrypted message:\n",new,sep="")