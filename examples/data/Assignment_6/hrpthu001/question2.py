"""program to do basic vector calculations
thushar hariparsad
20 april 2014"""

x=input("Enter vector A:\n")                
listA=x.split(" ")  #split inputs into list based on spaces
y=input("Enter vector B:\n")              
listB=y.split(" ")                         

ABadd=[]  #create list
for i in range(3):
    x=eval(listA[i])  #convert inputs to integers
    y=eval(listB[i])   
    add=x+y #add corresponding integers
    ABadd.append(add)  #append to list 

AB=0 
for j in range(3):
    x=eval(listA[j])                       
    y=eval(listB[j])                       
    multiply=x*y                            
    AB+=multiply                       
    
import math                  
sumN=0                                     
for k in range(3):
    x=eval(listA[k])   #convert list A inputs into integers
    sumN+=x**2  #square inputs and add to variable              
abs_x=math.sqrt(sumN)            
answer_x=round(abs_x,2)                     
if answer_x==0.0:
    answer_x=str(answer_x)+'0'
sumM=0                                     
for l in range(3):
    y=eval(listB[l])                       
    sumM+=y**2                             
abs_y=math.sqrt(sumM)   #root the sum of the squares of inputs
answer_y=round(abs_y,2)  #round answer to two decimal places
if answer_y==0.0:
    answer_y=str(answer_y)+'0'

print("A+B =",ABadd)                    
print("A.B =",AB)                  
print("|A| =",answer_x)        
print("|B| =",answer_y)