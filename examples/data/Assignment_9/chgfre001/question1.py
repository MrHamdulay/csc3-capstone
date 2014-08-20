#python program to analyse student marks read n from a file
#FJChigwaza
#12 may 2014

import math
marks=input('Enter the marks filename:\n')
f=open(marks,'r')
lines_list=f.readlines()
f.close()



arr=[]
arr_names=[]
#print(lines_list)
for i in lines_list:
    
    line=i.split(',')
    #print(line)
    for k in line:
        new=k.replace('\n','')
        #print(k)
        #print(new)
        if new.isdigit():
            arr.append(new)
        else:
            #if k.isalpha():
            arr_names.append(new)
            #print(arr)
            #print(arr_names)

            

total=0
for l in arr:
    total+=int(l)    
xbar=round(total/len(arr),2)
if str(xbar)[-2]=='.':
    print('The average is: ',str(xbar)+'0',sep='' ) 
else:
    print('The average is: ',xbar,sep='' )


x=0
for nmbr in arr:
    x+=(int(nmbr)-xbar)*(int(nmbr)-xbar)
stdDev=round(math.sqrt(x/len(arr)),2)
if str(stdDev)[-2]=='.':
    print('The std deviation is: ',str(stdDev)+'0',sep='')
else:
    print('The std deviation is: ',stdDev,sep='')


cut_off=xbar-stdDev
ind=''
#counter=0
#print(len(arr))
#print(len(arr_names))
for nmbr in arr:
    if int(nmbr)<cut_off:
        #print(nmbr)
        ind+=arr_names[arr.index(nmbr)]+'\n'
        #counter+=1
#print(ind)        

if stdDev>0:
    print('List of students who need to see an advisor:')
    print(ind)
   


   
    
    
    

 