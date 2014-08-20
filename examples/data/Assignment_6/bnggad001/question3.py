print("Independent Electoral Commission")
print("--------------------------------")
print("Enter the names of parties (terminated by DONE):")

a=""  #initialise empty string
a=""

list_1=[]   #initialise array empty

while a != "DONE" :
    
    a=str(input())
    list_1.append(a)
    
list_1.remove("DONE") 
list_1.sort()

list_c=[]     
list_v=[]     

for i in list_1 :
    
    if i not in list_c :
        
        list_c.append(i)
        b=list_1.count(i)
        list_v.append(b)
        
print()

print("Vote counts:")

k=len(list_c)    

for i in range(k):
    
    list_pos1=list_c[i]    
    list_pos2=list_v[i]
    
    form_f = "{0:<10}".format(list_pos1)  
    print(form_f,"-",list_pos2)
    
    
        