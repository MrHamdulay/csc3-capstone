#nasha meoli
#program to print mesage in frame
#22nd february 2014

message = input("Enter the message:\n")
repeat = eval(input("Enter the message repeat count:\n"))
thickness = eval(input("Enter the frame thickness:\n"))

def fancyframe():
        count2 = thickness
        count = 0 
        count3=1
        count4=thickness-1
        for i in range(thickness):
                print("|"*count+"+"+"-"*count2+"-"*len(message)+"-"*count2+"+"+"|"*count)
                count+=1
                count2-=1
        for i in range(repeat):
                print("|"*thickness,message,"|"*thickness)
        for i in range(thickness):
                print("|"*count4+"+"+"-"*count3+"-"*len(message)+"-"*count3+"+"+"|"*count4)
                count3+=1
                count4-=1
fancyframe()

        
