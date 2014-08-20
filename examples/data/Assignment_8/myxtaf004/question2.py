"""Counts the numbers of repeated pairs in a loop
Tafadzwa Moyo
4 May 2014"""

#checks for pairs of characters
def check(string):
    if len(string)>1:
        x=check(string[1:]) #x takes the value of check(string[1:])
        if string[0]==x[0]:
            return ["",x[1]+1] #return a blank string and the number of repeatations +1
        else:
            return [string[0],x[1]] #returns the 1st letter of its string and the nummber of repeatation
    else:
        return [string[0],0]    

#input
string=input("Enter a message:\n")
print("Number of pairs:", check(string)[1])