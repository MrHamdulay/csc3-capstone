"""Program to count the number of character pairs in a string (Question 2)
Jaren Hendricks
8 May 2014"""

# input statement
mes = input ("Enter a message:\n")

# Recursive formula to check character pairs
def pairs(mes):
    if len(mes)==1 or len(mes)==0:
        return 0
    elif mes[0] == mes[1]:
        return 1 + pairs(mes[2:])
    elif mes[0]!=mes[1]:
        return pairs(mes[1:])

# output statement
print ("Number of pairs:", pairs(mes))
