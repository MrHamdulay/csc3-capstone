#26 March 2014           #Mazwi Myeza
#Assignment3             #Question3

text = input("Enter the message:\n")
repeater = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
length = len(text)
j = frame
c = 0
for k in range(frame):
    trim = "+"+j*"-"+length*"-"+j*"-"+"+"
    print(c*"|"+trim+c*"|")
    c+= 1
    j -= 1
    
for i in range(repeater):
    print(frame*"|"+" "+text+" "+frame*"|")
e = 1
d = frame-1    
for k in range(frame):
    
    trim = "+"+e*"-"+length*"-"+e*"-"+"+"
    print(d*"|"+trim+d*"|")
    d -= 1
    e += 1    