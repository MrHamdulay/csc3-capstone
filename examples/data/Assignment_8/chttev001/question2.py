"""Tevin Chetty
8 May 2014
Program to count number of pairs of characters"""

def count_pairs(string,count):
    if len(string)==0 or len(string)==1: #if only one or zero then there will be no pairs
        return print("Number of pairs:",count)
    else:
        if string[0]==string[1]: #checks adjacent letters if equal
            count+=1 #adds to the pair count
            return (count_pairs(string[2:len(string)],count)) #slices off letters already checked
        else:
            return (count_pairs(string[2:len(string)],count))#slices off letters already checked
    print("number of pairs:", count)
    
    
    
    
string=input("Enter a message:\n")
count_pairs(string,0)
