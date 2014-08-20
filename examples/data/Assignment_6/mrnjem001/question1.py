"""Question 4 - right justify a series of names
Jembe Moran
25 April 2014"""
names=[]
x=input("Enter strings (end with DONE):\n")
wrdlength=0 #find longest word
while x != "DONE":
    names.append(x) #add input to list
    if len(x)>wrdlength: #keep track of word maximum
        wrdlength=len(x)
    x=input("") #ask for new input
print("\nRight-aligned list:")
for i in range(len(names)):
    names[i]=" "*(wrdlength-len(names[i]))+names[i] #add spaces to right justify
    print(names[i])