inp=""
maxlen=0 #integer to help determine spaces from left
print("Enter strings (end with DONE):")
strings=[]
while(inp!="DONE"):    
    inp=input() # get input
    if(inp!="DONE"):
        strings.append(inp) # add input to string
        if(maxlen<len(inp)):
            maxlen=len(inp) # re-assign max length value if needed
print("\n","Right-aligned list:",sep="")

for i in range(len(strings)):
    
    print(" "*(maxlen-len(strings[i])),strings[i],sep="") # print output