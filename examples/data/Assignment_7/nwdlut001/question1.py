strings=[]
string=input("Enter strings (end with DONE):\n")
while string!="DONE":
  
  strings.append(string)
  string=input("")
print()
print("Unique list:")
newstrings=list(set( strings))
newstrings.sort(key=strings.index)
print("\n".join(newstrings))
