#Darryl Gounden
#Checks for pairs of occurances of letters in a string

word = input("Enter a message:\n")
count = 0

def counting(word):
    global count
    
    if len(word)>1:
        if word[0] == word[1]:
            count +=1
            return counting(word[2:])

        
        else:
            counting(word[1:])
            return count
        
    else:
        return count
    
    
x = counting(word)

print("Number of pairs:",x)