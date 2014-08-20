#Assignment 3 Q3
#Charlie Shang  
#SHNHUA002

sMessage = input('Enter the message:\n')
iRep = eval(input('Enter the message repeat count:\n'))
iThick = eval(input('Enter the frame thickness:\n'))
iLen = len(sMessage)
i = 0
j = 0
iExtra = iThick * 2 # extra '-'
for i in range(iThick):
    print('|'*i, '+' , '-'*(iLen+iExtra) , '+' , '|'*i, sep = '')
    iExtra -= 2

for j in range(iRep):
    print('|'*iThick, sMessage, '|'* iThick)

for i in range(iThick):
    iExtra += 2
    print('|'*(iThick-1-i), '+' , '-'*(iLen+iExtra) , '+' , '|'*(iThick-1-i), sep = '')