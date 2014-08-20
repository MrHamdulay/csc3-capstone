print("Enter strings (end with DONE):")

b=""  
l_ist=[]  #open empty array

while b != "DONE" :
    
    b=str(input())
    l_ist.append(b)
    
k = len(l_ist) #output length of list to k  
len_lis=[]   

for j in range(k):
    
    a=l_ist[j]   # access pos j on list
    length_a=len(a)  
    len_lis.append(length_a)
    
print()
    
print("Right-aligned list:")

max_length=max(len_lis)
z=max_length  

for l in range(k-1):  
    
    r=l_ist[l]
    x=len(r)    
    print(" "*(z-x),r,sep="")