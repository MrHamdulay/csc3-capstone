def repeat():
    print("|"*thick,msg,"|"*thick)
def frame():
    msg=str(input("Enter the message:\n"))
    rpt=eval(input("Enter the message repeat count:\n"))
    thick=eval(input("Enter the frame thickness:\n"))
    for j in range(thick,0,-1):
        print("|"*(thick-j)+"+"+"-"*j+"-"*len(msg)+"-"*j+"+"+"|"*(thick-j))
    #print("|"+"+-"+"-"*len(msg)+"-+"+"|")
    for i in range(rpt):
        print("|"*thick,msg,"|"*thick)
    for h in range(thick):
        print("|"*((thick-1)-h)+"+"+"-"*(h+1)+"-"*len(msg)+"-"*(h+1)+"+"+"|"*(thick-1-h))   
    #print("|"+"+-"+"-"*len(msg)+"-+"+"|")
    #print("+"+"--"+"-"*len(msg)+"--"+"+")
frame()