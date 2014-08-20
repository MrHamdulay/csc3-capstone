#Grant Meeser
#MSRGRA002
#25/03/2014

msg=input('Enter the message:\n')
rmsg=eval(input('Enter the message repeat count:\n'))
bw=eval(input('Enter the frame thickness:\n'))
s=''

#print('+'+('-'*(bw+len(msg)+2+bw))+'+')
for b in range(bw-1):
	s=s+(('|'*b)+'+'+('-'*(bw+len(msg)+bw-(b*2)))+'+'+('|'*b))+'\n'

s=s+(('|'*(bw-1))+'+'+('-'*((bw-1)+len(msg)+2+bw-1-((bw-1)*2)))+'+'+('|'*(bw-1)))

smsg=((('|'*bw)+' '+msg+' '+('|'*bw)+'\n')*rmsg)

if bw>0:
	print(s)
print(smsg[:len(smsg)-1])
if bw>0:
	print(s[::-1])

