"""program to print a right aligned list of things
thushar hariparsad
20 april 2014"""

print("Enter strings (end with DONE):")     
s_list=[]  #create sentinel loop for continuous inputs
while True:                                 
    x=input("")
    if x=='DONE': break                
    else:
        s_list.append(x) #add on to list of strings

max_len=0                                   
for i in s_list:
    if len(i)>max_len:
        max_len=len(i)   #find length of longest string
    else: ""

print()
print("Right-aligned list:")
for j in s_list:
    gap=max_len-len(j) #find gap
    print(gap*" "+j)                     