# Tashiv Sewpersad
# CSC1015F
# Assignment 3 - Question 1

iHeight = eval(input("Enter the height of the rectangle:\n"))
iWidth = eval(input("Enter the width of the rectangle:\n"))
sLine =""
for j in range(iWidth):
	sLine += "*"
if iHeight > 0:
	sRec = (sLine + "\n")*(iHeight-1) + sLine
else: 
	sRec = ""	
print(sRec)
  
