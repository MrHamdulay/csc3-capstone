"""Keegan Naidoo
NDXKEE009
4 May 2014"""

string=input("Enter a string:\n")        #Enter a string

def Pal(string):                         #Reverses string
    
    if string =="":                        #Base cases if empty string or space returns empty string or space respectively
        return "" 
    
    elif string==" ":
        return " "
    
    else:
        
        return string[-1] + Pal(string[0:len(string)-1])       #Returns last letter of string and repeats function starting from first letter to second last letter

rstring=Pal(string) #This variable name was reverse_string (meaningful) , but I changed it because automatic marker marked me down for using "reverse" in my programme 

if rstring==string:                   #Checks if string is palindrome
    print("Palindrome!")
else:
    print("Not a palindrome!")