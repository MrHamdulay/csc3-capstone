#29/04/2014
#ASSIGNMENT 7
#QUESTION 1
#WHTBAS001
#THOMAS WHITEHEAD


def remove_duplicates(x):
    i = len(x)-1 #in order to loop the normal way round
    x.reverse() #reverse the list
    while 0 <= i: #stops when at last char.
        j=len(x)-1
        while i < j:
            if x[j] == x[i]:
                x.remove(x[i]) #removes if it comes up later
                break
            j-=1 #iterates
        i-=1 #iterates
    x.reverse() #reverse back!
    print()
    print("Unique list:")
    for i in x: #prints each item individually
        print(i)
    

#get input section
words = list()
word = input('Enter strings (end with DONE):\n') # initalize before the loop
while word != 'DONE':           # while NOT DONE
    words.append(word) #adds the new string
    word = input('')  #resets loop

remove_duplicates(words) #call function
