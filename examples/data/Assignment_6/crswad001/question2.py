'''Wade Cresswell Question 2'''
import math
vas= input('Enter vector A:\n')
vbs= input('Enter vector B:\n')
vectA = vas.split(' ') # creating the list containing the vectors
vectB = vbs.split(' ')
vAB = [eval(vectA[0])+eval(vectB[0]),eval(vectA[1])+eval(vectB[1]),eval(vectA[2])+eval(vectB[2])] #adding the vectors
vATB = eval(vectA[0])*eval(vectB[0])+eval(vectA[1])*eval(vectB[1])+eval(vectA[2])*eval(vectB[2]) #MULTIPLYING the vectors
nA = round(math.sqrt(pow(eval(vectA[0]),2)+pow(eval(vectA[1]),2)+pow(eval(vectA[2]),2)),2) #NORM A
nB = round(math.sqrt(pow(eval(vectB[0]),2)+pow(eval(vectB[1]),2)+pow(eval(vectB[2]),2)),2) #NORM B
print('A+B =',vAB)
print('A.B =',vATB) # PRINTING ALL THE RESULTS

if nA!=0:
   print('|A| =',nA) 
else:
   print('|A| =','0.00')
if nB!=0:
   print('|B| =',nB) 
else:
   print('|B| =','0.00')   


