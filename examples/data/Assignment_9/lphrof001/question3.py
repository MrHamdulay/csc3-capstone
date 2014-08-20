filename=input("Put in filename:\n")
f=open(filename,"r")
line=f.read()
f.close()
#print(line)
li=line.split("\n")
#print(li)

n=len(li)
for i in range(n):
 countLi={}
 for j in li[i]:
  if not j in countLi:
   countLi[j]=1
  else:
   countLi[j]+=1
coun=0
for i in range(n):
 for j in li[i]:
  if countLi[j]>1:
   coun+=1
print(coun)

#function to get the sudoku in the opposite direction
#def turn(n):
lin=""
for i in range(n):
 for j in range(n):
  lin+=li[j][i]
 lin+=","
lin=lin.split(",")
del(lin[9])
#print(lin)

n=len(lin)
for i in range(n):
 countLin={}
 for j in lin[i]:
  if not j in countLin:
   countLin[j]=1
  else:
   countLin[j]+=1
coun2=0
for i in range(n):
 for j in lin[i]:
  if countLin[j]>1:
   coun2+=1
print(coun2)

if coun2>0 or coun>0:
 print("Sudoku grid is not valid")
else:
 print("Sudoku grid is valid")





