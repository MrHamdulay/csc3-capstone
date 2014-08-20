input_file=input("Enter the input function:\n")
#output_file=input("Enter the output function:\n")
width=eval(input("Enter the line width:\n"))
in_file=open(input_file,"r")
who=in_file.read()
in_file.close()
#whole=who.split(" ")


for i in range(len(who)):
    if i%width==0:
        if who[i+1]==" ":
            print()
        else:
            print(" 12345")
    print(who[i],end="")
