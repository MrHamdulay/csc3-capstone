#Thembekile Dubazana
#dbzphi002
#Assignment 8:Q1

"""Check if string is a palindrome"""

#Inputs and lower case string
string=input("Enter a string:\n")
string=string.lower()

#Function
def palin(string):
    if len(string)< 2:#This is where the palin will end
        return True
    else:
        if string[0]==string[-1]:#check first and last letters 
            return palin(string[1:-1]) #remove letters with each recursion
        else:
            return False
    
#Print result
if palin(string)==True:
    print("Palindrome!")
else:
    print("Not a palindrome!")
        

    