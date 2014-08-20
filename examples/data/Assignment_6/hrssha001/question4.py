# Program to count mark categories
#Shane Horsley
#20 April 2014
marks = input("Enter a space-separated list of marks:\n") # get marks
A=[] # list for each category of marks
B=[]
C=[]
D=[] 
E=[]
for i in marks.split(" "): # seperate string in to seperate marks
    i = int(i) # convert string to int to work with relational operators
    if i >= 75: #add the mark to the category list that it falls under
        A.append(i)
    if 70 <= i < 75:
        B.append(i)
    if 60<= i < 70:
        C.append(i)
    if 50 <= i < 60:
        D.append(i)
    if i < 50:
        E.append(i)
print("1 |"+len(A)*"X") #print x's for each item in a list
print("2+|"+len(B)*"X")
print("2-|"+len(C)*"X")
print("3 |"+len(D)*"X")
print("F |"+len(E)*"X")