#Kelly Goosen
#recursive function that counts the number of pairs of repeated chars in a string
#05/08/2014





def count_reps(s):
    
    if len(s)== 1:return 0 #go through all values in string length
    
    elif len(s)== 2:
        if s[0]== s[1]:return 1
        else:return 0
   
    elif s[0]== s[1]:return 1 + count_reps(s[2:]) #adding 1 and using recursion
    
    else:return count_reps(s[1:])


string = input("Enter a message:\n")
print("Number of pairs: "+ str(count_reps(string)))
