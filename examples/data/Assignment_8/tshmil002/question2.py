#Program to check for pairs
#Mila Tshaka
#9 May 2014
x=input("Enter a message:\n")
def Pairs(rString,n,count):
    d=n+1
    if d > (len(rString)-1):
        return count
    elif(rString[n]==rString[d]):
        count=count+1
        return Pairs(rString,n+2,count)
    if(rString[n]!=rString[d]):
        return Pairs(rString,n+2,count)
print("Number of pairs:",Pairs(x,0,0))    