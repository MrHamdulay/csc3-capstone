'''elections programme 
Siphesihle Zwane
23/04/14'''
print('Independent Electoral Commission')
print('--------------------------------')
print('Enter the names of parties (terminated by DONE):')
box=[] #where all the votes are kept IEC
form='{0:<10}' #to organise the vertical list
while True:
    ballot=input('') #actual vote 
    if ballot=='DONE':
        break
    box.append(ballot)
print()
print('Vote counts:')
box.sort() #to get them in order
acc=0
for i in range(len(box)):
    
    if len(box)==1:
        i=0
        a=box[0]
        print(form.format(a),' - ',1,sep='')
        box.remove(a)
        break
    if len(box)==0:
            break    
    a=box[0]
    count=box.count(a)
    if count>=1:
        for i in range(count):
            box.remove(a)
        acc+=1
        print(form.format(a),' - ',count,sep='')

        
        