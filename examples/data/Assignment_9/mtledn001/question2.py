inputFile = input('Enter the input filename:\n')
output = input('Enter the output filename:\n')
width = eval(input('Enter the line width:\n'))
f = open(inputFile,'r')
file = f.readlines()
f.close()
#for i in range(len(file)):
    #print(file[i])
#print(file)

f = open(output, 'w')
count = 0#Counts the letters we have already entered
for i in range(len(file)):
    
    p=file[i].replace('\n','')
    #print(p)
    p=p.split(' ')
    #print(p)
    for  k in p:
        if file[i]==['']:
            print('\n',file=f)
            continue
        elif count+len(k)>width:
            #print(file=f)
            print('\n'+k,end=' ', file = f)
            count=len(k)+1
        elif count+len(k)<width:
            print(k,end=' ',file = f)
            count+=len(k)+1
        elif count+len(k)==width:
            print(k,end='\n', file = f)
            count=0
f.close()
    