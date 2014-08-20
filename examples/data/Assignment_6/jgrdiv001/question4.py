"""PROGRAM THAT OUTPUTS A HISTOGRAM REPRESENTATION OF VOTES
DIVAN JAGERS
25 PARIL 2014"""
list_marks=input("Enter a space-separated list of marks:\n").split(" ") #prompts the user to enter a list of marks and automatically creates a list by separating th\ marks by a " "
fail=""      #categories of marks , empty at the moment but frequency will be addeed
third=""
l_second=""
u_second=""
first=""
for m in range(len(list_marks)):  # checks the grade and adds an X to each item of the respective grade categories
   
    if (int(list_marks[m])<50):       #If statements to place respective grades
        fail+="X"
    if (50<=int(list_marks[m])<60):
        third+="X"
    if (60<=int(list_marks[m])<70):
        l_second+="X"
    if (70<=int(list_marks[m])<75):
        u_second+="X"
    if (int(list_marks[m])>=75):
        first+="X"
print("1 |"+first)        #prints out the grades and frequency
print("2+|"+u_second)
print("2-|"+l_second)
print("3 |"+third)
print("F |"+fail)