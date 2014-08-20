"""
Serayen Govender
count votes for parties
25/04/14
"""

print("Independent Electoral Commission\n--------------------------------")
inp_str = input("Enter the names of parties (terminated by DONE):\n")
print()
inp_list = [ ]
#list of inputs
while (inp_str != "DONE"):
    
    inp_list.append(inp_str)    
    
    inp_str = input()
    #fill list of inputs
    
part=[] #list of parties
for i in range (len(inp_list)):
    
    if(inp_list.index(inp_list[i])==i):
        
        part.append(inp_list[i]) 
        
part.sort()  #sort parties    

c=[]
#list to count votes

for i in range (len(part)):
    c.append(0)

for i in range(len(part)):
    
    for j in range(len(inp_list)):
        
        if(inp_list[j]==part[i]):
            
            c[i]+=1
 #count number of votes for each party           

print("Vote counts:")

for i in range(len(part)):
    print("{0:<10} - {1}".format(part[i],c[i]))
    #align and print party names and votes
    
