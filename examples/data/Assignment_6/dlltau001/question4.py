#Question4
#Assignment 6
#CSC1015F

marks = input("Enter a space-separated list of marks:\n").split()
#marks = eval(marks)
for i in range(len(marks)):
   marks[i] = eval(marks[i])
tally = [0,0,0,0,0]
for i in range(len(marks)):
   if marks[i] < 50:
      tally[4]+=1
   if marks[i] >= 50 and marks[i] < 60:
      tally[3]+=1
   if marks[i] >= 60 and marks[i] < 70:
      tally[2]+=1
   if marks[i] >= 70 and marks[i] < 75:
      tally[1]+=1
   if marks[i] >= 75:
      tally[0]+=1
        
for i in range(len(tally)):
      if i == 0: print("1 ",end='')
      elif i == 1: print("2+",end='')
      elif i == 2: print("2-",end='')
      elif i == 3: print("3 ",end='')
      elif i == 4: print("F ",end='')
      print("|",("X"*tally[i]),sep='')