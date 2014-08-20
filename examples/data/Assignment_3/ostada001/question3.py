msg = input("Enter the message:\n")
rpt = eval(input("Enter the message repeat count:\n"))
thk = eval(input("Enter the frame thickness:\n"))

msg = " "+msg+" "

length = len(msg)+(thk-1)*2
lm = len(msg)
for i in range (0,thk,1):
    print(("|"*i)+("+")+("-"*(length)+("+")+("|"*i)))
    if (length > lm):
        length -= 2
          
      
print((thk*"|"+(msg)+thk*"|"+"\n")*rpt,end = "")    
length = len(msg)
for i in range (1,thk+1,1):
    print(("|"*(thk-i))+("+")+("-"*(length)+("+")+("|"*(thk-i))))
    if (length <= lm+(thk-1)*2):
        length += 2    