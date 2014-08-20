"""Align list of strings
Muzammil Jable
20 April 2014"""
name=""
names = []
print("Enter strings (end with DONE):")
name=input()
while name!="DONE": 
    count=0
    
    names.append(name)
    name=input("")

print("")

def longestString(names):
    new_list=[]
    for i in range(len(names)):
        new_list.append(len(names[i]))
        
    return new_list
        
        
    
def right_List(names):
    pos=0
    n_list=longestString(names)
    
    pos=max(n_list)
    
   
    for i in range(len(names)):
        n=names[i].rjust(pos)
        print(n)
                       
print("Right-aligned list:")
if len(names)!=0:
    right_List(names)  