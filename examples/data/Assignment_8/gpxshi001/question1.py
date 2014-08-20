"""
-GPXSHI001
-Ass8
-Q1

"""

stuff=input("Enter a string:\n")

def palindromic(stuff):
    
    if stuff =="":    
        return ""
    
    elif stuff==" ":
        return " "
    
    else:
        
        return stuff[-1] + palindromic(stuff[0:len(stuff)-1])

x= palindromic(stuff)

if x==stuff:
    
    print("Palindrome!")
else:
    print("Not a palindrome!")