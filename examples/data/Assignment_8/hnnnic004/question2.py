'''program to find pairs of repeated letters in string
nicole henning
due 9 may 2014'''

message = input("Enter a message:\n")
list_count = []

def rep_letters(message):
    index=0
    start = message[index]
    
    if len(message) == 1: #no reps if only one letter
        count = 0
        list_count.append(str(count))
    elif len(message) == 2: #when two letters, only rep if both are the same
        if (ord(start) == ord(message[1])):
            count = 1
            list_count.append(str(count))
        else:
            count = 0
            list_count.append(str(count))
    else:
        if (ord(start) == ord(message[1])): #if first letter is same as next, add 1 to list
            count=1
            list_count.append(str(count))
            #message starts at letter after rep
            return rep_letters(message[2:])
        else:
           #if no rep pair, start at next letter
            index+=1
            return rep_letters(message[1:])
    
    sum_reps = "+".join(list_count) #convert list into string resembling a sum of numbers
    answer = eval(sum_reps) #evaluate string of count created above
    print("Number of pairs:",answer)
        
rep_letters(message)        