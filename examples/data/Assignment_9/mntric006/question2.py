data = open (input("Enter the input filename:\n"), "r")
out = open (input("Enter the output filename:\n"), "w")
width = eval(input("Enter the line width:\n"))

array = []
for line in data:
    array.append(line[:-1].split(" "))
data.close ()
for i in range(len(array)):
    if array[i][len(array[i])-1] == "": del array[i][len(array[i])-1]
freshline = ""
first = True
for i in range(len(array)):
    for j in range(len(array[i])):
        if len(freshline) <= (width - len(array[i][j]) - 1):
            if first == True:
                freshline = array[i][j]
                first = False
            else:
                newline = freshline
                freshline = newline + " " + array[i][j]
        else:
            out.write(freshline+"\n")         
            freshline = array[i][j]
out.write(freshline)
out.close()
