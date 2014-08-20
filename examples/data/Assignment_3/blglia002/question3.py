word = input("Enter the message:\n")
rep = eval(input("Enter the message repeat count:\n"))
frame = eval(input("Enter the frame thickness:\n"))
#word1=len(word)-1

for i in range(frame,0,-1):
    print('|'*(frame-i),'+','-'*(i),len(word)*'-','-'*(i),'+','|'*(frame-i),sep='')

for i in range(rep):
    print(('|'*frame),word,('|'*frame))    
    
for i in range(1,frame+1):
    print('|'*(frame-i),'+','-'*(i),len(word)*'-','-'*(i),'+','|'*(frame-i),sep='')    