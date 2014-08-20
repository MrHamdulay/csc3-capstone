"""program to sort input list of marks according to UCT grading system
Mick Perring
25 April 2014"""

marks = input("Enter a space-separated list of marks:\n") # user inputs list of marks
list_1 = []
x = marks.split(" ")   # splits input marks into seperate values in a list (x)

for i in x:      # evaluates values in list x into integers and transfers them to mani list (list_1)
    y = eval(i)
    list_1.append(y)

# sets mark count for each grade at 0   
Fail = 0
Third = 0
SecLow = 0
SecUp = 0
First = 0
    
for i in list_1: # sorts and counts marks for each grade
    if i < 50:
        Fail += 1
    elif i < 60:
        Third += 1
    elif i < 70:
        SecLow += 1
    elif i < 75:
        SecUp += 1
    elif i >= 75:
        First += 1
        
print ("1 |{0}\n2+|{1}\n2-|{2}\n3 |{3}\nF |{4}"    # prints out no. of marks received for each grade
       .format(First*"X",SecUp*"X",SecLow*"X",Third*"X",Fail*"X"))
        