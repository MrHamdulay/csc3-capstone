"""check if palindrome using recurrsion
 Roger Cox
 6/05/14"""
# set a global variable
x=0
def strings (string):
    global x
    if (len(string))/2>=1  : #only if the string is not in the centre stopping point
        
        if string[0]==string[-1] : #first char = last Char
            
            strings(string[1:-1]) # recursion of smaller string
        
        else :    
            x+=1   # global variable changed if not a palindrome

def palindrome ():
    string=input("Enter a string:\n")
    strings(string)
    global x
    if x==0 :
        print("Palindrome!")
    else :  
        print ("Not a palindrome!")
palindrome()
