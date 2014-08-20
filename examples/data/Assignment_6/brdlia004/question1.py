"""Program to generate a right aligned list of inputted strings"""
#Liam Brodie
#4.20 2014
#BRDLIA004

NamList = []
print("Enter strings (end with DONE):")
i=""
while i != "DONE":
    i = input("")
    if i == "DONE":
        break
    elif i != "DONE":
        i = str(i)                    
        NamList.append(i)
        
def_max = 0
for x in NamList:
    if len(x) > def_max:
        def_max = len(x)
   
print()

print("Right-aligned list:")
for j in NamList:
    print(j.rjust(def_max))
    
