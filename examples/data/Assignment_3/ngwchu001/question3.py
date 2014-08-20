print("Enter the message:")
message=(input())
print("Enter the message repeat count:")
count=eval(input())
print("Enter the frame thickness:")
thick=eval(input())

word=(len(message)+2)

for m in range(count):
  print(" ",message,"")
print("+"+word*"-"+"+") 
  