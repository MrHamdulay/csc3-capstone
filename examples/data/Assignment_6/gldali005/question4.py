#a program that takes in a list of marks (separated by spaces) and outputs a histogram representation of the marks according to the mark categories at UCT:
#Ali Goldstein
#23 April 2014

#prompt the user to enter a list of marks, seperated by a space
marks=input("Enter a space-separated list of marks: \n")
mark=marks.split(" ")

#making variables for the different categroies
fail=0
third=0
lower2nd=0
upper2nd=0
first=0

#searching through the marks
#counting the number of marks that satisfy the conditions of each category.
for i in range (len (mark)):
      if int(mark[i]) < 50:
            fail += 1
      elif int(mark[i])>=50 and int(mark[i])<60:
            third+=1
      elif int(mark[i])>=60 and int(mark[i])<70:
            lower2nd+=1
      elif int(mark[i])>=70 and int(mark[i])<75:
            upper2nd+=1
      elif int(mark[i])>=75:
            first+=1
            
#displaying the results in horizontal bars to represent a histogram     
print("1 |" , first*'X', sep= "")
print("2+|" , upper2nd*'X', sep="")
print("2-|" , lower2nd*'X', sep="")
print("3 |" , third*'X', sep="")
print("F |" , fail*'X', sep="")
               
          
        
    
