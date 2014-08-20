strings=[]
string=input("Enter strings (end with DONE):\n")
while  string!="DONE":
    strings.append(string)
    string=input("")
print()    
print("Right-aligned list:")
mlength=0
for stre in range (len(strings)):
    if len(strings[stre])>mlength:
        mlength=len(strings[stre])

if len(strings)!=0:
    for string in strings:
        print("{0:>{1}}".format(string,mlength))
    #if len(string)==d:
       #print(string)   
    
    #elif (len(string))!=d:
      # print(" "*(d-len(string)),"\n".join(strings))