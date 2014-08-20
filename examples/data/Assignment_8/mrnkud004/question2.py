"""counting number of pairs of repeated characters in a string
kennedy muranda
9/5/2014"""

#define the function
def count(s,c):#s=string and c=count
    if len(s)==0 or len(s)==1:
        return print("Number of pairs:",c)
    
    else:
        if s[0]==s[1]:
            c+=1
            return (count(s[2:len(s)],c))
        else:
            return (count(s[2:len(s)],c))
        print("Number of pairs:",c)
        
        
#prompt user to enter message
s = input("Enter a message:\n")
count(s,0)
