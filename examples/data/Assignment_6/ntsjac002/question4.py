'''A program that that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT
Jacob Ntesang
22 April 2014'''

#Get the list of marks from the user 
Marks = input("Enter a space-separated list of marks:\n")
Marks = Marks.split(" ")
for i in range(0,len(Marks)):
    Marks[i] = eval(Marks[i])
#Go through the list 
First = 0
S_upper = 0
S_lower = 0
T = 0
F = 0
for i in Marks:
    if i < 50:
        F += 1
    elif 50 <= i < 60:
        T += 1
    elif 60 <= i < 70:
        S_lower += 1
    elif 70 <= i < 75:
        S_upper += 1
    else:
        First += 1
        
print("1 |"+"X"*First)
print("2+|"+"X"*S_upper)
print("2-|"+"X"*S_lower)
print("3 |"+"X"*T)
print("F |"+"X"*F)

