#Write a program that takes in a list of marks and outputs a histogram representation of the marks according to the mark categories at UCT.
#BRXCAI001
#25 April 2014


#Get a list of marks.
mark = input("Enter a space-separated list of marks:\n")
list_marks = mark.split(' ')

#Create empty lists of the classes of the grades.
fail = 0
third = 0
lower2nd = 0
upper2nd = 0
first = 0

for mark in list_marks:
    actualmark = eval(mark)
    if actualmark < 50:
        fail+= 1
    elif actualmark < 60:
        third+=1
    elif actualmark < 70:
        lower2nd+=1
    elif actualmark < 75:
        upper2nd+=1
    else:
        first+=1
print("1 |","X"*first, sep ='')
print("2+|","X"*upper2nd, sep='')
print("2-|","X"*lower2nd, sep='')
print("3 |","X"*third, sep='')
print("F |","X"*fail, sep='')


        
        
        


   


