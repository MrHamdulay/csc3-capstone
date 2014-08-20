string=""
listing=[]
string = input("Enter strings (end with DONE):\n")
while string != "DONE":
    listing.append(string)
    string = input("")

print()

p=-1
maxi=0
for i in range(len(listing)-1):
    test=len(listing[p+1])
    length=len(listing[i+1])
    p+=1
    
    if length > maxi:
    
        if length > test:
            maxi = length
            
        else:
            maxi = test
   
    else:
        continue

print("Right-aligned list:")
for i in range(len(listing)):
    form="{0:" ">{1}}"
    print(form.format(listing[i],maxi))

    