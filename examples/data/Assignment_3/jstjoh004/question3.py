#question 3

msg = input("Enter the message:\n")
msgrpt = eval(input("Enter the message repeat count:\n"))
frmthck = eval(input("Enter the frame thickness:\n"))
strlen = msg.__len__()

#top
for a in range(frmthck):
    print(a*"|"+"+"+(strlen+(frmthck-a)*2)*"-"+"+"+a*"|")


#middle
for b in range(msgrpt):
    print("|"*frmthck,msg,"|"*frmthck,sep=" ")
    
#bottom
for c in range(frmthck):
    print((frmthck-c-1)*"|"+"+"+(2+strlen+c*2)*"-"+"+"+(frmthck-c-1)*"|")
    
    



    

