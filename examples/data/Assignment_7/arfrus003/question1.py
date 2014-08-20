#create empty list
inputlist = []

#prompt for input
input_item = input("Enter strings (end with DONE):\n")

#loop until user enters "DONE"
while input_item !="DONE":
   inputlist.append (input_item)
   input_item = input ("")
print()
#create function that creates new list containing only unrepeated items
def uniq(inputlist):
    output = []
    for x in inputlist:
        if x not in output:
          output.append(x)
    print("Unique list:")    
    print("\n".join(output))
uniq(inputlist)