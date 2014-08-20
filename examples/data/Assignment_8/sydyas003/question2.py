#Yaseen Sayed Ismail
#SYDYAS003
#09/05/2014
#Checks for pairs of similar characters

def check(a):
    if(len(a)<=1):
        return 0
    else:
        if(a[0]==a[1]):
            return 1+check(a[2::])
        else:
            return 0+check(a[1::])
a=input("Enter a message:\n")
print("Number of pairs:",check(a))
