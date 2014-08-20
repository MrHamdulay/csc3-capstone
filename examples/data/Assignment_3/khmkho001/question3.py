#Assignment 3
#question3.py
#Author: Nelisa Khumalo

mes=input("Enter the message: \n")
Msg_RepCount=eval(input("Enter the message repeat count: \n"))
Frame_Thickness=eval(input("Enter the frame thickness: \n"))

#Loop 1 for printing of upper frame
lengte = len(mes) + 2 * Frame_Thickness
no_v_sye = 0
for i in range(Frame_Thickness):
    print("|"*no_v_sye,"+", "-"*lengte,"+","|"*no_v_sye, sep="")
    lengte = lengte - 2 # same as lengte -= 2
    no_v_sye = no_v_sye + 1
    #print("|"*1,"+", "-"*(len(message)+(2*2 - 2*1)),"+","|"*1, sep="")
    
    #Loop 2 for printing of the message
for j in range(Msg_RepCount):
    print("|"*Frame_Thickness, mes, "|"*Frame_Thickness)
        
#Loop 3 for bottom frame - PART 2
lengte = len(mes) + 2
no_v_sye = Frame_Thickness - 1
for k in range(Frame_Thickness):
    print("|"*no_v_sye,'+', '-'*lengte, '+','|'*no_v_sye, sep='')
    lengte = lengte + 2
    no_v_sye = no_v_sye - 1
#print("+", '-'*(len(message)+(2*2)),'+', sep='')

