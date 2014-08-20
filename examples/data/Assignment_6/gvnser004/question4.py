"""
Serayen Govender
Histogram
25/04/14
"""

marks = input("Enter a space-separated list of marks:\n")
# mark input
mark_list = marks.split()
#list of marks


f= 0
thrd = 0
low = 0
up = 0
frst = 0 
#positions

for j in range (len(mark_list)):
    
    mark_list[j] = eval(mark_list[j])
    
    #turn mark_list to integers


    
for i in mark_list:
    
    if ( 0 <= i < 50):
        f+=1
        
    elif (i< 60): 
        thrd+=1
        
    elif (i < 70):
        low+=1
        
    elif (i < 75):
        up+=1
        
    else:
        frst+=1
        
print("1 |","X"*frst,sep='')
print("2+|","X"*up,sep='')
print("2-|","X"*low,sep='')
print("3 |","X"*thrd,sep='')
print("F |","X"*f,sep='')
        #print histogram