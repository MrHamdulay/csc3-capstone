#A program that uses a recursive function to count the number of pairs of repeated characters in a string.

#Make count equal to zero first
count=0

def pairs(phrase):
    global count
    if len(phrase)<=1:
        print(count)
    elif phrase[0]==phrase[1]:
        count = count+1
        return pairs(phrase[2:])
    else:
        return pairs(phrase[2:])
    
#Get the message from the user
phrase = input("Enter a message:\n")
#Print out the number of pairs within the given message 
print("Number of pairs: ",end ="")
pairs(phrase)