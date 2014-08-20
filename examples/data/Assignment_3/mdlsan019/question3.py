#Sanele Mdlalose
#MDLSAN019#
#question3
mssg = input("Enter the message:\n")
mrc = eval(input("Enter the message repeat count:\n"))
frmthcknss = eval(input("Enter the frame thickness:\n"))

for i in range(frmthcknss):
    print('|'*i,"+","-"*len(mssg),"-"*(2*(frmthcknss-i)),"+",i*'|',sep="")
for i in range(mrc):
    print('|'*frmthcknss,mssg,'|'*frmthcknss)
for i in range(frmthcknss-1,-1,-1):
        print('|'*i,"+","-"*len(mssg),"-"*(2)*(frmthcknss-i),"+",i*'|',sep="")    
        