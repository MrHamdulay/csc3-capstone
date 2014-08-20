"""Name: Sibulele Hlongwane
Date: 21 April 2014
Program: Separate a list of marks into categories depending on grade"""

#Prompts user to enter a list of marks
marks= input("Enter a space-separated list of marks:\n")
#Data inputted by user is then spilt and put into a list:
listofmarks= marks.split(" ")
#Creates empty lists
first=[]
uppersecond=[]
lowersecond=[]
third=[]
fail=[]

#Checks the elements of listofmarks, which are then seperated into a specific category depending on the mark, and "X" values are added to a list categorising the mark bounds
for a in listofmarks:
    if int(a)>=75:
        first.append("X")
    if (int(a)>=70) and (int(a)<75):
        uppersecond.append("X")
    if (int(a)>=60) and (int(a)<70):
        lowersecond.append("X")
    if (int(a)>=50) and (int(a)<60):
        third.append("X")
    if (int(a)<50):
        fail.append("X")
        
#prints the output of the histrogram, by joining the individual X elements in each respective list.   
print("1 |" + "".join(first))
print("2+|" + "".join(uppersecond))
print("2-|" + "".join(lowersecond))
print("3 |" + "".join(third))
print("F |" + "".join(fail))



        

    
    