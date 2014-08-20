# krwane001

message = input("Enter the message:\n")
lenght = len(message)
count = int(input("Enter the message repeat count:\n"))
thick = int(input("Enter the frame thickness:\n"))
character = ""

for i in range(thick):
    print(character+"+"+"-"*(lenght+(2*thick))+"+"+character)
    character = character + "|"
    lenght = lenght-2
    
for j in range(count):
    print(character+" "+message+" "+character)
character1 = character
number = len(character)-1
lenght = len(message)

for k in range(thick):
    print(character1[0:number]+"+"+"-"*(lenght+2)+"+"+character1[0:number])
    number = number - 1
    lenght = lenght + 2
