'''Sohail Tulsi
TLSSOH001
a count the number of times letters are ittirated next to each other'''

count=0
x=input("Enter a message:\n")    #user input message     

#check the number or times letters are placed next to each other in the message
def county(word): 
    global count
    if word=='':
        return count

    else:
        if(len(word)>1 and word[0]==word[1]):
            count=count+1
            return county(word[2:len(word)])

        else:
            return county(word[1:len(word)])


print("Number of pairs:",county(x))