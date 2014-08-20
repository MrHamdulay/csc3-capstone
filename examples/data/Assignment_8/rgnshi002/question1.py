#Shivam Ragoonaden
#RGNSHI002
#Program that uses recursion to check if a sentence inputted is a palindrome or not


string=input("Enter a string:\n")

def Pal(string):
            
    if string == "":  #Base case
        return ""
    
    elif string == " ":  #Return space
        return " "
    
    else:
        return string[-1] + Pal(string[0:len(string)-1])  #Return the last letter and call the function again with the last letter ommitted
    
x = Pal(string) #Assign the reversed string to x

if x == string:  #Compare the two to check if Palindrome
    print("Palindrome!")
else:
    print("Not a palindrome!")
