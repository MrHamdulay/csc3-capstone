#9 May 2014
#Program to count the number of pairs of repeated characters in a string
#LYLJON002

k = 0

def count(k, text):                         #function to count pairs
    if len(text) == 1 or text == '':        #return no pairs if 1 or no characters
        return k
    char1 = text[0]
    char2 = text[1]
    if char1 == char2:                  #compare two characters next to each other
        k = k + 1                       #increase count if they match
        return count(k, text[2:])       #run function on text missing the pair
    else:  
        return count(k, text[1:])       #if no pair then run function missing first letter

text = input("Enter a message:\n")  
print("Number of pairs:", str(count(k, text)), sep=' ')     #output