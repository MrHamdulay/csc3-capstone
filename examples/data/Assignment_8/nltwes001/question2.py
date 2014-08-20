#ASSIGNMENT 8
#QUESTION 2
#NLTWES001

test=input("Enter a message:\n")

def pairs(test):
    if len(test)<=1:
        return 0
    else:
        count=0
        if test[0]==test[1]:
            count= count+1
            return count + pairs(test[2:])
        else:
            return pairs(test[1:])

print("Number of pairs:", pairs(test))