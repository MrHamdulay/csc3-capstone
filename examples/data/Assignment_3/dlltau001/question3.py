

text = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
width = eval(input("Enter the frame thickness:\n"))

#text = "Test words"
#repeat = 5
#width = 6

count = 0
i = 0
line = 0
word = len(text) + width



while i != width:
   print("|"*line,"+","-"*(word+width),"+","|"*line,sep="")
   i += 1
   word = word - 2
   line = line + 1
   
    

while count != repeat:
   print("|"*width,text,"|"*width)
   count += 1
   
word = len(text) + 2
line = line - 1



while i != 0:
   print("|"*line,"+","-"*(word),"+","|"*line,sep="")
   i -= 1
   word = word + 2
   line = line - 1