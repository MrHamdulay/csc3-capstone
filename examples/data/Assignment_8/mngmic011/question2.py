"""Assignment 8
Question 2
Micaela Menegaldo"""

def countingpairs(string):
    if len(string)==1:
        return 0
    elif string[0]==string[1]:
        if len(string)==2:
            return 1
        else:
            return 1 + countingpairs(string[2:])
    else:
        return countingpairs(string[1:])
    
        


if __name__=='__main__':
    message=input("Enter a message:\n")
    number=countingpairs(message)
    print("Number of pairs:", number)