#Thiolan Prevan Naidoo
#NDXTHI031
#question2 
#Check for the number of pairs of characters in a string using recursion



count=0
def pair(word):
    global count#ensures the count function can be used throughtout the function even wthout it being initialised wthin the function
    if word=='':
        return count
    else:
        
        if len(word)>1 and word[0]==word[1]:#checks if the first and second characters in the string recieved by the pair function are the same
            count+=1
            return pair(word[2:len(word)])#sends the string without the first two characters back into the pair function
        else:
            return pair(word[1:len(word)])#sends the string without the first character back into the pair function

x=input("Enter a message:\n")         
print("Number of pairs:",pair(x))
