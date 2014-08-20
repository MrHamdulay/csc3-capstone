# Tashiv Sewpersad
# CSC1015F
# Assignment 3 - Question 2

iHeight = eval(input("Enter the height of the triangle:\n"))
for i in range(1,iHeight+1):
  sSpace = (((2*iHeight-1)-(2*i-1))//2)*" "
  print(sSpace,(2*i-1)*"*",sSpace,sep="")
