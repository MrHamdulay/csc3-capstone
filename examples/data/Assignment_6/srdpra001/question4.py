'''
Prashanth Sridharan
SRDPRA001
Assignment 06
Question 04
'''
marks = map (int, input ("Enter a space-separated list of marks:\n").split(" ")) #inputting the marks seperated by spaces, hence the split function.
counts = [0] * 5 #intialising a counter 
for m in marks: #m is the variable for mark
   
   if m>=75:
      i = 0
   elif m>=70:
      i = 1
   elif m>=60:
      i = 2
   elif m >= 50:
      i = 3  
   else:
      i=4
   counts[i] = counts[i] + 1

labels = ["1 ", "2+", "2-", "3 ", "F "] #the corresponding grades
for i in range (len (counts)): #repeating for all inputs
   print (labels[i] + "|" + "X" * counts[i]) #outputting an 'X' for the number of times each grade is repeated.