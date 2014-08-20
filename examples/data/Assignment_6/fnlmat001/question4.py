# Matthew Finlayson - FNLMAT001 
# Assignment 6 question 3
# 22/04/14

marks = input("Enter a space-separated list of marks:\n")
marksList = marks.split(" ")

fail = 0 # variables to keep track of the num of each
third = 0
lower2 = 0
upper2 = 0
first = 0

# goes through each mark in the list and classifies it and adjusts the counter 
for i in range(len(marksList)): 
  mark = int(marksList[i])
  if mark >= 75:
    first+=1
  elif mark >= 70:
    upper2 +=1
  elif mark >= 60:
    lower2 +=1
  elif mark >= 50:
    third +=1
  else: fail +=1
  
#print(first, upper2, lower2, third, fail)
  
print("1 |"+"X"*first) # prints the histogram
print("2+|"+"X"*upper2)
print("2-|"+"X"*lower2)
print("3 |"+"X"*third)
print("F |"+"X"*fail)