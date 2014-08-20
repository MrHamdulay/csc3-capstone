message = input("Enter the message:\n")
rows = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))

uprights1 = 0
for i in range(frame + 1, 1, -1):
    print('|'*uprights1 + '+', '+' + '|'*uprights1, sep = '-'*(len(message) - 2 + 2*i))
    uprights1 += 1
    
for i in range(rows):
    print ('|'*frame, message, '|'*frame)

uprights2 = frame - 1
for i in range(1, frame + 1):
    print('|'*uprights2 + '+', '+' + '|'*uprights2, sep = '-'*(len(message) + 2*i))
    uprights2 -= 1    
             

