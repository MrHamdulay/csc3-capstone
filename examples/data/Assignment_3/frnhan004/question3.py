message = input("Enter the message:\n")
repeats = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))


widthWithFrame = len(message) + thickness*2 + 2

for i in range(0, thickness):
  print("|"*i + "+" + "-"*(widthWithFrame-(i+1)*2) + "+" + "|"*i)
  
for i in range(0,repeats):
  print("|"*thickness + " " + message + " " + "|"*thickness) 

for i in reversed(range(0, thickness)):
  print("|"*i + "+" + "-"*(widthWithFrame-(i+1)*2) + "+" + "|"*i)  



 