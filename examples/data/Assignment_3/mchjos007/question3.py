mes = input("Enter the message:\n")
repc = eval(input("Enter the message repeat count:\n"))
frat = eval(input("Enter the frame thickness:\n"))
for i in range (frat):
    print ("|"*i +"+" + "-"* (len(mes)+((frat-i)*2))+"+"+ "|"*i )
for i in range (repc):
    print ("|"*frat +" " + mes + " " +"|"*frat)
for i in range (frat):
    print ("|"*(frat-(i+1)) +"+" + "-"* (len(mes)+((i+1)*2))+"+"+ "|"*(frat -(i+1)))