count=0
def county(word):
    global count
    if word=='':
        return count
    else:
        
        if(len(word)>1 and word[0]==word[1]):
    
            count=count+1
        
            return county(word[2:len(word)])#If there is a pair, take out the 2 letters
        else:
            return county(word[1:len(word)])#if there is no pair, just remove the 1

x=input("Enter a message:\n")         
print("Number of pairs:",county(x))
