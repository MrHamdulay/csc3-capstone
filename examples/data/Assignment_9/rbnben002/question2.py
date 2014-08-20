user = input("Enter the input filename:\n")
user1 = input("Enter the output filename:\n")
user2 = eval(input("Enter the line width:\n"))
f = open(user, "r")
f1 = open(user1,"w")
lines = ""
count = 0
for line in f:  
    if line == "\n":
        lines = lines + "\n"
    else:
        user2n = line[:-1]
        user2ords = user2n.split(" ")
        for pp in(user2ords):
            count = count + len(pp)+1    
            if count <= user2:
                lines = lines + pp + " "                
            else:
                lines = lines + "\n" + pp + " "
                count = 0
print(lines,file = f1)
f.close()
f1.close()
        