"""Program to print strings without duplicate
Micaela Narasmulu
3 May 2014"""

m=input("Enter strings (end with DONE):\n") 
st=[] #create empty string
newST=[]

while m!="DONE": 
    st.append(m) #moves inputed string to the end of the list each time
    m=input()  #continue asking user for input
    
for i in st:
    if not i in newST:#if input is an unique string it adds to the "unique list"
        newST.append(i)
        
print()

print("Unique list:")       

for p in newST:
    print(p)