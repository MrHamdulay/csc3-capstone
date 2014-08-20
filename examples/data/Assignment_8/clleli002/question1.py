"""check for palindrome
Elizabeth Cilliers
2014/05/05"""

def palin(string,count,strlength):
    #if the string length is zero or one letter long, it is a palindrome. Therefore true
    if len(string)<2: 
        return True
    
    if count==strlength:
        return True
    
    #if the first and last letter of the string are equal than remove those letters from the string then call function again.
    elif string[0]==string[-1]: 
        string= string[1:-1]
        count+=1
        return palin(string,count,strlength)
    
    
    else:
        return False
    

string=input("Enter a string:\n")
count=1
strlength=len(string)//2

if palin(string,count,strlength)==True:
    print("Palindrome!")
else:
    print("Not a palindrome!")
