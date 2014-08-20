#kairav soni
#09/05/14
#Q2 Ass8

word=input("Enter a message:\n")
count=0

def counting(word):
    global count
    
    if len(word) > (1):
        
        
        if word[0]==(word[1]):
            count=(count+1)
            x=(counting(word[2:]))
            return (x)
        

        
        else:
            counting(word[1:])
            return (count)
        
        
    else:
        return (count)
    
    
num=counting(word)
print("Number of pairs:",num)