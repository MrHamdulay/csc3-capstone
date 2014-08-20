"""
Serayen Govender
Align list
25/04/14
"""

strings=[] #list of strings

inp_str= input("Enter strings (end with DONE):\n") # input next srting in list
print()
while inp_str!="DONE":
    strings.append(inp_str)
    
    inp_str= input()
#fill strings list 

longest=0 #length of longest strings

for i in range(len(strings)):
    
    if len(strings[i])>longest:
        longest=len(strings[i])
#find length of longest string
print("Right-aligned list: ")
    
for i in range (len(strings)):
    spaces=longest-len(strings[i]) #number of spaces to align string
    print(" "*spaces+strings[i])
    #prints list with enough spaces in front to right align
    