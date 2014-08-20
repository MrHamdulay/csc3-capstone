# Nikhil Gilbert
# May 15th 2014
# Programme to format the text of a file

# gets intput from user
infile = input("Enter the input filename:\n")
outfile = input("Enter the output filename:\n")
line_width = eval(input("Enter the line width:\n"))
f = open(infile, "r")
inFilelist = f.readlines()
inFilelist = [line.rstrip() for line in inFilelist]
f.close()
create = open(outfile,"w")

# this part sorts the input into an appropriate format 
sort = (" ").join(inFilelist)
newlist = sort.split(" ")
ceiling = line_width
linekeeper = []
for i in newlist: #cycle through all the stuff in the list
    if i == '' and len(inFilelist)>8:
        printer2 = (" ").join(linekeeper)
        print (printer2,file=create)
        print(file=create)
        count = 0
        accountant = 0
        linekeeper = []                
    # the following nested for loops check the number of characters in the linekeeper list
    count = 0
    for a in range (len(linekeeper)):
        for j in linekeeper[a]:
            if i != '':
                count = count+1
            elif i == '' and len(inFilelist)<5:
                count= count+1
        # this line allows for an total keeper that tracks the grand total of the line count that includes spaces that will be included in the print versionif 
    accountant = count + len(linekeeper) - 1
        # this part checks whether the count will be above 40, if not, it adds the item to the list     
    if len(i) + accountant < ceiling:
        if i != '':
            linekeeper.append(i)
        elif i == '' and len(inFilelist)<5:
            linekeeper.append(i)
        # if the count of the item and current charcter count in list is greater than the intended ceiling
    elif len(i) + accountant >= ceiling:
        printer = (" ").join(linekeeper)
        print (printer,file=create)
        count = 0
        accountant = 0
        linekeeper = []
        linekeeper.append(i)
    # this last part ensures that the final bits are printed if not triggered by the above 40 condition
if len(linekeeper) != 0:
    newprint = (" ").join(linekeeper)
    print (newprint,file=create) 
#Closes file
create.close()