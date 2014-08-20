#counting the number of repeated characters in a string
#Anthony Jacob
#9 May 2014

#asking user to enter a message
s = input("Enter a message:\n")

def count_chr(s,c):#defining the function where s=string and c=count
    if len(s)==0 or len(s)==1:
        return print("Number of pairs:",c) 
    else:
        if s[0]==s[1]:
            c+=1
            return (count_chr(s[2:len(s)],c))
        else:
            return (count_chr(s[2:len(s)],c))
        print("Number of pairs:",c)
            
count_chr(s,0)   #calling the function