# Sohail Tulsi TLSSOH001
# 24/03/2014
# frameing words

word= input('Enter the message:\n')
repeat = eval(input('Enter the message repeat count:\n'))
thick= eval(input('Enter the frame thickness:\n'))
x=len(word)

for i in range(thick):
    print("|"*i,'+','-'*(x+(thick*2)),'+',"|"*i,sep='')
    x-=2

for i in range(repeat):
    print('|'*thick,word,'|'*thick)

for i in range(thick):
    x+=2
    print("|"*(thick-i-1),'+','-'*(x+(thick*2)),'+',"|"*(thick-i-1),sep='')
