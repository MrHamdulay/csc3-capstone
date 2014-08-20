message = input("Enter the message: \n")
count = eval(input("Enter the message repeat count: \n"))
thickness = eval(input("Enter the frame thickness: \n"))

leng = len(message)

plus = 1
minus = leng+(thickness*2)+2
pole = -1

for i in range(thickness):
    pole += 1
    minus -= 2    
    print("|"*pole, "+", "-"*minus, "+", "|"*pole, sep="")
   
pol = pole + 1

for i in range(count):
    print("|"*pol, " ", message, " ", "|"*pol, sep="")
    
for i in range(thickness):
    print("|"*pole, "+", "-"*minus, "+", "|"*pole, sep="")
    pole -= 1
    minus += 2

# +---------------+
# |+-------------+|
# || Hello World ||
# || Hello World ||
# || Hello World ||
# |+-------------+|
# +---------------+