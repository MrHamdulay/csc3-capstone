"""Count number of repeated characters in a string
Kiara Ramjith
May 2014"""
def char(s,p):
    if(len(s)>=2): #when there is more than 2 characters
        if(s[0]==s[1]): #if the 1st 2 are =
            return char(s[2:],p+1) #increase p by 1 and redo
        else:
            return char(s[2:],p)#redo function
    elif(len(s)==1):
        return p
    else:
        return p #just return p
    
if __name__=="__main__":
    s=input("Enter a message:\n")
    num= char(s,0)
    print("Number of pairs:",num)
    