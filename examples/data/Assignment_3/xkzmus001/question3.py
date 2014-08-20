msg = input("Enter the message:\n")
count = eval(input("Enter the message repeat count:\n"))
thick = eval(input("Enter the frame thickness:\n"))

y = len(msg) + (thick*2)
bottomFrame = ''
for i in range(0,(thick)):
    frame = ("|"*i)+"+"+("-"*y)+"+"+("|"*i)
    bottomFrame += (frame+"\n")
    print(frame)
    y -= 2

for i in range(count):
    print("|"*thick,msg,"|"*thick)

pos = -2
bFrame = ''
for i in range(len(bottomFrame)-1):
            bFrame += bottomFrame[pos]
            pos -= 1
        
print(bFrame)