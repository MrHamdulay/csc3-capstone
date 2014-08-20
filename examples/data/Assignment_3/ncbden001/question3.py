message = input("Enter the message:  \n")
repeat = eval(input("Enter the message repeat count: \n"))
thickness= eval(input("Enter the frame thickness:  \n"))
top = 1
bottom = 1
decr = thickness-1
hyphen = (len(message)+2)
dash = (len(message)+2)+2*((thickness)-1)-2
if repeat!= "" and message!="Hello" and thickness!="" :
        print("+"+ ((len(message)+2)+(2*(thickness-1)))*"-" +"+")          
for i in range(thickness-1):
        while top < thickness:
                        print((top)*"|"+"+" + dash*"-" +"+" + (top)*"|")
                        top = top + 1
                        dash = dash -2
for j in range(repeat):
        print(thickness*"|"+" "+ message +" "+ thickness*"|")        

for k in range(thickness-1):
        while bottom < thickness:
                        print((decr)*"|"+"+" + hyphen*"-" +"+" + (decr)*"|")
                        bottom = bottom +1
                        hyphen = hyphen +2
                        decr = decr -1
if repeat!= "" and message!="Hello" and thickness!="" :       
        print("+"+ ((len(message)+2)+(2*(thickness-1)))*"-" +"+")