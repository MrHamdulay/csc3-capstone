#MZWNIC001/Nicholas Mazower    
#24/04/2014
#list right-aligner


global name
name=input("Enter strings (end with DONE):\n")
names=[name]
#this t is simply a dummy variable to make a while loop, it has no external significnace
t=1
while t>0:
    if name=="DONE":
        names.remove("DONE") #This step is to prevent 'DONE' from being included in the list of names
        break
    else:
        name=input("")
        names.append (name)

list_length=len(names)
#the list_ticker just controls the length of the loop, it may not be strictly necessary.
list_ticker=list_length
width=0
print("\nRight-aligned list:")
while list_ticker>0:
    for i in names:
        temp_width=len(i)
        if temp_width>width:
            width=temp_width
        list_ticker-=list_ticker
    for x in names:
        print('{:>{width}}'.format(x,width=width))

    
