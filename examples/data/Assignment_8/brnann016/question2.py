#Assingment 8-question 2
#Annika Brundyn
#count pairs of repeared characters in string

def count_pairs(message):
    if len(message)==0 or len(message)==1:
        return 0
    elif message[0]==message[1]:
        return 1+count_pairs(message[2:])
    else:
        return count_pairs(message[1:])
    
message=input("Enter a message:\n")
print("Number of pairs:",count_pairs(message))

