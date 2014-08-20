#Saijil Nemchund
#NMCSAI001
#Question 2


count=0
def counting (word): 
    global count
    if word=='': #if the string is empty, there are no pairs hence 0 pairs are present 
        return count
    else:
        
        if(len(word)>1 and word[0]==word[1]): 
    
            count=count+1 #counts the number of strings repeated 
        
            return counting (word[2:len(word)])
        else:
            return counting (word[1:len(word)])

x=input("Enter a message:\n")      #Prompting the user for an input    
print("Number of pairs:",counting (x))