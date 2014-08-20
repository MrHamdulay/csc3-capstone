message=input('Enter the message:''\n')
repeat=eval(input('Enter the message repeat count:''\n'))
thickness=eval(input('Enter the frame thickness:''\n'))

a= len(message)
def messagelength(repeat):
    b=a+2
    c=thickness
    f=c-1
    if repeat:
        d=b+(c)
        e=0
        for z in range(d+(c-2),b-1,-2):
                print('|'*e+'+'+'-'*(z)+'+'+'|'*e)
                e+=1
        
             
        for i in range(repeat):
            print(('|'*(c)+' '+message+' '+'|'*(c))*(repeat-(repeat-1)),sep='/n')
        
        for z in range(b,d+c,2):
                print('|'*(f)+'+'+'-'*(z)+'+'+'|'*(f))
                f=f-1
        

messagelength(repeat)






