#Gina Horscroft
#Question 2
#count number of double characters next to one another
#double = "same characters next to each other" ... hello has 1, mississippi has 3, wolverine has 0

def doubleChar(s):
    if len(s)<=1:
        return 0
    elif s[0] == s[1]:
        return 1 + doubleChar(s[2:len(s)])#take away those two equal characters -in cases such as where more than 2 consecutive equal letters
    else:
        return doubleChar(s[1:len(s)])
    
s = input("Enter a message:\n")
print("Number of pairs:", doubleChar(s))