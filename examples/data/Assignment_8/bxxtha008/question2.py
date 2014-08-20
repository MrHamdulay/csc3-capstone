'''program to using recursion to count no. of pairs of repeated characters in string
Thabiso Beau
4 May 2014
Assignment 8: #question2.py'''

x=input('Enter a message: \n')
count = 0 #setting a counting variable
def pairs(x):
    if len(x) <2: #if it's less than 2, then it's simply a letter
        return count
    if x[0] == x[1]: #if the 1st letter is equal to the 2nd one
        return 1 + pairs(x[2:])
    #increase by 1 every time the statement is true
    else:
        return pairs(x[1:]) #continue the slicing operation from the 2nd letter now, if equality is False 
        
print('Number of pairs:', pairs(x))
pairs(x)