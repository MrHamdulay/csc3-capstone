# program to do basic vector calculations in 3 dimensions: addition, dot product and normalization.
# Mulisa Badugela
# 20 April 2014

def marks(): 
     A=[]   # create empty list for each condition
     B=[]
     C=[]  
     D=[]
     F=[]
     
     # user input list of marks
     n=input('Enter a space-separated list of marks:\n')
     
     # insert each user input to its corresponding list using a  for loop
     for i in n.split(): 
          if eval(i) >= 75:
               A.append(i)
          elif 70<=eval(i)<75:
               B.append(i)
          elif 60<=eval(i)<70:
               C.append(i)
          elif 50<=eval(i)<60:
               D.append(i)
          elif eval(i)<50:
               F.append(i)
               
     # Find the total number of items in each list   
     a=len(A) 
     b=len(B) 
     c=len(C) 
     d=len(D)
     f=len(F)     
     
     # print out the histogram
     print("1 |"+'X'*a)  
     print("2+|"+'X'*b)  
     print("2-|"+'X'*c) 
     print("3 |"+'X'*d) 
     print("F |"+'X'*f)     

marks()