#deepak bhoojrajh
#question 2

count=0
def pairs(word):
    global count
    
    if word=='':
        return count

    else:
        
        if(len(word)>1 and word[0]==word[1]):
            count=count+1
            return pairs(word[2:len(word)])
       
        else:
            return pairs(word[1:len(word)])


x=input("Enter a message:\n")         
print("Number of pairs:",pairs(x))