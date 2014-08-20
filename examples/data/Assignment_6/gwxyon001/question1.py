#string aligner
#YONGAMA GIWU
#20 april 2014
accumulator=[]
#string=input('Enter strings (end with DONE):\n')
print('Enter strings (end with DONE):')
while True:
    string=input('')
    #accumulator+=string
    if string=='DONE':
        print()
        break    
    accumulator.append(string)
l=len(accumulator) 
for i  in range(l):
    maxr=len(accumulator[0])
    word=accumulator[i]
    max1=len(word)
    if max1>=maxr:
        maxr=max1
print('Right-aligned list:')
for i in range(l):
    word=accumulator[i]
    l2=len(word)
    print(' '*(maxr-len(word)),word,sep='')
    