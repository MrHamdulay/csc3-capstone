"""Question 4, Assignment 6
Tejasvin Bagirathi BGRTEJ001"""

#user inputs marks
marks=input("Enter a space-separated list of marks:\n")

#Convert marks to integers
marks=marks.split()
for i in range(len(marks)):
       marks[i]=eval(marks[i])
       
#Declare counter variables for each category
first = 0
upsecnd = 0
lowsecnd = 0
third = 0
fail = 0
    
#Place marks in list into catagories.
for i in marks:
       if i >= 75:
              first += 1
       elif i >= 70:
              upsecnd += 1
       elif i >= 60:
              lowsecnd += 1
       elif i >= 50:
              third += 1
       else:
              fail += 1
            
#Print out histogram using 'X'
print("1 |", "X"*first, sep = "")
print("2+|", "X"*upsecnd, sep = "")
print("2-|", "X"*lowsecnd, sep = "")
print("3 |", "X"*third, sep = "")
print("F |", "X"*fail, sep = "")
