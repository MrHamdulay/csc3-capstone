# Yentl Naidu (NDXYEN001)
# Assignment 3
# 26 March 2014
# Question 3

message = input("Enter the message:\n")
repeats = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

frame = len(message)*2 + thickness*2

for i in range(0, thickness) :
  print("|"*i + "+" + "-"*((frame-(i+1)*2)-len(message)+2) + "+" + "|"*i)
  
for repeat in range(repeats):
  print("|"*thickness,message,"|"*thickness)
  
for i in reversed(range(0,thickness)) :
  print("|"*(i) + "+" + "-"*((frame-(i+1)*2)-len(message)+2) + "+" + "|"*(i))