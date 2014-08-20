#Ikhlaas Pohplonker
#23 April 2014
#a program that takes in a list of marks and outputs a histogram representation of the marks according to the mark categories at UCT
marks=input("Enter a space-separated list of marks:\n")
list_of_marks=marks.split(" ")#makes an array of marks
fail=[]
third=[]
lower_second=[]
upper_second=[]
first=[]
for i in list_of_marks:
    if eval(i)<50:
        fail.append(i)#add mark to fail 
    if 50<=eval(i)<60:
        third.append(i)#add mark to third
    if 60<=eval(i)<70:
        lower_second.append(i)#add mark to lower_second
    if 70<=eval(i)<75:
        upper_second.append(i)#add mark to upper second
    if 75<=eval(i):
        first.append(i)#add mark to first
print("1 |", len(first)*"X",sep="")#prints the numer of X's according to the number of marks that fell into the first category
print("2+|", len(upper_second)*"X",sep="")#prints the numer of X's according to the number of marks that fell into the upper_second category
print("2-|", len(lower_second)*"X",sep="")#prints the numer of X's according to the number of marks that fell into the lower_second category
print("3 |", len(third)*"X",sep="")#prints the numer of X's according to the number of marks that fell into the third category
print("F |", len(fail)*"X",sep="")#prints the numer of X's according to the number of marks that fell into the fail category

    