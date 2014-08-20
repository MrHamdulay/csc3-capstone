"""Assignment 8- Question 2
Duncan Saffy
4 May 2014"""
def rep(x,count):
    n=0
    if n >= len(x)-1:
        return count
    elif x[n] == x[n+1]:
        return rep(x[n+2:],count+1)
    else:
        return rep(x[(n+1):],count)
    
x= input("Enter a message:\n")
count=0
print("Number of pairs:",rep(x,count))