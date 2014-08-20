#Grant Meeser
#MSRGRA002
#24/04/2014

print('Enter a space-separated list of marks:')
marks = input().split(' ')

st=0
nd=0
rd=0
th=0
fail=0

for i in marks:
	i=int(i)
	if i<50:
		fail+=1
	elif 50<=i<60:
		th+=1
	elif 60<=i<70:
		rd+=1
	elif 70<=i<75:
		nd+=1
	else:
		st+=1

print('1 |'+('X'*st))
print('2+|'+('X'*nd))
print('2-|'+('X'*rd))
print('3 |'+('X'*th))
print('F |'+('X'*fail))

