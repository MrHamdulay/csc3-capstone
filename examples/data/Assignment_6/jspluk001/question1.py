# Luke Joseph
# Question 1 of assignment 6
# 2014-04-20
def right():
    print("Enter strings (end with DONE):")
    x = []
    y=""
    a=0
    while y != "DONE": #gaining sequence of strings
        y=input("")
        x.append(y)
    longest = ""
    lt=x[0]
    r=lt #variables used in loops
    for j in range(len(x)): #loop to check for longest string of list
        lt=x[0]
        a=0
        if len(r)>len(x[j+a]):
            a+=1
        else:
            r=(x[j+a])
            a+=1
    formats = '{:>'
    formats = formats + str(len(r)) + '}' #formatting variable
    print("\nRight-aligned list:")
    for i in range(len(x)-1): # loop printing new list that has been right aligned
        print(formats.format(x[i]))
        a+=1    
right()
    
