"""Sphiwe Muthembi
   Std no: MTHSPH007
   Assignment 6 - Question 4
   program to create a histogram graph"""

#mark allocations
#fail< fail
#50% <= 3rd <60%
#60% <= lower 2nd < 70%
#70% ,=upper 2nd  < 75%
#75% <= 1st

#input marks:

mark = []
marks = input("Enter a space-separated list of marks:\n")

mark = marks.split(" ")         #Splitting marks

#counters to keep track off each condition
cnt1=0
cnt2=0
cnt3=0
cnt4=0
cnt5=0
countmain=0


#while countmain < len(mark):
for i in range(len(mark)):
     perc = eval(mark[i])
     if perc < 50:
          cnt1+=1
     elif 50<= perc < 60:
          cnt2+=1
     elif 60<= perc < 70:
          cnt3+=1
     elif 70 <= perc < 75:
          cnt4+=1
     else:
          cnt5+=1
    
print('1 |'+'X'*cnt5)
print('2+|'+'X'*cnt4)
print('2-|'+'X'*cnt3)
print('3 |'+'X'*cnt2)
print('F |'+'X'*cnt1)
    
        
    
        

