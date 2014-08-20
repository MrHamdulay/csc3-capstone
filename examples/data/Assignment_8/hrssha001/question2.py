# Shane Horsley
# Program to check number of pairs in a string
# 5 May 2014
string = input("Enter a message:\n") #get string from user
def pair(x):
    z = len(x)
    if z == 1: #cant have a pair if length is 1
        return 0
    if z!=1 and z!=2:
        if x[0]==x[1]: #if first and second letters are the same, return the string from the 3rd character and 1 (like a count)
            x=x[2:]
            return 1 + pair(x)
        else: #if the second letter and first arent the same
            return pair(x[1:])
    else:
        if x[0]==x[1]: #for 2 characters
            return 1
        else:
            return 0
print('Number of pairs:',pair(string))

